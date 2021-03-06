from enum import Enum


class IssueSeverity(Enum):
    INFORMATION = 'Information'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'


class IssueConfidence(Enum):
    CERTAIN = 'Certain'
    FIRM = 'Firm'
    TENTATIVE = 'Tentative'


class IssueType(Enum):
    ASPNET_VIEWSTATE_WITHOUT_MAC_ENABLED = 4195840
    ASPNET_DEBUGGING_ENABLED = 1050624
    ASPNET_TRACING_ENABLED = 1049216
    AJAX_REQUEST_HEADER_MANIPULATION_DOM_BASED = 5245952
    AJAX_REQUEST_HEADER_MANIPULATION_REFLECTED_DOM_BASED = 5245953
    AJAX_REQUEST_HEADER_MANIPULATION_STORED_DOM_BASED = 5245954
    BASE64_ENCODED_DATA_IN_PARAMETER = 7340544
    BROWSER_CROSS_SITE_SCRIPTING_FILTER_DISABLED = 5245360
    CACHEABLE_HTTPS_RESPONSE = 7340288
    CLEARTEXT_SUBMISSION_OF_PASSWORD = 3145984
    CLIENT_SIDE_JSON_INJECTION_DOM_BASED = 2098032
    CLIENT_SIDE_JSON_INJECTION_REFLECTED_DOM_BASED = 2098033
    CLIENT_SIDE_JSON_INJECTION_STORED_DOM_BASED = 2098034
    CLIENT_SIDE_SQL_INJECTION_DOM_BASED = 2097968
    CLIENT_SIDE_SQL_INJECTION_REFLECTED_DOM_BASED = 2097969
    CLIENT_SIDE_SQL_INJECTION_STORED_DOM_BASED = 2097970
    CLIENT_SIDE_XPATH_INJECTION_DOM_BASED = 2098016
    CLIENT_SIDE_XPATH_INJECTION_REFLECTED_DOM_BASED = 2098017
    CLIENT_SIDE_XPATH_INJECTION_STORED_DOM_BASED = 2098018
    CLIENT_SIDE_TEMPLATE_INJECTION = 2097928
    CONTENT_TYPE_INCORRECTLY_STATED = 8389632
    CONTENT_TYPE_IS_NOT_SPECIFIED = 8389888
    COOKIE_MANIPULATION_DOM_BASED = 5245696
    COOKIE_MANIPULATION_REFLECTED_DOM_BASED = 5245697
    COOKIE_MANIPULATION_STORED_DOM_BASED = 5245698
    COOKIE_SCOPED_TO_PARENT_DOMAIN = 5243648
    COOKIE_WITHOUT_HTTPONLY_FLAG_SET = 5244416
    CREDIT_CARD_NUMBERS_DISCLOSED = 6292736
    CROSS_DOMAIN_POST = 4195584
    CROSS_DOMAIN_REFERER_LEAKAGE = 5243904
    CROSS_DOMAIN_SCRIPT_INCLUDE = 5244160
    CROSS_SITE_REQUEST_FORGERY = 2098944
    CROSS_SITE_SCRIPTING_DOM_BASED = 2097936
    CROSS_SITE_SCRIPTING_REFLECTED_DOM_BASED = 2097937
    CROSS_SITE_SCRIPTING_REFLECTED = 2097920
    CROSS_SITE_SCRIPTING_STORED_DOM_BASED = 2097938
    CROSS_SITE_SCRIPTING_STORED = 2097408
    DOM_DATA_MANIPULATION_DOM_BASED = 5247488
    DOM_DATA_MANIPULATION_REFLECTED_DOM_BASED = 5247489
    DOM_DATA_MANIPULATION_STORED_DOM_BASED = 5247490
    DATABASE_CONNECTION_STRING_DISCLOSED = 6291584
    DENIAL_OF_SERVICE_DOM_BASED = 5246208
    DENIAL_OF_SERVICE_REFLECTED_DOM_BASED = 5246209
    DENIAL_OF_SERVICE_STORED_DOM_BASED = 5246210
    DIRECTORY_LISTING = 6291712
    DOCUMENT_DOMAIN_MANIPULATION_DOM_BASED = 5247232
    DOCUMENT_DOMAIN_MANIPULATION_REFLECTED_DOM_BASED = 5247233
    DOCUMENT_DOMAIN_MANIPULATION_STORED_DOM_BASED = 5247234
    DUPLICATE_COOKIES_SET = 4196864
    EMAIL_ADDRESSES_DISCLOSED = 6291968
    EXPRESSION_LANGUAGE_INJECTION = 1052448
    EXTENSION_GENERATED_ISSUE = 134217728
    EXTERNAL_SERVICE_INTERACTION_DNS = 3146240
    EXTERNAL_SERVICE_INTERACTION_HTTP = 3146256
    FILE_PATH_MANIPULATION = 1051392
    FILE_PATH_TRAVERSAL = 1049344
    FILE_UPLOAD_FUNCTIONALITY = 5245312
    FLASH_CROSS_DOMAIN_POLICY = 2098176
    FRAMEABLE_RESPONSE_POTENTIAL_CLICKJACKING = 5245344
    HTML_DOES_NOT_SPECIFY_CHARSET = 8389120
    HTML_USES_UNRECOGNIZED_CHARSET = 8389376
    HTML5_CROSS_ORIGIN_RESOURCE_SHARING = 2098688
    HTML5_STORAGE_MANIPULATION_DOM_BASED = 5246720
    HTML5_STORAGE_MANIPULATION_REFLECTED_DOM_BASED = 5246721
    HTML5_STORAGE_MANIPULATION_STORED_DOM_BASED = 5246722
    HTML5_WEB_MESSAGE_MANIPULATION_DOM_BASED = 5246464
    HTML5_WEB_MESSAGE_MANIPULATION_REFLECTED_DOM_BASED = 5246465
    HTML5_WEB_MESSAGE_MANIPULATION_STORED_DOM_BASED = 5246466
    HTTP_PUT_METHOD_IS_ENABLED = 1050880
    HTTP_TRACE_METHOD_IS_ENABLED = 5245440
    HTTP_RESPONSE_HEADER_INJECTION = 2097664
    INPUT_RETURNED_IN_RESPONSE_REFLECTED = 4197376
    INPUT_RETURNED_IN_RESPONSE_STORED = 4197120
    JAVASCRIPT_INJECTION_DOM_BASED = 2097952
    JAVASCRIPT_INJECTION_REFLECTED_DOM_BASED = 2097953
    JAVASCRIPT_INJECTION_STORED_DOM_BASED = 2097954
    LDAP_INJECTION = 1049856
    LINK_MANIPULATION_DOM_BASED = 5246976
    LINK_MANIPULATION_REFLECTED_DOM_BASED = 5246977
    LINK_MANIPULATION_STORED_DOM_BASED = 5246978
    LOCAL_FILE_PATH_MANIPULATION_DOM_BASED = 2098000
    LOCAL_FILE_PATH_MANIPULATION_REFLECTED_DOM_BASED = 2098001
    LOCAL_FILE_PATH_MANIPULATION_STORED_DOM_BASED = 2098002
    LONG_REDIRECTION_RESPONSE = 4196352
    MIXED_CONTENT = 16778240
    MULTIPLE_CONTENT_TYPES_SPECIFIED = 8388864
    OS_COMMAND_INJECTION = 1048832
    OPEN_REDIRECTION = 5243136
    OPEN_REDIRECTION_DOM_BASED = 5243152
    OPEN_REDIRECTION_REFLECTED_DOM_BASED = 5243153
    OPEN_REDIRECTION_STORED_DOM_BASED = 5243154
    OUT_OF_BAND_RESOURCE_LOAD_HTTP = 1051136
    PHP_CODE_INJECTION = 1051648
    PASSWORD_FIELD_WITH_AUTOCOMPLETE_ENABLED = 5244928
    PASSWORD_RETURNED_IN_URL_QUERY_STRING = 4195328
    PASSWORD_RETURNED_IN_LATER_RESPONSE = 4194816
    PASSWORD_SUBMITTED_USING_GET_METHOD = 4195072
    PASSWORD_VALUE_SET_IN_COOKIE = 5245184
    PATH_RELATIVE_STYLE_SHEET_IMPORT = 2097960
    PERL_CODE_INJECTION = 1052160
    PRIVATE_IP_ADDRESSES_DISCLOSED = 6292224
    PRIVATE_KEY_DISCLOSED = 6292816
    PYTHON_CODE_INJECTION = 1052432
    REFERER_DEPENDENT_RESPONSE = 4194560
    ROBOTSTXT_FILE = 6292992
    RUBY_CODE_INJECTION = 1052416
    SQL_INJECTION = 1049088
    SQL_STATEMENT_IN_REQUEST_PARAMETER = 4195456
    SSI_INJECTION = 1052928
    SSL_CERTIFICATE = 16777472
    SSL_COOKIE_WITHOUT_SECURE_FLAG_SET = 5243392
    SERIALIZED_OBJECT_IN_HTTP_MESSAGE = 4196608
    SERVER_SIDE_JAVASCRIPT_CODE_INJECTION = 1051904
    SERVER_SIDE_TEMPLATE_INJECTION = 1052800
    SESSION_TOKEN_IN_URL = 5244672
    SILVERLIGHT_CROSS_DOMAIN_POLICY = 2098432
    SOCIAL_SECURITY_NUMBERS_DISCLOSED = 6292480
    SOURCE_CODE_DISCLOSURE = 6291632
    STRICT_TRANSPORT_SECURITY_NOT_ENFORCED = 16777984
    UNENCRYPTED_COMMUNICATIONS = 16777728
    UNIDENTIFIED_CODE_INJECTION = 1052672
    USER_AGENT_DEPENDENT_RESPONSE = 4194592
    WEBSOCKET_HIJACKING_DOM_BASED = 2097984
    WEBSOCKET_HIJACKING_REFLECTED_DOM_BASED = 2097985
    WEBSOCKET_HIJACKING_STORED_DOM_BASED = 2097986
    X_FORWARDED_FOR_DEPENDENT_RESPONSE = 4194576
    XML_ENTITY_EXPANSION = 4196096
    XML_EXTERNAL_ENTITY_INJECTION = 1049600
    XML_INJECTION = 1050368
    XPATH_INJECTION = 1050112


class Tool(Enum):
    REPEATER = 'repeater'
    INTRUDER = 'intruder'
