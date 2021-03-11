# swagger-client
Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8 You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API endpoints require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example: ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API endpoint has an associated access policy, it is documented in the description of each endpoint.  Different access policies are available: * Public access * Authenticated access * Restricted access * Administrator access  ### Public access  No authentication is required to access the endpoints with this access policy.  ### Authenticated access  Authentication is required to access the endpoints with this access policy.  ### Restricted access  Authentication is required to access the endpoints with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the endpoints with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific endpoints to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API endpoint (which is not documented below due to Swagger limitations). This endpoint has a restricted access policy so you still need to be authenticated to be able to query this endpoint. Any query on this endpoint will be proxied to the Docker API of the associated endpoint (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.24.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthenticateUserRequest() # AuthenticateUserRequest | Credentials used for authentication

try:
    # Authenticate a user
    api_response = api_instance.authenticate_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->authenticate_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://portainer.domain/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**authenticate_user**](docs/AuthApi.md#authenticate_user) | **POST** /auth | Authenticate a user
*DockerhubApi* | [**docker_hub_inspect**](docs/DockerhubApi.md#docker_hub_inspect) | **GET** /dockerhub | Retrieve DockerHub information
*DockerhubApi* | [**docker_hub_update**](docs/DockerhubApi.md#docker_hub_update) | **PUT** /dockerhub | Update DockerHub information
*EndpointGroupsApi* | [**endpoint_group_add_endpoint**](docs/EndpointGroupsApi.md#endpoint_group_add_endpoint) | **PUT** /endpoint_groups/{id}/endpoints/{endpointId} | Add an endpoint to an endpoint group
*EndpointGroupsApi* | [**endpoint_group_create**](docs/EndpointGroupsApi.md#endpoint_group_create) | **POST** /endpoint_groups | Create a new endpoint
*EndpointGroupsApi* | [**endpoint_group_delete**](docs/EndpointGroupsApi.md#endpoint_group_delete) | **DELETE** /endpoint_groups/{id} | Remove an endpoint group
*EndpointGroupsApi* | [**endpoint_group_delete_endpoint**](docs/EndpointGroupsApi.md#endpoint_group_delete_endpoint) | **DELETE** /endpoint_groups/{id}/endpoints/{endpointId} | Remove an endpoint group
*EndpointGroupsApi* | [**endpoint_group_inspect**](docs/EndpointGroupsApi.md#endpoint_group_inspect) | **GET** /endpoint_groups/{id} | Inspect an endpoint group
*EndpointGroupsApi* | [**endpoint_group_list**](docs/EndpointGroupsApi.md#endpoint_group_list) | **GET** /endpoint_groups | List endpoint groups
*EndpointGroupsApi* | [**endpoint_group_update**](docs/EndpointGroupsApi.md#endpoint_group_update) | **PUT** /endpoint_groups/{id} | Update an endpoint group
*EndpointsApi* | [**endpoint_create**](docs/EndpointsApi.md#endpoint_create) | **POST** /endpoints | Create a new endpoint
*EndpointsApi* | [**endpoint_delete**](docs/EndpointsApi.md#endpoint_delete) | **DELETE** /endpoints/{id} | Remove an endpoint
*EndpointsApi* | [**endpoint_inspect**](docs/EndpointsApi.md#endpoint_inspect) | **GET** /endpoints/{id} | Inspect an endpoint
*EndpointsApi* | [**endpoint_job**](docs/EndpointsApi.md#endpoint_job) | **POST** /endpoints/{id}/job | Execute a job on the endpoint host
*EndpointsApi* | [**endpoint_list**](docs/EndpointsApi.md#endpoint_list) | **GET** /endpoints | List endpoints
*EndpointsApi* | [**endpoint_update**](docs/EndpointsApi.md#endpoint_update) | **PUT** /endpoints/{id} | Update an endpoint
*ExtensionsApi* | [**extension_create**](docs/ExtensionsApi.md#extension_create) | **POST** /extensions | Enable an extension
*ExtensionsApi* | [**extension_delete**](docs/ExtensionsApi.md#extension_delete) | **DELETE** /extensions/{id} | Disable an extension
*ExtensionsApi* | [**extension_inspect**](docs/ExtensionsApi.md#extension_inspect) | **GET** /extensions/{id} | Inspect an extension
*ExtensionsApi* | [**extension_list**](docs/ExtensionsApi.md#extension_list) | **GET** /extensions | List extensions
*ExtensionsApi* | [**extension_update**](docs/ExtensionsApi.md#extension_update) | **PUT** /extensions/{id} | Update an extension
*RegistriesApi* | [**registry_create**](docs/RegistriesApi.md#registry_create) | **POST** /registries | Create a new registry
*RegistriesApi* | [**registry_delete**](docs/RegistriesApi.md#registry_delete) | **DELETE** /registries/{id} | Remove a registry
*RegistriesApi* | [**registry_inspect**](docs/RegistriesApi.md#registry_inspect) | **GET** /registries/{id} | Inspect a registry
*RegistriesApi* | [**registry_list**](docs/RegistriesApi.md#registry_list) | **GET** /registries | List registries
*RegistriesApi* | [**registry_update**](docs/RegistriesApi.md#registry_update) | **PUT** /registries/{id} | Update a registry
*ResourceControlsApi* | [**resource_control_create**](docs/ResourceControlsApi.md#resource_control_create) | **POST** /resource_controls | Create a new resource control
*ResourceControlsApi* | [**resource_control_delete**](docs/ResourceControlsApi.md#resource_control_delete) | **DELETE** /resource_controls/{id} | Remove a resource control
*ResourceControlsApi* | [**resource_control_update**](docs/ResourceControlsApi.md#resource_control_update) | **PUT** /resource_controls/{id} | Update a resource control
*RolesApi* | [**role_list**](docs/RolesApi.md#role_list) | **GET** /roles | List roles
*SettingsApi* | [**public_settings_inspect**](docs/SettingsApi.md#public_settings_inspect) | **GET** /settings/public | Retrieve Portainer public settings
*SettingsApi* | [**settings_inspect**](docs/SettingsApi.md#settings_inspect) | **GET** /settings | Retrieve Portainer settings
*SettingsApi* | [**settings_ldap_check**](docs/SettingsApi.md#settings_ldap_check) | **PUT** /settings/authentication/checkLDAP | Test LDAP connectivity
*SettingsApi* | [**settings_update**](docs/SettingsApi.md#settings_update) | **PUT** /settings | Update Portainer settings
*StacksApi* | [**stack_create**](docs/StacksApi.md#stack_create) | **POST** /stacks | Deploy a new stack
*StacksApi* | [**stack_delete**](docs/StacksApi.md#stack_delete) | **DELETE** /stacks/{id} | Remove a stack
*StacksApi* | [**stack_file_inspect**](docs/StacksApi.md#stack_file_inspect) | **GET** /stacks/{id}/file | Retrieve the content of the Stack file for the specified stack
*StacksApi* | [**stack_inspect**](docs/StacksApi.md#stack_inspect) | **GET** /stacks/{id} | Inspect a stack
*StacksApi* | [**stack_list**](docs/StacksApi.md#stack_list) | **GET** /stacks | List stacks
*StacksApi* | [**stack_migrate**](docs/StacksApi.md#stack_migrate) | **POST** /stacks/{id}/migrate | Migrate a stack to another endpoint
*StacksApi* | [**stack_update**](docs/StacksApi.md#stack_update) | **PUT** /stacks/{id} | Update a stack
*StatusApi* | [**status_inspect**](docs/StatusApi.md#status_inspect) | **GET** /status | Check Portainer status
*TagsApi* | [**tag_create**](docs/TagsApi.md#tag_create) | **POST** /tags | Create a new tag
*TagsApi* | [**tag_delete**](docs/TagsApi.md#tag_delete) | **DELETE** /tags/{id} | Remove a tag
*TagsApi* | [**tag_list**](docs/TagsApi.md#tag_list) | **GET** /tags | List tags
*TeamMembershipsApi* | [**team_membership_create**](docs/TeamMembershipsApi.md#team_membership_create) | **POST** /team_memberships | Create a new team membership
*TeamMembershipsApi* | [**team_membership_delete**](docs/TeamMembershipsApi.md#team_membership_delete) | **DELETE** /team_memberships/{id} | Remove a team membership
*TeamMembershipsApi* | [**team_membership_list**](docs/TeamMembershipsApi.md#team_membership_list) | **GET** /team_memberships | List team memberships
*TeamMembershipsApi* | [**team_membership_update**](docs/TeamMembershipsApi.md#team_membership_update) | **PUT** /team_memberships/{id} | Update a team membership
*TeamsApi* | [**team_create**](docs/TeamsApi.md#team_create) | **POST** /teams | Create a new team
*TeamsApi* | [**team_delete**](docs/TeamsApi.md#team_delete) | **DELETE** /teams/{id} | Remove a team
*TeamsApi* | [**team_inspect**](docs/TeamsApi.md#team_inspect) | **GET** /teams/{id} | Inspect a team
*TeamsApi* | [**team_list**](docs/TeamsApi.md#team_list) | **GET** /teams | List teams
*TeamsApi* | [**team_memberships_inspect**](docs/TeamsApi.md#team_memberships_inspect) | **GET** /teams/{id}/memberships | Inspect a team memberships
*TeamsApi* | [**team_update**](docs/TeamsApi.md#team_update) | **PUT** /teams/{id} | Update a team
*TemplatesApi* | [**template_create**](docs/TemplatesApi.md#template_create) | **POST** /templates | Create a new template
*TemplatesApi* | [**template_delete**](docs/TemplatesApi.md#template_delete) | **DELETE** /templates/{id} | Remove a template
*TemplatesApi* | [**template_inspect**](docs/TemplatesApi.md#template_inspect) | **GET** /templates/{id} | Inspect a template
*TemplatesApi* | [**template_list**](docs/TemplatesApi.md#template_list) | **GET** /templates | List available templates
*TemplatesApi* | [**template_update**](docs/TemplatesApi.md#template_update) | **PUT** /templates/{id} | Update a template
*UploadApi* | [**upload_tls**](docs/UploadApi.md#upload_tls) | **POST** /upload/tls/{certificate} | Upload TLS files
*UsersApi* | [**user_admin_check**](docs/UsersApi.md#user_admin_check) | **GET** /users/admin/check | Check administrator account existence
*UsersApi* | [**user_admin_init**](docs/UsersApi.md#user_admin_init) | **POST** /users/admin/init | Initialize administrator account
*UsersApi* | [**user_create**](docs/UsersApi.md#user_create) | **POST** /users | Create a new user
*UsersApi* | [**user_delete**](docs/UsersApi.md#user_delete) | **DELETE** /users/{id} | Remove a user
*UsersApi* | [**user_inspect**](docs/UsersApi.md#user_inspect) | **GET** /users/{id} | Inspect a user
*UsersApi* | [**user_list**](docs/UsersApi.md#user_list) | **GET** /users | List users
*UsersApi* | [**user_memberships_inspect**](docs/UsersApi.md#user_memberships_inspect) | **GET** /users/{id}/memberships | Inspect a user memberships
*UsersApi* | [**user_password_check**](docs/UsersApi.md#user_password_check) | **POST** /users/{id}/passwd | Check password validity for a user
*UsersApi* | [**user_update**](docs/UsersApi.md#user_update) | **PUT** /users/{id} | Update a user


## Documentation For Models

 - [AccessPolicy](docs/AccessPolicy.md)
 - [AuthenticateUserRequest](docs/AuthenticateUserRequest.md)
 - [AuthenticateUserResponse](docs/AuthenticateUserResponse.md)
 - [Authorizations](docs/Authorizations.md)
 - [AzureCredentials](docs/AzureCredentials.md)
 - [DockerHub](docs/DockerHub.md)
 - [DockerHubSubset](docs/DockerHubSubset.md)
 - [DockerHubUpdateRequest](docs/DockerHubUpdateRequest.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointGroup](docs/EndpointGroup.md)
 - [EndpointGroupCreateRequest](docs/EndpointGroupCreateRequest.md)
 - [EndpointGroupListResponse](docs/EndpointGroupListResponse.md)
 - [EndpointGroupUpdateRequest](docs/EndpointGroupUpdateRequest.md)
 - [EndpointJobRequest](docs/EndpointJobRequest.md)
 - [EndpointListResponse](docs/EndpointListResponse.md)
 - [EndpointSubset](docs/EndpointSubset.md)
 - [EndpointUpdateRequest](docs/EndpointUpdateRequest.md)
 - [Extension](docs/Extension.md)
 - [ExtensionCreateRequest](docs/ExtensionCreateRequest.md)
 - [ExtensionListResponse](docs/ExtensionListResponse.md)
 - [ExtensionUpdateRequest](docs/ExtensionUpdateRequest.md)
 - [GenericError](docs/GenericError.md)
 - [LDAPGroupSearchSettings](docs/LDAPGroupSearchSettings.md)
 - [LDAPSearchSettings](docs/LDAPSearchSettings.md)
 - [LDAPSettings](docs/LDAPSettings.md)
 - [LicenseInformation](docs/LicenseInformation.md)
 - [Pair](docs/Pair.md)
 - [PublicSettingsInspectResponse](docs/PublicSettingsInspectResponse.md)
 - [Registry](docs/Registry.md)
 - [RegistryCreateRequest](docs/RegistryCreateRequest.md)
 - [RegistryListResponse](docs/RegistryListResponse.md)
 - [RegistrySubset](docs/RegistrySubset.md)
 - [RegistryUpdateRequest](docs/RegistryUpdateRequest.md)
 - [ResourceControl](docs/ResourceControl.md)
 - [ResourceControlCreateRequest](docs/ResourceControlCreateRequest.md)
 - [ResourceControlUpdateRequest](docs/ResourceControlUpdateRequest.md)
 - [Role](docs/Role.md)
 - [RoleListResponse](docs/RoleListResponse.md)
 - [Settings](docs/Settings.md)
 - [SettingsBlackListedLabels](docs/SettingsBlackListedLabels.md)
 - [SettingsLDAPCheckRequest](docs/SettingsLDAPCheckRequest.md)
 - [SettingsUpdateRequest](docs/SettingsUpdateRequest.md)
 - [Stack](docs/Stack.md)
 - [StackCreateRequest](docs/StackCreateRequest.md)
 - [StackEnv](docs/StackEnv.md)
 - [StackFileInspectResponse](docs/StackFileInspectResponse.md)
 - [StackListResponse](docs/StackListResponse.md)
 - [StackMigrateRequest](docs/StackMigrateRequest.md)
 - [StackUpdateRequest](docs/StackUpdateRequest.md)
 - [Status](docs/Status.md)
 - [TLSConfiguration](docs/TLSConfiguration.md)
 - [Tag](docs/Tag.md)
 - [TagCreateRequest](docs/TagCreateRequest.md)
 - [TagListResponse](docs/TagListResponse.md)
 - [Team](docs/Team.md)
 - [TeamAccessPolicies](docs/TeamAccessPolicies.md)
 - [TeamCreateRequest](docs/TeamCreateRequest.md)
 - [TeamListResponse](docs/TeamListResponse.md)
 - [TeamMembership](docs/TeamMembership.md)
 - [TeamMembershipCreateRequest](docs/TeamMembershipCreateRequest.md)
 - [TeamMembershipListResponse](docs/TeamMembershipListResponse.md)
 - [TeamMembershipUpdateRequest](docs/TeamMembershipUpdateRequest.md)
 - [TeamMembershipsResponse](docs/TeamMembershipsResponse.md)
 - [TeamUpdateRequest](docs/TeamUpdateRequest.md)
 - [Template](docs/Template.md)
 - [TemplateCreateRequest](docs/TemplateCreateRequest.md)
 - [TemplateEnv](docs/TemplateEnv.md)
 - [TemplateEnvSelect](docs/TemplateEnvSelect.md)
 - [TemplateListResponse](docs/TemplateListResponse.md)
 - [TemplateRepository](docs/TemplateRepository.md)
 - [TemplateUpdateRequest](docs/TemplateUpdateRequest.md)
 - [TemplateVolume](docs/TemplateVolume.md)
 - [User](docs/User.md)
 - [UserAccessPolicies](docs/UserAccessPolicies.md)
 - [UserAdminInitRequest](docs/UserAdminInitRequest.md)
 - [UserCreateRequest](docs/UserCreateRequest.md)
 - [UserListResponse](docs/UserListResponse.md)
 - [UserMembershipsResponse](docs/UserMembershipsResponse.md)
 - [UserPasswordCheckRequest](docs/UserPasswordCheckRequest.md)
 - [UserPasswordCheckResponse](docs/UserPasswordCheckResponse.md)
 - [UserSubset](docs/UserSubset.md)
 - [UserUpdateRequest](docs/UserUpdateRequest.md)


## Documentation For Authorization


## jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

info@portainer.io
