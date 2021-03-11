# LDAPSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_mode** | **bool** | Enable this option if the server is configured for Anonymous access. When enabled, ReaderDN and Password will not be used. | [optional] 
**reader_dn** | **str** | Account that will be used to search for users | [optional] 
**password** | **str** | Password of the account that will be used to search users | [optional] 
**url** | **str** | URL or IP address of the LDAP server | [optional] 
**tls_config** | [**TLSConfiguration**](TLSConfiguration.md) |  | [optional] 
**start_tls** | **bool** | Whether LDAP connection should use StartTLS | [optional] 
**search_settings** | [**list[LDAPSearchSettings]**](LDAPSearchSettings.md) |  | [optional] 
**group_search_settings** | [**list[LDAPGroupSearchSettings]**](LDAPGroupSearchSettings.md) |  | [optional] 
**auto_create_users** | **bool** | Automatically provision users and assign them to matching LDAP group names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


