# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .application_base_py3 import ApplicationBase


class ApplicationCreateParameters(ApplicationBase):
    """Request parameters for creating a new application.

    All required parameters must be populated in order to send to Azure.

    :param allow_guests_sign_in: A property on the application to indicate if
     the application accepts other IDPs or not or partially accepts.
    :type allow_guests_sign_in: bool
    :param allow_passthrough_users: Indicates that the application supports
     pass through users who have no presence in the resource tenant.
    :type allow_passthrough_users: bool
    :param app_logo_url: The url for the application logo image stored in a
     CDN.
    :type app_logo_url: str
    :param app_roles: The collection of application roles that an application
     may declare. These roles can be assigned to users, groups or service
     principals.
    :type app_roles: list[~azure.graphrbac.models.AppRole]
    :param app_permissions: The application permissions.
    :type app_permissions: list[str]
    :param available_to_other_tenants: Whether the application is available to
     other tenants.
    :type available_to_other_tenants: bool
    :param error_url: A URL provided by the author of the application to
     report errors when using the application.
    :type error_url: str
    :param group_membership_claims: Configures the groups claim issued in a
     user or OAuth 2.0 access token that the app expects.
    :type group_membership_claims: object
    :param homepage: The home page of the application.
    :type homepage: str
    :param informational_urls: URLs with more information about the
     application.
    :type informational_urls: ~azure.graphrbac.models.InformationalUrl
    :param is_device_only_auth_supported: Specifies whether this application
     supports device authentication without a user. The default is false.
    :type is_device_only_auth_supported: bool
    :param key_credentials: A collection of KeyCredential objects.
    :type key_credentials: list[~azure.graphrbac.models.KeyCredential]
    :param known_client_applications: Client applications that are tied to
     this resource application. Consent to any of the known client applications
     will result in implicit consent to the resource application through a
     combined consent dialog (showing the OAuth permission scopes required by
     the client and the resource).
    :type known_client_applications: list[str]
    :param logout_url: the url of the logout page
    :type logout_url: str
    :param oauth2_allow_implicit_flow: Whether to allow implicit grant flow
     for OAuth2
    :type oauth2_allow_implicit_flow: bool
    :param oauth2_allow_url_path_matching: Specifies whether during a token
     Request Azure AD will allow path matching of the redirect URI against the
     applications collection of replyURLs. The default is false.
    :type oauth2_allow_url_path_matching: bool
    :param oauth2_permissions: The collection of OAuth 2.0 permission scopes
     that the web API (resource) application exposes to client applications.
     These permission scopes may be granted to client applications during
     consent.
    :type oauth2_permissions: list[~azure.graphrbac.models.OAuth2Permission]
    :param oauth2_require_post_response: Specifies whether, as part of OAuth
     2.0 token requests, Azure AD will allow POST requests, as opposed to GET
     requests. The default is false, which specifies that only GET requests
     will be allowed.
    :type oauth2_require_post_response: bool
    :param org_restrictions: A list of tenants allowed to access application.
    :type org_restrictions: list[str]
    :param optional_claims:
    :type optional_claims: ~azure.graphrbac.models.OptionalClaims
    :param password_credentials: A collection of PasswordCredential objects
    :type password_credentials:
     list[~azure.graphrbac.models.PasswordCredential]
    :param pre_authorized_applications: list of pre-authorized applications.
    :type pre_authorized_applications:
     list[~azure.graphrbac.models.PreAuthorizedApplication]
    :param public_client: Specifies whether this application is a public
     client (such as an installed application running on a mobile device).
     Default is false.
    :type public_client: bool
    :param publisher_domain: Reliable domain which can be used to identify an
     application.
    :type publisher_domain: str
    :param reply_urls: A collection of reply URLs for the application.
    :type reply_urls: list[str]
    :param required_resource_access: Specifies resources that this application
     requires access to and the set of OAuth permission scopes and application
     roles that it needs under each of those resources. This pre-configuration
     of required resource access drives the consent experience.
    :type required_resource_access:
     list[~azure.graphrbac.models.RequiredResourceAccess]
    :param saml_metadata_url: The URL to the SAML metadata for the
     application.
    :type saml_metadata_url: str
    :param sign_in_audience: Audience for signing in to the application
     (AzureADMyOrganization, AzureADAllOrganizations,
     AzureADAndMicrosoftAccounts).
    :type sign_in_audience: str
    :param www_homepage: The primary Web page.
    :type www_homepage: str
    :param display_name: Required. The display name of the application.
    :type display_name: str
    :param identifier_uris: A collection of URIs for the application.
    :type identifier_uris: list[str]
    """

    _validation = {
        'display_name': {'required': True},
    }

    _attribute_map = {
        'allow_guests_sign_in': {'key': 'allowGuestsSignIn', 'type': 'bool'},
        'allow_passthrough_users': {'key': 'allowPassthroughUsers', 'type': 'bool'},
        'app_logo_url': {'key': 'appLogoUrl', 'type': 'str'},
        'app_roles': {'key': 'appRoles', 'type': '[AppRole]'},
        'app_permissions': {'key': 'appPermissions', 'type': '[str]'},
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'error_url': {'key': 'errorUrl', 'type': 'str'},
        'group_membership_claims': {'key': 'groupMembershipClaims', 'type': 'object'},
        'homepage': {'key': 'homepage', 'type': 'str'},
        'informational_urls': {'key': 'informationalUrls', 'type': 'InformationalUrl'},
        'is_device_only_auth_supported': {'key': 'isDeviceOnlyAuthSupported', 'type': 'bool'},
        'key_credentials': {'key': 'keyCredentials', 'type': '[KeyCredential]'},
        'known_client_applications': {'key': 'knownClientApplications', 'type': '[str]'},
        'logout_url': {'key': 'logoutUrl', 'type': 'str'},
        'oauth2_allow_implicit_flow': {'key': 'oauth2AllowImplicitFlow', 'type': 'bool'},
        'oauth2_allow_url_path_matching': {'key': 'oauth2AllowUrlPathMatching', 'type': 'bool'},
        'oauth2_permissions': {'key': 'oauth2Permissions', 'type': '[OAuth2Permission]'},
        'oauth2_require_post_response': {'key': 'oauth2RequirePostResponse', 'type': 'bool'},
        'org_restrictions': {'key': 'orgRestrictions', 'type': '[str]'},
        'optional_claims': {'key': 'optionalClaims', 'type': 'OptionalClaims'},
        'password_credentials': {'key': 'passwordCredentials', 'type': '[PasswordCredential]'},
        'pre_authorized_applications': {'key': 'preAuthorizedApplications', 'type': '[PreAuthorizedApplication]'},
        'public_client': {'key': 'publicClient', 'type': 'bool'},
        'publisher_domain': {'key': 'publisherDomain', 'type': 'str'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'required_resource_access': {'key': 'requiredResourceAccess', 'type': '[RequiredResourceAccess]'},
        'saml_metadata_url': {'key': 'samlMetadataUrl', 'type': 'str'},
        'sign_in_audience': {'key': 'signInAudience', 'type': 'str'},
        'www_homepage': {'key': 'wwwHomepage', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier_uris': {'key': 'identifierUris', 'type': '[str]'},
    }

    def __init__(self, *, display_name: str, allow_guests_sign_in: bool=None, allow_passthrough_users: bool=None, app_logo_url: str=None, app_roles=None, app_permissions=None, available_to_other_tenants: bool=None, error_url: str=None, group_membership_claims=None, homepage: str=None, informational_urls=None, is_device_only_auth_supported: bool=None, key_credentials=None, known_client_applications=None, logout_url: str=None, oauth2_allow_implicit_flow: bool=None, oauth2_allow_url_path_matching: bool=None, oauth2_permissions=None, oauth2_require_post_response: bool=None, org_restrictions=None, optional_claims=None, password_credentials=None, pre_authorized_applications=None, public_client: bool=None, publisher_domain: str=None, reply_urls=None, required_resource_access=None, saml_metadata_url: str=None, sign_in_audience: str=None, www_homepage: str=None, identifier_uris=None, **kwargs) -> None:
        super(ApplicationCreateParameters, self).__init__(allow_guests_sign_in=allow_guests_sign_in, allow_passthrough_users=allow_passthrough_users, app_logo_url=app_logo_url, app_roles=app_roles, app_permissions=app_permissions, available_to_other_tenants=available_to_other_tenants, error_url=error_url, group_membership_claims=group_membership_claims, homepage=homepage, informational_urls=informational_urls, is_device_only_auth_supported=is_device_only_auth_supported, key_credentials=key_credentials, known_client_applications=known_client_applications, logout_url=logout_url, oauth2_allow_implicit_flow=oauth2_allow_implicit_flow, oauth2_allow_url_path_matching=oauth2_allow_url_path_matching, oauth2_permissions=oauth2_permissions, oauth2_require_post_response=oauth2_require_post_response, org_restrictions=org_restrictions, optional_claims=optional_claims, password_credentials=password_credentials, pre_authorized_applications=pre_authorized_applications, public_client=public_client, publisher_domain=publisher_domain, reply_urls=reply_urls, required_resource_access=required_resource_access, saml_metadata_url=saml_metadata_url, sign_in_audience=sign_in_audience, www_homepage=www_homepage, **kwargs)
        self.display_name = display_name
        self.identifier_uris = identifier_uris
