# swagger_client.EndpointGroupsApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_group_add_endpoint**](EndpointGroupsApi.md#endpoint_group_add_endpoint) | **PUT** /endpoint_groups/{id}/endpoints/{endpointId} | Add an endpoint to an endpoint group
[**endpoint_group_create**](EndpointGroupsApi.md#endpoint_group_create) | **POST** /endpoint_groups | Create a new endpoint
[**endpoint_group_delete**](EndpointGroupsApi.md#endpoint_group_delete) | **DELETE** /endpoint_groups/{id} | Remove an endpoint group
[**endpoint_group_delete_endpoint**](EndpointGroupsApi.md#endpoint_group_delete_endpoint) | **DELETE** /endpoint_groups/{id}/endpoints/{endpointId} | Remove an endpoint group
[**endpoint_group_inspect**](EndpointGroupsApi.md#endpoint_group_inspect) | **GET** /endpoint_groups/{id} | Inspect an endpoint group
[**endpoint_group_list**](EndpointGroupsApi.md#endpoint_group_list) | **GET** /endpoint_groups | List endpoint groups
[**endpoint_group_update**](EndpointGroupsApi.md#endpoint_group_update) | **PUT** /endpoint_groups/{id} | Update an endpoint group


# **endpoint_group_add_endpoint**
> endpoint_group_add_endpoint(id, endpoint_id)

Add an endpoint to an endpoint group

Add an endpoint to an endpoint group **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
endpoint_id = 56 # int | Endpoint identifier

try:
    # Add an endpoint to an endpoint group
    api_instance.endpoint_group_add_endpoint(id, endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_add_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Endpoint identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_create**
> EndpointGroup endpoint_group_create(body)

Create a new endpoint

Create a new endpoint group. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.EndpointGroupCreateRequest() # EndpointGroupCreateRequest | Registry details

try:
    # Create a new endpoint
    api_response = api_instance.endpoint_group_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointGroupCreateRequest**](EndpointGroupCreateRequest.md)| Registry details | 

### Return type

[**EndpointGroup**](EndpointGroup.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete**
> endpoint_group_delete(id)

Remove an endpoint group

Remove an endpoint group. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier

try:
    # Remove an endpoint group
    api_instance.endpoint_group_delete(id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete_endpoint**
> endpoint_group_delete_endpoint(id, endpoint_id)

Remove an endpoint group

Remove an endpoint group. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
endpoint_id = 56 # int | Endpoint identifier

try:
    # Remove an endpoint group
    api_instance.endpoint_group_delete_endpoint(id, endpoint_id)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_delete_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Endpoint identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_inspect**
> EndpointGroup endpoint_group_inspect(id)

Inspect an endpoint group

Retrieve details abount an endpoint group. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Endpoint group identifier

try:
    # Inspect an endpoint group
    api_response = api_instance.endpoint_group_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Endpoint group identifier | 

### Return type

[**EndpointGroup**](EndpointGroup.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_list**
> EndpointGroupListResponse endpoint_group_list()

List endpoint groups

List all endpoint groups based on the current user authorizations. Will return all endpoint groups if using an administrator account otherwise it will only return authorized endpoint groups. **Access policy**: restricted 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))

try:
    # List endpoint groups
    api_response = api_instance.endpoint_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EndpointGroupListResponse**](EndpointGroupListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_update**
> EndpointGroup endpoint_group_update(id, body)

Update an endpoint group

Update an endpoint group. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | EndpointGroup identifier
body = swagger_client.EndpointGroupUpdateRequest() # EndpointGroupUpdateRequest | EndpointGroup details

try:
    # Update an endpoint group
    api_response = api_instance.endpoint_group_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointGroupsApi->endpoint_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **body** | [**EndpointGroupUpdateRequest**](EndpointGroupUpdateRequest.md)| EndpointGroup details | 

### Return type

[**EndpointGroup**](EndpointGroup.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

