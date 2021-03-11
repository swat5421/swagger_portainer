# RegistryCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name that will be used to identify this registry | 
**type** | **int** | Registry Type. Valid values are: 1 (Quay.io), 2 (Azure container registry) or 3 (custom registry) | 
**url** | **str** | URL or IP address of the Docker registry | 
**authentication** | **bool** | Is authentication against this registry enabled | 
**username** | **str** | Username used to authenticate against this registry | 
**password** | **str** | Password used to authenticate against this registry | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


