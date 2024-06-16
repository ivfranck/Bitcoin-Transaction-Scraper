# Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Storage Account
resource "azurerm_storage_account" "sa" {
  name                     = var.storage_ac_name
  resource_group_name      = var.resource_group_name
  account_replication_type = "LRS"
  account_tier             = "Standard"
  location                 = var.location
  is_hns_enabled           = true
}


# Files System
resource "azurerm_storage_data_lake_gen2_filesystem" "adlfs" {
  name               = var.file_system_name
  storage_account_id = azurerm_storage_account.sa.id
}

# Directories
resource "azurerm_storage_data_lake_gen2_path" "dlp" {
  for_each           = toset(var.directory_paths)
  path               = each.key
  filesystem_name    = azurerm_storage_data_lake_gen2_filesystem.adlfs.name
  resource           = "directory"
  storage_account_id = azurerm_storage_account.sa.id
}

# ASQL Server
resource "azurerm_mssql_server" "asqls" {
  name                         = var.asqls_name
  resource_group_name          = var.resource_group_name
  location                     = "uksouth"
  version                      = "12.0"
  administrator_login          = var.sql_server_admin_username
  administrator_login_password = var.sql_server_admin_password
  minimum_tls_version          = "1.2"

  azuread_administrator {
    login_username = var.login_username
    object_id      = var.azure_ad_admin_object_id
    tenant_id      = var.azure_ad_admin_tenant_id
  }

}

# ASQL Server Firewall Rule
resource "azurerm_mssql_firewall_rule" "sqlfr" {
  end_ip_address   = var.client_ipv4_address
  name             = var.client_ip_name
  server_id        = azurerm_mssql_server.asqls.id
  start_ip_address = var.client_ipv4_address
}


# ASQL DB
resource "azurerm_mssql_database" "mssql" {
  name                 = var.asqldb_name
  server_id            = azurerm_mssql_server.asqls.id
  storage_account_type = "Local"
}

# Azure Data Factory
resource "azurerm_data_factory" "adf" {
  location            = var.location
  name                = var.adf_name
  resource_group_name = var.resource_group_name
  identity {
    type = "SystemAssigned"
  }
}

# Azure Databricks
resource "azurerm_databricks_workspace" "adbw" {
  location            = var.location
  name                = var.adbw_name
  resource_group_name = var.resource_group_name
  sku                 = "trial"
}