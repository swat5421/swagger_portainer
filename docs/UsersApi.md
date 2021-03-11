# swagger_client.UsersApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_admin_check**](UsersApi.md#user_admin_check) | **GET** /users/admin/check | Check administrator account existence
[**user_admin_init**](UsersApi.md#user_admin_init) | **POST** /users/admin/init | Initialize administrator account
[**user_create**](UsersApi.md#user_create) | **POST** /users | Create a new user
[**user_delete**](UsersApi.md#user_delete) | **DELETE** /users/{id} | Remove a user
[**user_inspect**](UsersApi.md#user_inspect) | **GET** /users/{id} | Inspect a user
[**user_list**](UsersApi.md#user_list) | **GET** /users | List users
[**user_memberships_inspect**](UsersApi.md#user_memberships_inspect) | **GET** /users/{id}/memberships | Inspect a user memberships
[**user_password_check**](UsersApi.md#user_password_check) | **POST** /users/{id}/passwd | Check password validity for a user
[**user_update**](UsersApi.md#user_update) | **PUT** /users/{id} | Update a user


# **user_admin_check**
> user_admin_check()

Check administrator account existence

Check if an administrator account exists in the database. **Access policy**: public 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Check administrator account existence
    api_instance.user_admin_check()
except ApiException as e:
    print("Exception when calling UsersApi->user_admin_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_init**
> User user_admin_init(body)

Initialize administrator account

Initialize the 'admin' user account. **Access policy**: public 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAdminInitRequest() # UserAdminInitRequest | User details

try:
    # Initialize administrator account
    api_response = api_instance.user_admin_init(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_admin_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAdminInitRequest**](UserAdminInitRequest.md)| User details | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> UserSubset user_create(body)

Create a new user

Create a new Portainer user. Only team leaders and administrators can create users. Only administrators can create an administrator user account. **Access policy**: restricted 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreateRequest() # UserCreateRequest | User details

try:
    # Create a new user
    api_response = api_instance.user_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateRequest**](UserCreateRequest.md)| User details | 

### Return type

[**UserSubset**](UserSubset.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(id)

Remove a user

Remove a user. **Access policy**: administrator 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Remove a user
    api_instance.user_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_inspect**
> User user_inspect(id)

Inspect a user

Retrieve details about a user. **Access policy**: administrator 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Inspect a user
    api_response = api_instance.user_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list**
> UserListResponse user_list()

List users

List Portainer users. Non-administrator users will only be able to list other non-administrator user accounts. **Access policy**: restricted 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # List users
    api_response = api_instance.user_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserListResponse**](UserListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_memberships_inspect**
> UserMembershipsResponse user_memberships_inspect(id)

Inspect a user memberships

Inspect a user memberships. **Access policy**: authenticated 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | User identifier

try:
    # Inspect a user memberships
    api_response = api_instance.user_memberships_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_memberships_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**UserMembershipsResponse**](UserMembershipsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_password_check**
> UserPasswordCheckResponse user_password_check(id, body)

Check password validity for a user

Check if the submitted password is valid for the specified user. **Access policy**: authenticated 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | User identifier
body = swagger_client.UserPasswordCheckRequest() # UserPasswordCheckRequest | User details

try:
    # Check password validity for a user
    api_response = api_instance.user_password_check(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_password_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **body** | [**UserPasswordCheckRequest**](UserPasswordCheckRequest.md)| User details | 

### Return type

[**UserPasswordCheckResponse**](UserPasswordCheckResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> User user_update(id, body)

Update a user

Update user details. A regular user account can only update his details. **Access policy**: authenticated 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
id = 56 # int | User identifier
body = swagger_client.UserUpdateRequest() # UserUpdateRequest | User details

try:
    # Update a user
    api_response = api_instance.user_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **body** | [**UserUpdateRequest**](UserUpdateRequest.md)| User details | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

