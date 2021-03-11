# swagger_client.EndpointsApi

All URIs are relative to *http://portainer.domain/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_create**](EndpointsApi.md#endpoint_create) | **POST** /endpoints | Create a new endpoint
[**endpoint_delete**](EndpointsApi.md#endpoint_delete) | **DELETE** /endpoints/{id} | Remove an endpoint
[**endpoint_inspect**](EndpointsApi.md#endpoint_inspect) | **GET** /endpoints/{id} | Inspect an endpoint
[**endpoint_job**](EndpointsApi.md#endpoint_job) | **POST** /endpoints/{id}/job | Execute a job on the endpoint host
[**endpoint_list**](EndpointsApi.md#endpoint_list) | **GET** /endpoints | List endpoints
[**endpoint_update**](EndpointsApi.md#endpoint_update) | **PUT** /endpoints/{id} | Update an endpoint


# **endpoint_create**
> Endpoint endpoint_create(name, endpoint_type, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key)

Create a new endpoint

Create a new endpoint that will be used to manage a Docker environment. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name that will be used to identify this endpoint (example: my-endpoint)
endpoint_type = 56 # int | Environment type. Value must be one of: 1 (Docker environment), 2 (Agent environment), 3 (Azure environment) or 4 (Edge agent environment)
url = 'url_example' # str | URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine) (optional)
public_url = 'public_url_example' # str | URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) (optional)
group_id = 'group_id_example' # str | Endpoint group identifier. If not specified will default to 1 (unassigned). (optional)
tls = 'tls_example' # str | Require TLS to connect against this endpoint (example: true) (optional)
tls_skip_verify = 'tls_skip_verify_example' # str | Skip server verification when using TLS (example: false) (optional)
tls_skip_client_verify = 'tls_skip_client_verify_example' # str | Skip client verification when using TLS (example: false) (optional)
tlsca_cert_file = '/path/to/file.txt' # file | TLS CA certificate file (optional)
tls_cert_file = '/path/to/file.txt' # file | TLS client certificate file (optional)
tls_key_file = '/path/to/file.txt' # file | TLS client key file (optional)
azure_application_id = 'azure_application_id_example' # str | Azure application ID. Required if endpoint type is set to 3 (optional)
azure_tenant_id = 'azure_tenant_id_example' # str | Azure tenant ID. Required if endpoint type is set to 3 (optional)
azure_authentication_key = 'azure_authentication_key_example' # str | Azure authentication key. Required if endpoint type is set to 3 (optional)

try:
    # Create a new endpoint
    api_response = api_instance.endpoint_create(name, endpoint_type, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name that will be used to identify this endpoint (example: my-endpoint) | 
 **endpoint_type** | **int**| Environment type. Value must be one of: 1 (Docker environment), 2 (Agent environment), 3 (Azure environment) or 4 (Edge agent environment) | 
 **url** | **str**| URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine) | [optional] 
 **public_url** | **str**| URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) | [optional] 
 **group_id** | **str**| Endpoint group identifier. If not specified will default to 1 (unassigned). | [optional] 
 **tls** | **str**| Require TLS to connect against this endpoint (example: true) | [optional] 
 **tls_skip_verify** | **str**| Skip server verification when using TLS (example: false) | [optional] 
 **tls_skip_client_verify** | **str**| Skip client verification when using TLS (example: false) | [optional] 
 **tlsca_cert_file** | **file**| TLS CA certificate file | [optional] 
 **tls_cert_file** | **file**| TLS client certificate file | [optional] 
 **tls_key_file** | **file**| TLS client key file | [optional] 
 **azure_application_id** | **str**| Azure application ID. Required if endpoint type is set to 3 | [optional] 
 **azure_tenant_id** | **str**| Azure tenant ID. Required if endpoint type is set to 3 | [optional] 
 **azure_authentication_key** | **str**| Azure authentication key. Required if endpoint type is set to 3 | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_delete**
> endpoint_delete(id)

Remove an endpoint

Remove an endpoint. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Endpoint identifier

try:
    # Remove an endpoint
    api_instance.endpoint_delete(id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Endpoint identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_inspect**
> Endpoint endpoint_inspect(id)

Inspect an endpoint

Retrieve details abount an endpoint. **Access policy**: restricted 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Endpoint identifier

try:
    # Inspect an endpoint
    api_response = api_instance.endpoint_inspect(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Endpoint identifier | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_job**
> Endpoint endpoint_job(id, method, node_name, body, image=image, file=file)

Execute a job on the endpoint host

Execute a job (script) on the underlying host of the endpoint. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Endpoint identifier
method = 'method_example' # str | Job execution method. Possible values: file or string.
node_name = 'node_name_example' # str | Optional. Hostname of a node when targeting a Portainer agent cluster.
body = swagger_client.EndpointJobRequest() # EndpointJobRequest | Job details. Required when method equals string.
image = 'image_example' # str | Container image which will be used to execute the job. Required when method equals file. (optional)
file = '/path/to/file.txt' # file | Job script file. Required when method equals file. (optional)

try:
    # Execute a job on the endpoint host
    api_response = api_instance.endpoint_job(id, method, node_name, body, image=image, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Endpoint identifier | 
 **method** | **str**| Job execution method. Possible values: file or string. | 
 **node_name** | **str**| Optional. Hostname of a node when targeting a Portainer agent cluster. | 
 **body** | [**EndpointJobRequest**](EndpointJobRequest.md)| Job details. Required when method equals string. | 
 **image** | **str**| Container image which will be used to execute the job. Required when method equals file. | [optional] 
 **file** | **file**| Job script file. Required when method equals file. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_list**
> EndpointListResponse endpoint_list()

List endpoints

List all endpoints based on the current user authorizations. Will return all endpoints if using an administrator account otherwise it will only return authorized endpoints. **Access policy**: restricted 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))

try:
    # List endpoints
    api_response = api_instance.endpoint_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EndpointListResponse**](EndpointListResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_update**
> endpoint_update(id, body)

Update an endpoint

Update an endpoint. **Access policy**: administrator 

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Endpoint identifier
body = swagger_client.EndpointUpdateRequest() # EndpointUpdateRequest | Endpoint details

try:
    # Update an endpoint
    api_instance.endpoint_update(id, body)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoint_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Endpoint identifier | 
 **body** | [**EndpointUpdateRequest**](EndpointUpdateRequest.md)| Endpoint details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

