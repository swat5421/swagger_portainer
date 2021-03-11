# swagger_client.ExtensionsApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extension_create**](ExtensionsApi.md#extension_create) | **POST** /extensions | Enable an extension
[**extension_delete**](ExtensionsApi.md#extension_delete) | **DELETE** /extensions/{id} | Disable an extension
[**extension_inspect**](ExtensionsApi.md#extension_inspect) | **GET** /extensions/{id} | Inspect an extension
[**extension_list**](ExtensionsApi.md#extension_list) | **GET** /extensions | List extensions
[**extension_update**](ExtensionsApi.md#extension_update) | **PUT** /extensions/{id} | Update an extension


# **extension_create**
> extension_create(body)

Enable an extension

Enable an extension. **Access policy**: administrator 

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
api_instance = swagger_client.ExtensionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExtensionCreateRequest() # ExtensionCreateRequest | Extension details

try:
    # Enable an extension
    api_instance.extension_create(body)
except ApiException as e:
    print("Exception when calling ExtensionsApi->extension_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExtensionCreateRequest**](ExtensionCreateRequest.md)| Extension details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_delete**
> extension_delete(id)

Disable an extension

Disable an extension. **Access policy**: administrator 

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
api_instance = swagger_client.ExtensionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Extension identifier

try:
    # Disable an extension
    api_instance.extension_delete(id)
except ApiException as e:
    print("Exception when calling ExtensionsApi->extension_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Extension identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_inspect**
> Extension extension_inspect(id)

Inspect an extension

Retrieve details abount an extension. **Access policy**: administrator 

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
api_instance = swagger_client.ExtensionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | extension identifier

try:
    # Inspect an extension
    api_response = api_instance.extension_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->extension_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| extension identifier | 

### Return type

[**Extension**](Extension.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_list**
> ExtensionListResponse extension_list(store=store)

List extensions

List all extensions registered inside Portainer. If the store parameter is set to true, will retrieve extensions details from the online repository. **Access policy**: administrator 

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
api_instance = swagger_client.ExtensionsApi(swagger_client.ApiClient(configuration))
store = true # bool | Retrieve online information about extensions. Possible values: true or false. (optional)

try:
    # List extensions
    api_response = api_instance.extension_list(store=store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->extension_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store** | **bool**| Retrieve online information about extensions. Possible values: true or false. | [optional] 

### Return type

[**ExtensionListResponse**](ExtensionListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extension_update**
> extension_update(id, body)

Update an extension

Update an extension to a specific version of the extension. **Access policy**: administrator 

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
api_instance = swagger_client.ExtensionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Extension identifier
body = swagger_client.ExtensionUpdateRequest() # ExtensionUpdateRequest | Extension details

try:
    # Update an extension
    api_instance.extension_update(id, body)
except ApiException as e:
    print("Exception when calling ExtensionsApi->extension_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Extension identifier | 
 **body** | [**ExtensionUpdateRequest**](ExtensionUpdateRequest.md)| Extension details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

