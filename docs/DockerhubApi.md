# swagger_client.DockerhubApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docker_hub_inspect**](DockerhubApi.md#docker_hub_inspect) | **GET** /dockerhub | Retrieve DockerHub information
[**docker_hub_update**](DockerhubApi.md#docker_hub_update) | **PUT** /dockerhub | Update DockerHub information


# **docker_hub_inspect**
> DockerHubSubset docker_hub_inspect()

Retrieve DockerHub information

Use this endpoint to retrieve the information used to connect to the DockerHub **Access policy**: authenticated 

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
api_instance = swagger_client.DockerhubApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve DockerHub information
    api_response = api_instance.docker_hub_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockerhubApi->docker_hub_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DockerHubSubset**](DockerHubSubset.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_hub_update**
> DockerHub docker_hub_update(body)

Update DockerHub information

Use this endpoint to update the information used to connect to the DockerHub **Access policy**: administrator 

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
api_instance = swagger_client.DockerhubApi(swagger_client.ApiClient(configuration))
body = swagger_client.DockerHubUpdateRequest() # DockerHubUpdateRequest | DockerHub information

try:
    # Update DockerHub information
    api_response = api_instance.docker_hub_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DockerhubApi->docker_hub_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerHubUpdateRequest**](DockerHubUpdateRequest.md)| DockerHub information | 

### Return type

[**DockerHub**](DockerHub.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

