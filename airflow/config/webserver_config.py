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
# AUTH_OAUTH : Is for OAuth
AUTH_TYPE = AUTH_OAUTH

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

AUTH_ROLES_SYNC_AT_LOGIN = True # Check roles on every login
AUTH_USER_REGISTRATION = True  # Allow users who are not already in the FAB DB
AUTH_USER_REGISTRATION_ROLE = "Public"  # this role will be given in addition to any AUTH_ROLES_MAPPING

AUTH_ROLES_MAPPING = {
    "db925d57-0219-4baf-8d2c-80e0e79c7b7b": ["User"],
    "eaa4ae52-583e-4db1-b3b9-5251fd892bc2": ["Admin"],
}

AZURE_APPLICATION_ID = os.environ["AZURE_APPLICATION_ID"]
AZURE_APPLICATION_SECRET = os.environ["AZURE_APPLICATION_SECRET"]
AZURE_TENANT_ID = os.environ["AZURE_TENANT_ID"]

# scopes: openid email profile offline_access User.Read
# https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc

OAUTH_PROVIDERS = [
    {
        "name": "azure",
        "icon": "fa-windows",
        "token_key": "access_token",
        "remote_app": {
            "client_id": AZURE_APPLICATION_ID,
            "client_secret": AZURE_APPLICATION_SECRET,
            "api_base_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0",
            "client_kwargs": {
                "scope": "openid email profile offline_access",
                "resource": AZURE_APPLICATION_ID,
            },
            "request_token_url": None,
            "access_token_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token",
            "authorize_url": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/authorize",
            "jwks_uri": f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/discovery/v2.0/keys"
        },
    },
]
