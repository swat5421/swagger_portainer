# swagger_client.TemplatesApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_create**](TemplatesApi.md#template_create) | **POST** /templates | Create a new template
[**template_delete**](TemplatesApi.md#template_delete) | **DELETE** /templates/{id} | Remove a template
[**template_inspect**](TemplatesApi.md#template_inspect) | **GET** /templates/{id} | Inspect a template
[**template_list**](TemplatesApi.md#template_list) | **GET** /templates | List available templates
[**template_update**](TemplatesApi.md#template_update) | **PUT** /templates/{id} | Update a template


# **template_create**
> Template template_create(body)

Create a new template

Create a new template. **Access policy**: administrator 

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
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TemplateCreateRequest() # TemplateCreateRequest | Template details

try:
    # Create a new template
    api_response = api_instance.template_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplateCreateRequest**](TemplateCreateRequest.md)| Template details | 

### Return type

[**Template**](Template.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_delete**
> template_delete(id)

Remove a template

Remove a template. **Access policy**: administrator 

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
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Template identifier

try:
    # Remove a template
    api_instance.template_delete(id)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_inspect**
> Template template_inspect(id)

Inspect a template

Retrieve details about a template. **Access policy**: administrator 

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
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Template identifier

try:
    # Inspect a template
    api_response = api_instance.template_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**Template**](Template.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_list**
> TemplateListResponse template_list()

List available templates

List available templates. Administrator templates will not be listed for non-administrator users. **Access policy**: restricted 

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
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))

try:
    # List available templates
    api_response = api_instance.template_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_update**
> template_update(id, body)

Update a template

Update a template. **Access policy**: administrator 

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
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
id = 56 # int | Template identifier
body = swagger_client.TemplateUpdateRequest() # TemplateUpdateRequest | Template details

try:
    # Update a template
    api_instance.template_update(id, body)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 
 **body** | [**TemplateUpdateRequest**](TemplateUpdateRequest.md)| Template details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

