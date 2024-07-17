# Configure Terraform
terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.53.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.112.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  features {}
}

# Create application
data "azuread_client_config" "current" {}

resource "azuread_application" "airflow_sso" {
    device_only_auth_enabled       = false
    display_name                   = "airflow-sso-gui"
    fallback_public_client_enabled = false
    oauth2_post_response_required  = false
    prevent_duplicate_names        = false
    sign_in_audience               = "AzureADMyOrg"

    feature_tags {
        custom_single_sign_on = false
        enterprise            = false
        gallery               = false
        hide                  = false
    }

    required_resource_access {
        resource_app_id = "00000003-0000-0000-c000-000000000000" # Microsoft Graph API

        resource_access {
            id   = "e1fe6dd8-ba31-4d61-89e7-88639da4683d" # Add Microsoft Graph delegated permission User.Read
            type = "Scope"
        }
    }


    web {
        redirect_uris = [
            "https://localhost:8080/oauth-authorized/azure",
        ]

        implicit_grant {
            access_token_issuance_enabled = false
            id_token_issuance_enabled     = false
        }
    }
}

resource "azuread_service_principal" "airflow_sso" {
    account_enabled               = true
    app_role_assignment_required  = false
    client_id                     = azuread_application.airflow_sso.client_id

    feature_tags {
        custom_single_sign_on = false
        enterprise            = true
        gallery               = false
        hide                  = true
    }
}