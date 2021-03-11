# Stack

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stack identifier | [optional] 
**name** | **str** | Stack name | [optional] 
**type** | **int** | Stack type. 1 for a Swarm stack, 2 for a Compose stack | [optional] 
**endpoint_id** | **int** | Endpoint identifier. Reference the endpoint that will be used for deployment  | [optional] 
**entry_point** | **str** | Path to the Stack file | [optional] 
**swarm_id** | **str** | Cluster identifier of the Swarm cluster where the stack is deployed | [optional] 
**project_path** | **str** | Path on disk to the repository hosting the Stack file | [optional] 
**env** | [**list[StackEnv]**](StackEnv.md) | A list of environment variables used during stack deployment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


