# coding: utf-8

"""
    Portainer API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8 You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API endpoints require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example: ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API endpoint has an associated access policy, it is documented in the description of each endpoint.  Different access policies are available: * Public access * Authenticated access * Restricted access * Administrator access  ### Public access  No authentication is required to access the endpoints with this access policy.  ### Authenticated access  Authentication is required to access the endpoints with this access policy.  ### Restricted access  Authentication is required to access the endpoints with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the endpoints with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific endpoints to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API endpoint (which is not documented below due to Swagger limitations). This endpoint has a restricted access policy so you still need to be authenticated to be able to query this endpoint. Any query on this endpoint will be proxied to the Docker API of the associated endpoint (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8).   # noqa: E501

    OpenAPI spec version: 1.24.1
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AzureCredentials(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'application_id': 'str',
        'tenant_id': 'str',
        'authentication_key': 'str'
    }

    attribute_map = {
        'application_id': 'ApplicationID',
        'tenant_id': 'TenantID',
        'authentication_key': 'AuthenticationKey'
    }

    def __init__(self, application_id=None, tenant_id=None, authentication_key=None):  # noqa: E501
        """AzureCredentials - a model defined in Swagger"""  # noqa: E501

        self._application_id = None
        self._tenant_id = None
        self._authentication_key = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if authentication_key is not None:
            self.authentication_key = authentication_key

    @property
    def application_id(self):
        """Gets the application_id of this AzureCredentials.  # noqa: E501

        Azure application ID  # noqa: E501

        :return: The application_id of this AzureCredentials.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this AzureCredentials.

        Azure application ID  # noqa: E501

        :param application_id: The application_id of this AzureCredentials.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureCredentials.  # noqa: E501

        Azure tenant ID  # noqa: E501

        :return: The tenant_id of this AzureCredentials.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureCredentials.

        Azure tenant ID  # noqa: E501

        :param tenant_id: The tenant_id of this AzureCredentials.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def authentication_key(self):
        """Gets the authentication_key of this AzureCredentials.  # noqa: E501

        Azure authentication key  # noqa: E501

        :return: The authentication_key of this AzureCredentials.  # noqa: E501
        :rtype: str
        """
        return self._authentication_key

    @authentication_key.setter
    def authentication_key(self, authentication_key):
        """Sets the authentication_key of this AzureCredentials.

        Azure authentication key  # noqa: E501

        :param authentication_key: The authentication_key of this AzureCredentials.  # noqa: E501
        :type: str
        """

        self._authentication_key = authentication_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AzureCredentials, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AzureCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other