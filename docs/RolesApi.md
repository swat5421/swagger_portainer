# swagger_client.RolesApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_list**](RolesApi.md#role_list) | **GET** /roles | List roles


# **role_list**
> RoleListResponse role_list()

List roles

List all roles available for use with the RBAC extension. **Access policy**: administrator 

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))

try:
    # List roles
    api_response = api_instance.role_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleListResponse**](RoleListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

