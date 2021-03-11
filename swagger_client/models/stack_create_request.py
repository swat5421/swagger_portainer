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


class StackCreateRequest(object):
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
        'name': 'str',
        'swarm_id': 'str',
        'stack_file_content': 'str',
        'repository_url': 'str',
        'repository_reference_name': 'str',
        'compose_file_path_in_repository': 'str',
        'repository_authentication': 'bool',
        'repository_username': 'str',
        'repository_password': 'str',
        'env': 'list[StackEnv]'
    }

    attribute_map = {
        'name': 'Name',
        'swarm_id': 'SwarmID',
        'stack_file_content': 'StackFileContent',
        'repository_url': 'RepositoryURL',
        'repository_reference_name': 'RepositoryReferenceName',
        'compose_file_path_in_repository': 'ComposeFilePathInRepository',
        'repository_authentication': 'RepositoryAuthentication',
        'repository_username': 'RepositoryUsername',
        'repository_password': 'RepositoryPassword',
        'env': 'Env'
    }

    def __init__(self, name=None, swarm_id=None, stack_file_content=None, repository_url=None, repository_reference_name=None, compose_file_path_in_repository=None, repository_authentication=None, repository_username=None, repository_password=None, env=None):  # noqa: E501
        """StackCreateRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._swarm_id = None
        self._stack_file_content = None
        self._repository_url = None
        self._repository_reference_name = None
        self._compose_file_path_in_repository = None
        self._repository_authentication = None
        self._repository_username = None
        self._repository_password = None
        self._env = None
        self.discriminator = None

        self.name = name
        if swarm_id is not None:
            self.swarm_id = swarm_id
        if stack_file_content is not None:
            self.stack_file_content = stack_file_content
        if repository_url is not None:
            self.repository_url = repository_url
        if repository_reference_name is not None:
            self.repository_reference_name = repository_reference_name
        if compose_file_path_in_repository is not None:
            self.compose_file_path_in_repository = compose_file_path_in_repository
        if repository_authentication is not None:
            self.repository_authentication = repository_authentication
        if repository_username is not None:
            self.repository_username = repository_username
        if repository_password is not None:
            self.repository_password = repository_password
        if env is not None:
            self.env = env

    @property
    def name(self):
        """Gets the name of this StackCreateRequest.  # noqa: E501

        Name of the stack  # noqa: E501

        :return: The name of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StackCreateRequest.

        Name of the stack  # noqa: E501

        :param name: The name of this StackCreateRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def swarm_id(self):
        """Gets the swarm_id of this StackCreateRequest.  # noqa: E501

        Swarm cluster identifier. Required when creating a Swarm stack (type 1).  # noqa: E501

        :return: The swarm_id of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._swarm_id

    @swarm_id.setter
    def swarm_id(self, swarm_id):
        """Sets the swarm_id of this StackCreateRequest.

        Swarm cluster identifier. Required when creating a Swarm stack (type 1).  # noqa: E501

        :param swarm_id: The swarm_id of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._swarm_id = swarm_id

    @property
    def stack_file_content(self):
        """Gets the stack_file_content of this StackCreateRequest.  # noqa: E501

        Content of the Stack file. Required when using the 'string' deployment method.  # noqa: E501

        :return: The stack_file_content of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._stack_file_content

    @stack_file_content.setter
    def stack_file_content(self, stack_file_content):
        """Sets the stack_file_content of this StackCreateRequest.

        Content of the Stack file. Required when using the 'string' deployment method.  # noqa: E501

        :param stack_file_content: The stack_file_content of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._stack_file_content = stack_file_content

    @property
    def repository_url(self):
        """Gets the repository_url of this StackCreateRequest.  # noqa: E501

        URL of a Git repository hosting the Stack file. Required when using the 'repository' deployment method.  # noqa: E501

        :return: The repository_url of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """Sets the repository_url of this StackCreateRequest.

        URL of a Git repository hosting the Stack file. Required when using the 'repository' deployment method.  # noqa: E501

        :param repository_url: The repository_url of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._repository_url = repository_url

    @property
    def repository_reference_name(self):
        """Gets the repository_reference_name of this StackCreateRequest.  # noqa: E501

        Reference name of a Git repository hosting the Stack file. Used in 'repository' deployment method.  # noqa: E501

        :return: The repository_reference_name of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository_reference_name

    @repository_reference_name.setter
    def repository_reference_name(self, repository_reference_name):
        """Sets the repository_reference_name of this StackCreateRequest.

        Reference name of a Git repository hosting the Stack file. Used in 'repository' deployment method.  # noqa: E501

        :param repository_reference_name: The repository_reference_name of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._repository_reference_name = repository_reference_name

    @property
    def compose_file_path_in_repository(self):
        """Gets the compose_file_path_in_repository of this StackCreateRequest.  # noqa: E501

        Path to the Stack file inside the Git repository. Will default to 'docker-compose.yml' if not specified.  # noqa: E501

        :return: The compose_file_path_in_repository of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._compose_file_path_in_repository

    @compose_file_path_in_repository.setter
    def compose_file_path_in_repository(self, compose_file_path_in_repository):
        """Sets the compose_file_path_in_repository of this StackCreateRequest.

        Path to the Stack file inside the Git repository. Will default to 'docker-compose.yml' if not specified.  # noqa: E501

        :param compose_file_path_in_repository: The compose_file_path_in_repository of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._compose_file_path_in_repository = compose_file_path_in_repository

    @property
    def repository_authentication(self):
        """Gets the repository_authentication of this StackCreateRequest.  # noqa: E501

        Use basic authentication to clone the Git repository.  # noqa: E501

        :return: The repository_authentication of this StackCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._repository_authentication

    @repository_authentication.setter
    def repository_authentication(self, repository_authentication):
        """Sets the repository_authentication of this StackCreateRequest.

        Use basic authentication to clone the Git repository.  # noqa: E501

        :param repository_authentication: The repository_authentication of this StackCreateRequest.  # noqa: E501
        :type: bool
        """

        self._repository_authentication = repository_authentication

    @property
    def repository_username(self):
        """Gets the repository_username of this StackCreateRequest.  # noqa: E501

        Username used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :return: The repository_username of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository_username

    @repository_username.setter
    def repository_username(self, repository_username):
        """Sets the repository_username of this StackCreateRequest.

        Username used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :param repository_username: The repository_username of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._repository_username = repository_username

    @property
    def repository_password(self):
        """Gets the repository_password of this StackCreateRequest.  # noqa: E501

        Password used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :return: The repository_password of this StackCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository_password

    @repository_password.setter
    def repository_password(self, repository_password):
        """Sets the repository_password of this StackCreateRequest.

        Password used in basic authentication. Required when RepositoryAuthentication is true.  # noqa: E501

        :param repository_password: The repository_password of this StackCreateRequest.  # noqa: E501
        :type: str
        """

        self._repository_password = repository_password

    @property
    def env(self):
        """Gets the env of this StackCreateRequest.  # noqa: E501

        A list of environment variables used during stack deployment  # noqa: E501

        :return: The env of this StackCreateRequest.  # noqa: E501
        :rtype: list[StackEnv]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this StackCreateRequest.

        A list of environment variables used during stack deployment  # noqa: E501

        :param env: The env of this StackCreateRequest.  # noqa: E501
        :type: list[StackEnv]
        """

        self._env = env

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
        if issubclass(StackCreateRequest, dict):
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
        if not isinstance(other, StackCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
