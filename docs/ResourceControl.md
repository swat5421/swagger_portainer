# ResourceControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Docker resource identifier on which access control will be applied. In the case of a resource control applied to a stack, use the stack name as identifier | [optional] 
**type** | **str** | Type of Docker resource. Valid values are: container, volume service, secret, config or stack | [optional] 
**public** | **bool** | Permit access to the associated resource to any user | [optional] 
**users** | **list[int]** | List of user identifiers with access to the associated resource | [optional] 
**teams** | **list[int]** | List of team identifiers with access to the associated resource | [optional] 
**sub_resource_i_ds** | **list[str]** | List of Docker resources that will inherit this access control | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


