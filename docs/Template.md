# Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template identifier | [optional] 
**type** | **int** | Template type. Valid values are: 1 (container), 2 (Swarm stack) or 3 (Compose stack) | [optional] 
**title** | **str** | Title of the template | [optional] 
**description** | **str** | Description of the template | [optional] 
**administrator_only** | **bool** | Whether the template should be available to administrators only | [optional] 
**image** | **str** | Image associated to a container template. Mandatory for a container template | [optional] 
**repository** | [**TemplateRepository**](TemplateRepository.md) |  | [optional] 
**name** | **str** | Default name for the stack/container to be used on deployment | [optional] 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**env** | [**list[TemplateEnv]**](TemplateEnv.md) | A list of environment variables used during the template deployment | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | **str** | Platform associated to the template. Valid values are: &#39;linux&#39;, &#39;windows&#39; or leave empty for multi-platform | [optional] 
**categories** | **list[str]** | A list of categories associated to the template | [optional] 
**registry** | **str** | The URL of a registry associated to the image for a container template | [optional] 
**command** | **str** | The command that will be executed in a container template | [optional] 
**network** | **str** | Name of a network that will be used on container deployment if it exists inside the environment | [optional] 
**volumes** | [**list[TemplateVolume]**](TemplateVolume.md) | A list of volumes used during the container template deployment | [optional] 
**ports** | **list[str]** | A list of ports exposed by the container | [optional] 
**labels** | [**list[Pair]**](Pair.md) | Container labels | [optional] 
**privileged** | **bool** | Whether the container should be started in privileged mode | [optional] 
**interactive** | **bool** | Whether the container should be started in interactive mode (-i -t equivalent on the CLI) | [optional] 
**restart_policy** | **str** | Container restart policy | [optional] 
**hostname** | **str** | Container hostname | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


