# swagger_client.RegistriesApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registry_create**](RegistriesApi.md#registry_create) | **POST** /registries | Create a new registry
[**registry_delete**](RegistriesApi.md#registry_delete) | **DELETE** /registries/{id} | Remove a registry
[**registry_inspect**](RegistriesApi.md#registry_inspect) | **GET** /registries/{id} | Inspect a registry
[**registry_list**](RegistriesApi.md#registry_list) | **GET** /registries | List registries
[**registry_update**](RegistriesApi.md#registry_update) | **PUT** /registries/{id} | Update a registry


# **registry_create**
> Registry registry_create(body)

Create a new registry

Create a new registry. **Access policy**: administrator 

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
api_instance = swagger_client.RegistriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegistryCreateRequest() # RegistryCreateRequest | Registry details

try:
    # Create a new registry
    api_response = api_instance.registry_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryCreateRequest**](RegistryCreateRequest.md)| Registry details | 

### Return type

[**Registry**](Registry.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_delete**
> registry_delete(id)

Remove a registry

Remove a registry. **Access policy**: administrator 

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
api_instance = swagger_client.RegistriesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Registry identifier

try:
    # Remove a registry
    api_instance.registry_delete(id)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_inspect**
> Registry registry_inspect(id)

Inspect a registry

Retrieve details about a registry. **Access policy**: administrator 

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
api_instance = swagger_client.RegistriesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Registry identifier

try:
    # Inspect a registry
    api_response = api_instance.registry_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 

### Return type

[**Registry**](Registry.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_list**
> RegistryListResponse registry_list()

List registries

List all registries based on the current user authorizations. Will return all registries if using an administrator account otherwise it will only return authorized registries. **Access policy**: restricted 

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
api_instance = swagger_client.RegistriesApi(swagger_client.ApiClient(configuration))

try:
    # List registries
    api_response = api_instance.registry_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistryListResponse**](RegistryListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_update**
> Registry registry_update(id, body)

Update a registry

Update a registry. **Access policy**: administrator 

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
api_instance = swagger_client.RegistriesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Registry identifier
body = swagger_client.RegistryUpdateRequest() # RegistryUpdateRequest | Registry details

try:
    # Update a registry
    api_response = api_instance.registry_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->registry_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Registry identifier | 
 **body** | [**RegistryUpdateRequest**](RegistryUpdateRequest.md)| Registry details | 

### Return type

[**Registry**](Registry.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

