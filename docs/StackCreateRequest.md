# StackCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the stack | 
**swarm_id** | **str** | Swarm cluster identifier. Required when creating a Swarm stack (type 1). | [optional] 
**stack_file_content** | **str** | Content of the Stack file. Required when using the &#39;string&#39; deployment method. | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file. Required when using the &#39;repository&#39; deployment method. | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file. Used in &#39;repository&#39; deployment method. | [optional] 
**compose_file_path_in_repository** | **str** | Path to the Stack file inside the Git repository. Will default to &#39;docker-compose.yml&#39; if not specified. | [optional] 
**repository_authentication** | **bool** | Use basic authentication to clone the Git repository. | [optional] 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**repository_password** | **str** | Password used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**env** | [**list[StackEnv]**](StackEnv.md) | A list of environment variables used during stack deployment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


