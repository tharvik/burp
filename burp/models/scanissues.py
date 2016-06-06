from base64 import b64decode
from itertools import chain

from typing import MutableMapping, Any, Mapping, NamedTuple, Tuple, Iterator, Dict, Union

from burp.models import IssueType
from burp.models.enums import IssueSeverity, IssueConfidence
from burp.models.errors import InvalidHttpVersion
from burp.utils.json import ensure, JsonParser, pop_all, translate_keys, ensure_values


def _common_request_response_from_json(json: MutableMapping[str, Any]) -> Dict[str, Any]:
    return dict(
        host=json.pop('host'),
        port=ensure(int, json.pop('port')),
        protocol=json.pop('protocol'),
        raw=b64decode(json.pop('raw').encode()),
    )


class Request(NamedTuple('Request', [
    ('host', str),
    ('port', int),
    ('protocol', str),
    ('raw', bytes),
])):
    pass


class RequestReturned(NamedTuple('RequestReturned', [
    ('host', str),
    ('port', int),
    ('protocol', str),
    ('raw', bytes),
    ('http_version', Tuple[int, int]),
    ('in_scope', bool),
    ('reference_id', int),
    ('tool_flag', int),
])):
    @staticmethod
    def __parse_http_version(value: str) -> Tuple[int, int]:
        # TODO duplicate from sitemap
        try:
            protocol, version = value.split('/')
            if protocol != 'HTTP':
                raise ValueError()
            major, minor = version.split('.')
            return int(major), int(minor)
        except ValueError:
            raise InvalidHttpVersion(value)

    @classmethod
    def from_json(cls, json: MutableMapping[str, Any]) -> 'RequestReturned':
        with JsonParser(json):
            return RequestReturned(
                http_version=cls.__parse_http_version(json.pop('httpVersion')),
                in_scope=ensure(bool, json.pop('inScope')),
                reference_id=ensure(int, json.pop('referenceID')),
                tool_flag=ensure(int, json.pop('toolFlag')),
                **_common_request_response_from_json(json)
            )


class Response(NamedTuple('Response', [
    ('host', str),
    ('port', int),
    ('protocol', str),
    ('raw', bytes),
])):
    pass


class ResponseReturned(NamedTuple('ResponseReturned', [
    ('host', str),
    ('port', int),
    ('protocol', str),
    ('raw', bytes),
    ('status_code', int),
    ('in_scope', bool),
    ('reference_id', int),
    ('tool_flag', int),
])):
    @classmethod
    def from_json(cls, json: MutableMapping[str, Any]) -> 'ResponseReturned':
        with JsonParser(json):
            return ResponseReturned(
                in_scope=ensure(bool, json.pop('inScope')),
                **dict(chain(
                    _common_request_response_from_json(json).items(),
                    pop_all(translate_keys(ensure_values(int, json), {
                        'statusCode': 'status_code',
                        'referenceID': 'reference_id',
                        'toolFlag': 'tool_flag',
                    })).items()),
                )
            )


class ScanIssue(NamedTuple('ScanIssue', [
    ('url', str),
    ('host', str),
    ('port', int),
    ('protocol', str),  # TODO maybe enum
    ('name', str),
    ('issue_type', IssueType),
    ('severity', IssueSeverity),
    ('confidence', IssueConfidence),
    ('issue_background', str),
    ('remediation_background', str),
    ('issue_detail', str),
    ('remediation_detail', str),
    ('requests_responses', Tuple[Tuple[Request, Response], ...]),
])):
    def __new__(cls, host: str, port: int, protocol: str,
                **kwargs: Union[str, IssueType, IssueSeverity, Tuple[Tuple[Request, Response], ...]]) \
            -> 'ScanIssue':
        url = '{}://{}:{}/'.format(protocol, host, port)
        return super().__new__(cls, url=url, host=host, port=port, protocol=protocol, **kwargs)

    def to_json(self) -> Mapping[str, Any]:
        return dict(
            url=self.url,
            host=self.host,
            port=self.port,
            protocol=self.protocol,
            name=self.name,
            issueType=self.issue_type.value,
            severity=self.severity.value,
            confidence=self.confidence.value,
            issueBackground=self.issue_background,
            remediationBackground=self.remediation_background,
            issueDetail=self.issue_detail,
            remediationDetail=self.remediation_detail,
            requestResponses=[(req.to_json(), res.to_json()) for req, res in self.requests_responses],
        )


class ScanIssueReturned(NamedTuple('ScanIssueReturned', [
    ('url', str),
    ('host', str),
    ('port', int),
    ('protocol', str),  # TODO maybe enum
    ('name', str),
    ('issue_type', IssueType),
    ('severity', IssueSeverity),
    ('confidence', IssueConfidence),
    ('issue_background', str),
    ('remediation_background', str),
    ('issue_detail', str),
    ('remediation_detail', str),
    ('in_scope', bool),
    ('requests_responses', Tuple[Tuple[RequestReturned, ResponseReturned], ...]),
])):
    @staticmethod
    def _get_requests_responses(json: MutableMapping[str, Any]) \
            -> Iterator[Tuple[RequestReturned, ResponseReturned]]:
        for item in json.pop('requestResponses'):
            request, response = item.pop('request'), item.pop('response')
            yield RequestReturned.from_json(request), ResponseReturned.from_json(response)

    @classmethod
    def from_json(cls, json: MutableMapping[str, Any]) -> 'ScanIssueReturned':
        with JsonParser(json):
            json.pop('messageType', None)  # TODO maybe more than one type?
            return ScanIssueReturned(
                port=ensure(int, json.pop('port')),
                issue_type=IssueType(json.pop('issueType')),
                severity=IssueSeverity(json.pop('severity')),
                confidence=IssueConfidence(json.pop('confidence')),
                in_scope=ensure(bool, json.pop('inScope')),
                requests_responses=tuple(cls._get_requests_responses(json)),
                **pop_all(translate_keys(ensure_values(str, json), {
                    'issueBackground': 'issue_background',
                    'remediationBackground': 'remediation_background',
                    'issueDetail': 'issue_detail',
                    'remediationDetail': 'remediation_detail',
                }))
            )
