# EndpointGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Endpoint group identifier | [optional] 
**name** | **str** | Endpoint group name | [optional] 
**description** | **str** | Endpoint group description | [optional] 
**authorized_users** | **list[int]** | List of user identifiers authorized to connect to this endpoint group. Will be inherited by endpoints that are part of the group | [optional] 
**authorized_teams** | **list[int]** | List of team identifiers authorized to connect to this endpoint. Will be inherited by endpoints that are part of the group | [optional] 
**labels** | [**list[Pair]**](Pair.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


