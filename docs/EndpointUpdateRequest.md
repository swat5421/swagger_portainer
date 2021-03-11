# EndpointUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name that will be used to identify this endpoint | [optional] 
**url** | **str** | URL or IP address of a Docker host | [optional] 
**public_url** | **str** | URL or IP address where exposed containers will be reachable. Defaults to URL if not specified | [optional] 
**group_id** | **int** | Group identifier | [optional] 
**tls** | **bool** | Require TLS to connect against this endpoint | [optional] 
**tls_skip_verify** | **bool** | Skip server verification when using TLS | [optional] 
**tls_skip_client_verify** | **bool** | Skip client verification when using TLS | [optional] 
**application_id** | **str** | Azure application ID | [optional] 
**tenant_id** | **str** | Azure tenant ID | [optional] 
**authentication_key** | **str** | Azure authentication key | [optional] 
**user_access_policies** | [**UserAccessPolicies**](UserAccessPolicies.md) |  | [optional] 
**team_access_policies** | [**TeamAccessPolicies**](TeamAccessPolicies.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


