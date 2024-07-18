from __future__ import annotations

import os

from flask_appbuilder.const import AUTH_OAUTH

# from airflow.www.fab_security.manager import AUTH_LDAP
# from airflow.www.fab_security.manager import AUTH_OAUTH
# from airflow.www.fab_security.manager import AUTH_OID
# from airflow.www.fab_security.manager import AUTH_REMOTE_USER


basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# For details on how to set up each of the following authentication, see
# http://flask-appbuilder.readthedocs.io/en/latest/security.html# authentication-methods
# for details.

# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
# AUTH_OAUTH : Is for OAuth
AUTH_TYPE = AUTH_OAUTH

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment and set to desired role to enable access without authentication
# AUTH_ROLE_PUBLIC = 'Viewer'

# Will allow user self registration
# AUTH_USER_REGISTRATION = True

# The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Public"


AUTH_TYPE = AUTH_OAUTH

AUTH_ROLES_SYNC_AT_LOGIN = True # Check roles on every login
AUTH_USER_REGISTRATION = True  # Allow users who are not already in the FAB DB
AUTH_USER_REGISTRATION_ROLE = "Public"  # this role will be given in addition to any AUTH_ROLES_MAPPING

AUTH_ROLES_MAPPING = {
    "AZU-AIRFLOW-USERS": ["User"],
    "AZU-AIRFLOW-ADMIN": ["Admin"],
}

# the list of providers which the user can choose from
OAUTH_PROVIDERS = [
    {
        "name": "azure",
        "icon": "fa-windows",
        "token_key": "access_token",
        "remote_app": {
            "client_id": "AZURE_APPLICATION_ID",
            "client_secret": "AZURE_SECRET",
            "api_base_url": "https://login.microsoftonline.com/AZURE_TENANT_ID/oauth2",
            "client_kwargs": {
                "scope": "User.read name preferred_username email profile upn",
                "resource": "AZURE_APPLICATION_ID",
                # Optionally enforce signature JWT verification
                "verify_signature": False
            },
            "request_token_url": None,
            "access_token_url": "https://login.microsoftonline.com/AZURE_TENANT_ID/oauth2/token",
            "authorize_url": "https://login.microsoftonline.com/AZURE_TENANT_ID/oauth2/authorize",
        },
    },
]