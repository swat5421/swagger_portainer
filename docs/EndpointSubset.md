# EndpointSubset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Endpoint identifier | [optional] 
**name** | **str** | Endpoint name | [optional] 
**type** | **int** | Endpoint environment type. 1 for a Docker environment, 2 for an agent on Docker environment, 3 for an Azure environment. | [optional] 
**url** | **str** | URL or IP address of the Docker host associated to this endpoint | [optional] 
**public_url** | **str** | URL or IP address where exposed containers will be reachable | [optional] 
**group_id** | **int** | Endpoint group identifier | [optional] 
**authorized_users** | **list[int]** | List of user identifiers authorized to connect to this endpoint | [optional] 
**authorized_teams** | **list[int]** | List of team identifiers authorized to connect to this endpoint | [optional] 
**tls_config** | [**TLSConfiguration**](TLSConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


