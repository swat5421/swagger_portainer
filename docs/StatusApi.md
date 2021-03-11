# swagger_client.StatusApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_inspect**](StatusApi.md#status_inspect) | **GET** /status | Check Portainer status


# **status_inspect**
> Status status_inspect()

Check Portainer status

Retrieve Portainer status. **Access policy**: public 

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
api_instance = swagger_client.StatusApi(swagger_client.ApiClient(configuration))

try:
    # Check Portainer status
    api_response = api_instance.status_inspect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_inspect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

