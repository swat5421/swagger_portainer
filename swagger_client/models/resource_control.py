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


class ResourceControl(object):
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
        'resource_id': 'str',
        'type': 'str',
        'public': 'bool',
        'users': 'list[int]',
        'teams': 'list[int]',
        'sub_resource_i_ds': 'list[str]'
    }

    attribute_map = {
        'resource_id': 'ResourceID',
        'type': 'Type',
        'public': 'Public',
        'users': 'Users',
        'teams': 'Teams',
        'sub_resource_i_ds': 'SubResourceIDs'
    }

    def __init__(self, resource_id=None, type=None, public=None, users=None, teams=None, sub_resource_i_ds=None):  # noqa: E501
        """ResourceControl - a model defined in Swagger"""  # noqa: E501

        self._resource_id = None
        self._type = None
        self._public = None
        self._users = None
        self._teams = None
        self._sub_resource_i_ds = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if type is not None:
            self.type = type
        if public is not None:
            self.public = public
        if users is not None:
            self.users = users
        if teams is not None:
            self.teams = teams
        if sub_resource_i_ds is not None:
            self.sub_resource_i_ds = sub_resource_i_ds

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourceControl.  # noqa: E501

        Docker resource identifier on which access control will be applied. In the case of a resource control applied to a stack, use the stack name as identifier  # noqa: E501

        :return: The resource_id of this ResourceControl.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourceControl.

        Docker resource identifier on which access control will be applied. In the case of a resource control applied to a stack, use the stack name as identifier  # noqa: E501

        :param resource_id: The resource_id of this ResourceControl.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def type(self):
        """Gets the type of this ResourceControl.  # noqa: E501

        Type of Docker resource. Valid values are: container, volume service, secret, config or stack  # noqa: E501

        :return: The type of this ResourceControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceControl.

        Type of Docker resource. Valid values are: container, volume service, secret, config or stack  # noqa: E501

        :param type: The type of this ResourceControl.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def public(self):
        """Gets the public of this ResourceControl.  # noqa: E501

        Permit access to the associated resource to any user  # noqa: E501

        :return: The public of this ResourceControl.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ResourceControl.

        Permit access to the associated resource to any user  # noqa: E501

        :param public: The public of this ResourceControl.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def users(self):
        """Gets the users of this ResourceControl.  # noqa: E501

        List of user identifiers with access to the associated resource  # noqa: E501

        :return: The users of this ResourceControl.  # noqa: E501
        :rtype: list[int]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ResourceControl.

        List of user identifiers with access to the associated resource  # noqa: E501

        :param users: The users of this ResourceControl.  # noqa: E501
        :type: list[int]
        """

        self._users = users

    @property
    def teams(self):
        """Gets the teams of this ResourceControl.  # noqa: E501

        List of team identifiers with access to the associated resource  # noqa: E501

        :return: The teams of this ResourceControl.  # noqa: E501
        :rtype: list[int]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this ResourceControl.

        List of team identifiers with access to the associated resource  # noqa: E501

        :param teams: The teams of this ResourceControl.  # noqa: E501
        :type: list[int]
        """

        self._teams = teams

    @property
    def sub_resource_i_ds(self):
        """Gets the sub_resource_i_ds of this ResourceControl.  # noqa: E501

        List of Docker resources that will inherit this access control  # noqa: E501

        :return: The sub_resource_i_ds of this ResourceControl.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_resource_i_ds

    @sub_resource_i_ds.setter
    def sub_resource_i_ds(self, sub_resource_i_ds):
        """Sets the sub_resource_i_ds of this ResourceControl.

        List of Docker resources that will inherit this access control  # noqa: E501

        :param sub_resource_i_ds: The sub_resource_i_ds of this ResourceControl.  # noqa: E501
        :type: list[str]
        """

        self._sub_resource_i_ds = sub_resource_i_ds

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
        if issubclass(ResourceControl, dict):
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
        if not isinstance(other, ResourceControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
