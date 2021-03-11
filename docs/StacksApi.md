# swagger_client.StacksApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stack_create**](StacksApi.md#stack_create) | **POST** /stacks | Deploy a new stack
[**stack_delete**](StacksApi.md#stack_delete) | **DELETE** /stacks/{id} | Remove a stack
[**stack_file_inspect**](StacksApi.md#stack_file_inspect) | **GET** /stacks/{id}/file | Retrieve the content of the Stack file for the specified stack
[**stack_inspect**](StacksApi.md#stack_inspect) | **GET** /stacks/{id} | Inspect a stack
[**stack_list**](StacksApi.md#stack_list) | **GET** /stacks | List stacks
[**stack_migrate**](StacksApi.md#stack_migrate) | **POST** /stacks/{id}/migrate | Migrate a stack to another endpoint
[**stack_update**](StacksApi.md#stack_update) | **PUT** /stacks/{id} | Update a stack


# **stack_create**
> Stack stack_create(type, method, endpoint_id, body=body, name=name, endpoint_id2=endpoint_id2, swarm_id=swarm_id, file=file, env=env)

Deploy a new stack

Deploy a new stack into a Docker environment specified via the endpoint identifier. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
type = 56 # int | Stack deployment type. Possible values: 1 (Swarm stack) or 2 (Compose stack).
method = 'method_example' # str | Stack deployment method. Possible values: file, string or repository.
endpoint_id = 56 # int | Identifier of the endpoint that will be used to deploy the stack.
body = swagger_client.StackCreateRequest() # StackCreateRequest | Stack details. Required when method equals string or repository. (optional)
name = 'name_example' # str | Name of the stack. Required when method equals file. (optional)
endpoint_id2 = 'endpoint_id_example' # str | Endpoint identifier used to deploy the stack. Required when method equals file. (optional)
swarm_id = 'swarm_id_example' # str | Swarm cluster identifier. Required when method equals file and type equals 1. (optional)
file = '/path/to/file.txt' # file | Stack file. Required when method equals file. (optional)
env = 'env_example' # str | Environment variables passed during deployment, represented as a JSON array [{'name': 'name', 'value': 'value'}]. Optional, used when method equals file and type equals 1. (optional)

try:
    # Deploy a new stack
    api_response = api_instance.stack_create(type, method, endpoint_id, body=body, name=name, endpoint_id2=endpoint_id2, swarm_id=swarm_id, file=file, env=env)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| Stack deployment type. Possible values: 1 (Swarm stack) or 2 (Compose stack). | 
 **method** | **str**| Stack deployment method. Possible values: file, string or repository. | 
 **endpoint_id** | **int**| Identifier of the endpoint that will be used to deploy the stack. | 
 **body** | [**StackCreateRequest**](StackCreateRequest.md)| Stack details. Required when method equals string or repository. | [optional] 
 **name** | **str**| Name of the stack. Required when method equals file. | [optional] 
 **endpoint_id2** | **str**| Endpoint identifier used to deploy the stack. Required when method equals file. | [optional] 
 **swarm_id** | **str**| Swarm cluster identifier. Required when method equals file and type equals 1. | [optional] 
 **file** | **file**| Stack file. Required when method equals file. | [optional] 
 **env** | **str**| Environment variables passed during deployment, represented as a JSON array [{&#39;name&#39;: &#39;name&#39;, &#39;value&#39;: &#39;value&#39;}]. Optional, used when method equals file and type equals 1. | [optional] 

### Return type

[**Stack**](Stack.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_delete**
> stack_delete(id, external=external, endpoint_id=endpoint_id)

Remove a stack

Remove a stack. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Stack identifier
external = true # bool | Set to true to delete an external stack. Only external Swarm stacks are supported. (optional)
endpoint_id = 'endpoint_id_example' # str | Endpoint identifier used to remove an external stack (required when external is set to true) (optional)

try:
    # Remove a stack
    api_instance.stack_delete(id, external=external, endpoint_id=endpoint_id)
except ApiException as e:
    print("Exception when calling StacksApi->stack_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **external** | **bool**| Set to true to delete an external stack. Only external Swarm stacks are supported. | [optional] 
 **endpoint_id** | **str**| Endpoint identifier used to remove an external stack (required when external is set to true) | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_file_inspect**
> StackFileInspectResponse stack_file_inspect(id)

Retrieve the content of the Stack file for the specified stack

Get Stack file content. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Retrieve the content of the Stack file for the specified stack
    api_response = api_instance.stack_file_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_file_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**StackFileInspectResponse**](StackFileInspectResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_inspect**
> Stack stack_inspect(id)

Inspect a stack

Retrieve details about a stack. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Stack identifier

try:
    # Inspect a stack
    api_response = api_instance.stack_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**Stack**](Stack.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_list**
> StackListResponse stack_list(filters=filters)

List stacks

List all stacks based on the current user authorizations. Will return all stacks if using an administrator account otherwise it will only return the list of stacks the user have access to. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
filters = 'filters_example' # str | Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {\"SwarmID\": \"jpofkc0i9uo9wtx1zesuk649w\"} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID.  (optional)

try:
    # List stacks
    api_response = api_instance.stack_list(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {\&quot;SwarmID\&quot;: \&quot;jpofkc0i9uo9wtx1zesuk649w\&quot;} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID.  | [optional] 

### Return type

[**StackListResponse**](StackListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_migrate**
> Stack stack_migrate(id, endpoint_id=endpoint_id, body=body)

Migrate a stack to another endpoint

Migrate a stack from an endpoint to another endpoint. It will re-create the stack inside the target endpoint before removing the original stack. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Stack identifier
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated endpoint identifier. Use this optional parameter to set the endpoint identifier used by the stack. (optional)
body = swagger_client.StackMigrateRequest() # StackMigrateRequest | Stack migration details. (optional)

try:
    # Migrate a stack to another endpoint
    api_response = api_instance.stack_migrate(id, endpoint_id=endpoint_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated endpoint identifier. Use this optional parameter to set the endpoint identifier used by the stack. | [optional] 
 **body** | [**StackMigrateRequest**](StackMigrateRequest.md)| Stack migration details. | [optional] 

### Return type

[**Stack**](Stack.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_update**
> Stack stack_update(id, body, endpoint_id=endpoint_id)

Update a stack

Update a stack. **Access policy**: restricted 

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
api_instance = swagger_client.StacksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Stack identifier
body = swagger_client.StackUpdateRequest() # StackUpdateRequest | Stack details
endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated endpoint identifier. Use this optional parameter to set the endpoint identifier used by the stack. (optional)

try:
    # Update a stack
    api_response = api_instance.stack_update(id, body, endpoint_id=endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->stack_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StackUpdateRequest**](StackUpdateRequest.md)| Stack details | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated endpoint identifier. Use this optional parameter to set the endpoint identifier used by the stack. | [optional] 

### Return type

[**Stack**](Stack.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

