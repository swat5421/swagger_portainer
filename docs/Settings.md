# Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates_url** | **str** | URL to the templates that will be displayed in the UI when navigating to App Templates | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**black_listed_labels** | [**list[SettingsBlackListedLabels]**](SettingsBlackListedLabels.md) | A list of label name &amp; value that will be used to hide containers when querying containers | [optional] 
**display_external_contributors** | **bool** | Whether to display or not external templates contributions as sub-menus in the UI. | [optional] 
**authentication_method** | **int** | Active authentication method for the Portainer instance. Valid values are: 1 for managed or 2 for LDAP. | [optional] 
**ldap_settings** | [**LDAPSettings**](LDAPSettings.md) |  | [optional] 
**allow_bind_mounts_for_regular_users** | **bool** | Whether non-administrator should be able to use bind mounts when creating containers | [optional] 
**allow_privileged_mode_for_regular_users** | **bool** | Whether non-administrator should be able to use privileged mode when creating containers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


