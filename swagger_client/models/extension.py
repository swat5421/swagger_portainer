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


class Extension(object):
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
        'id': 'int',
        'name': 'str',
        'enabled': 'bool',
        'short_description': 'str',
        'description_url': 'str',
        'available': 'bool',
        'images': 'list[str]',
        'logo': 'str',
        'price': 'str',
        'price_description': 'str',
        'shop_url': 'str',
        'update_available': 'bool',
        'version': 'str',
        'license': 'LicenseInformation'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'enabled': 'Enabled',
        'short_description': 'ShortDescription',
        'description_url': 'DescriptionURL',
        'available': 'Available',
        'images': 'Images',
        'logo': 'Logo',
        'price': 'Price',
        'price_description': 'PriceDescription',
        'shop_url': 'ShopURL',
        'update_available': 'UpdateAvailable',
        'version': 'Version',
        'license': 'License'
    }

    def __init__(self, id=None, name=None, enabled=None, short_description=None, description_url=None, available=None, images=None, logo=None, price=None, price_description=None, shop_url=None, update_available=None, version=None, license=None):  # noqa: E501
        """Extension - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._enabled = None
        self._short_description = None
        self._description_url = None
        self._available = None
        self._images = None
        self._logo = None
        self._price = None
        self._price_description = None
        self._shop_url = None
        self._update_available = None
        self._version = None
        self._license = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if short_description is not None:
            self.short_description = short_description
        if description_url is not None:
            self.description_url = description_url
        if available is not None:
            self.available = available
        if images is not None:
            self.images = images
        if logo is not None:
            self.logo = logo
        if price is not None:
            self.price = price
        if price_description is not None:
            self.price_description = price_description
        if shop_url is not None:
            self.shop_url = shop_url
        if update_available is not None:
            self.update_available = update_available
        if version is not None:
            self.version = version
        if license is not None:
            self.license = license

    @property
    def id(self):
        """Gets the id of this Extension.  # noqa: E501

        Extension identifier  # noqa: E501

        :return: The id of this Extension.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Extension.

        Extension identifier  # noqa: E501

        :param id: The id of this Extension.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Extension.  # noqa: E501

        Extension name  # noqa: E501

        :return: The name of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Extension.

        Extension name  # noqa: E501

        :param name: The name of this Extension.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this Extension.  # noqa: E501

        Is the extension enabled  # noqa: E501

        :return: The enabled of this Extension.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Extension.

        Is the extension enabled  # noqa: E501

        :param enabled: The enabled of this Extension.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def short_description(self):
        """Gets the short_description of this Extension.  # noqa: E501

        Short description about the extension  # noqa: E501

        :return: The short_description of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Extension.

        Short description about the extension  # noqa: E501

        :param short_description: The short_description of this Extension.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def description_url(self):
        """Gets the description_url of this Extension.  # noqa: E501

        URL to the file containing the extension description  # noqa: E501

        :return: The description_url of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._description_url

    @description_url.setter
    def description_url(self, description_url):
        """Sets the description_url of this Extension.

        URL to the file containing the extension description  # noqa: E501

        :param description_url: The description_url of this Extension.  # noqa: E501
        :type: str
        """

        self._description_url = description_url

    @property
    def available(self):
        """Gets the available of this Extension.  # noqa: E501

        Is the extension available for download and activation  # noqa: E501

        :return: The available of this Extension.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this Extension.

        Is the extension available for download and activation  # noqa: E501

        :param available: The available of this Extension.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def images(self):
        """Gets the images of this Extension.  # noqa: E501

        List of screenshot URLs  # noqa: E501

        :return: The images of this Extension.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Extension.

        List of screenshot URLs  # noqa: E501

        :param images: The images of this Extension.  # noqa: E501
        :type: list[str]
        """

        self._images = images

    @property
    def logo(self):
        """Gets the logo of this Extension.  # noqa: E501

        Icon associated to the extension  # noqa: E501

        :return: The logo of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Extension.

        Icon associated to the extension  # noqa: E501

        :param logo: The logo of this Extension.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def price(self):
        """Gets the price of this Extension.  # noqa: E501

        Extension price  # noqa: E501

        :return: The price of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Extension.

        Extension price  # noqa: E501

        :param price: The price of this Extension.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def price_description(self):
        """Gets the price_description of this Extension.  # noqa: E501

        Details about extension pricing  # noqa: E501

        :return: The price_description of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._price_description

    @price_description.setter
    def price_description(self, price_description):
        """Sets the price_description of this Extension.

        Details about extension pricing  # noqa: E501

        :param price_description: The price_description of this Extension.  # noqa: E501
        :type: str
        """

        self._price_description = price_description

    @property
    def shop_url(self):
        """Gets the shop_url of this Extension.  # noqa: E501

        URL used to buy the extension  # noqa: E501

        :return: The shop_url of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._shop_url

    @shop_url.setter
    def shop_url(self, shop_url):
        """Sets the shop_url of this Extension.

        URL used to buy the extension  # noqa: E501

        :param shop_url: The shop_url of this Extension.  # noqa: E501
        :type: str
        """

        self._shop_url = shop_url

    @property
    def update_available(self):
        """Gets the update_available of this Extension.  # noqa: E501

        Is an update available for this extension  # noqa: E501

        :return: The update_available of this Extension.  # noqa: E501
        :rtype: bool
        """
        return self._update_available

    @update_available.setter
    def update_available(self, update_available):
        """Sets the update_available of this Extension.

        Is an update available for this extension  # noqa: E501

        :param update_available: The update_available of this Extension.  # noqa: E501
        :type: bool
        """

        self._update_available = update_available

    @property
    def version(self):
        """Gets the version of this Extension.  # noqa: E501

        Extension version  # noqa: E501

        :return: The version of this Extension.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Extension.

        Extension version  # noqa: E501

        :param version: The version of this Extension.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def license(self):
        """Gets the license of this Extension.  # noqa: E501


        :return: The license of this Extension.  # noqa: E501
        :rtype: LicenseInformation
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Extension.


        :param license: The license of this Extension.  # noqa: E501
        :type: LicenseInformation
        """

        self._license = license

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
        if issubclass(Extension, dict):
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
        if not isinstance(other, Extension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
