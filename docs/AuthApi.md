# swagger_client.AuthApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](AuthApi.md#authenticate_user) | **POST** /auth | Authenticate a user


# **authenticate_user**
> AuthenticateUserResponse authenticate_user(body)

Authenticate a user

Use this endpoint to authenticate against Portainer using a username and password. **Access policy**: public 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.AuthenticateUserRequest() # AuthenticateUserRequest | Credentials used for authentication

try:
    # Authenticate a user
    api_response = api_instance.authenticate_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authenticate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticateUserRequest**](AuthenticateUserRequest.md)| Credentials used for authentication | 

### Return type

[**AuthenticateUserResponse**](AuthenticateUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

