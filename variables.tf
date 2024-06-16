variable "resource_group_name" {
  description = "Resource Group name"
  type        = string
  default     = "btc-transactions-rg"
}

variable "asqldb_name" {
  description = "Azure SQL Database name"
  type        = string
  default     = "btc-transactions-db"
}

variable "asqls_name" {
  description = "Azure SQL Server name"
  type        = string
  default     = "btc-transactions-sqlserver"
}

variable "adf_name" {
  description = "Azure Data Factory name"
  type        = string
  default     = "btc-transactions-adf"
}

variable "adbw_name" {
  description = "Azure Databricks Workspace name"
  type        = string
  default     = "btc-transactions-adbw"
}

variable "location" {
  description = "Region name"
  type        = string
  default     = "westeurope"
}

variable "storage_ac_name" {
  description = "Storage Account name"
  type        = string
  default     = "btctransactionssa"
}

variable "file_system_name" {
  type = string
  default = "transactions"
}
variable "directory_paths" {
  type    = list(string)
  default = ["new", "old"]
}


variable "azure_ad_admin_login" {
  description = "Azure AD administrator login for the SQL server"
  type        = string
  default     = "" # Your Azure email
}

variable "azure_ad_admin_object_id" {
  description = "Object ID of the Azure AD administrator"
  type        = string
  default     = "" # Your Azure Account ObjectId
}

variable "azure_ad_admin_tenant_id" {
  description = "Tenant ID of the Azure AD administrator"
  type        = string
  default     = "" # Your Azure Account TenantId
}


variable "sql_server_admin_username" {
  description = "Administrator username for the SQL server"
  type        = string
  default     = "" # Create a username
}

variable "sql_server_admin_password" {
  description = "Administrator password for the SQL server"
  type        = string
  default     = "" # Create a password
}

variable "login_username" {
  type    = string
  default = "" # Create a username
}

variable "client_ipv4_address" {
  description = "IPv4 address to allow access to SQL server"
  type        = string
  default     = "" # Add your Ip
}

variable "client_ip_name" {
  type    = string
  default = "MyIp"
}