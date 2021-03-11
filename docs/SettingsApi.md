# swagger_client.SettingsApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_settings_inspect**](SettingsApi.md#public_settings_inspect) | **GET** /settings/public | Retrieve Portainer public settings
[**settings_inspect**](SettingsApi.md#settings_inspect) | **GET** /settings | Retrieve Portainer settings
[**settings_ldap_check**](SettingsApi.md#settings_ldap_check) | **PUT** /settings/authentication/checkLDAP | Test LDAP connectivity
[**settings_update**](SettingsApi.md#settings_update) | **PUT** /settings | Update Portainer settings


# **public_settings_inspect**
> PublicSettingsInspectResponse public_settings_inspect()

Retrieve Portainer public settings

Retrieve public settings. Returns a small set of settings that are not reserved to administrators only. **Access policy**: public 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve Portainer public settings
    api_response = api_instance.public_settings_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->public_settings_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSettingsInspectResponse**](PublicSettingsInspectResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_inspect**
> Settings settings_inspect()

Retrieve Portainer settings

Retrieve Portainer settings. **Access policy**: administrator 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve Portainer settings
    api_response = api_instance.settings_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_ldap_check**
> settings_ldap_check(body)

Test LDAP connectivity

Test LDAP connectivity using LDAP details. **Access policy**: administrator 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsLDAPCheckRequest() # SettingsLDAPCheckRequest | LDAP settings

try:
    # Test LDAP connectivity
    api_instance.settings_ldap_check(body)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_ldap_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsLDAPCheckRequest**](SettingsLDAPCheckRequest.md)| LDAP settings | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update**
> Settings settings_update(body)

Update Portainer settings

Update Portainer settings. **Access policy**: administrator 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsUpdateRequest() # SettingsUpdateRequest | New settings

try:
    # Update Portainer settings
    api_response = api_instance.settings_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsUpdateRequest**](SettingsUpdateRequest.md)| New settings | 

### Return type

[**Settings**](Settings.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

