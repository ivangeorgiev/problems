# Terraform Feature Toggle

## Scenario

You are given the following configuration file. Where **AppA** and **AppB** are two applications.

Review the code and complete the tasks below.

## Provided Code

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "rg-demo"
  location = "westeurope"
}


# --------------- AppA --------------------------
resource "azurerm_storage_account" "appa" {
  name                     = "appagensa"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_mssql_server" "appa" {
  name                         = "appa-sql"
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = "Password123!"
}

resource "azurerm_mssql_database" "appa" {
  name      = "appadb"
  server_id = azurerm_mssql_server.appa.id
  sku_name  = "Basic"
}

# --------------- AppB --------------------------
resource "azurerm_storage_account" "appb" {
  name                     = "appbgensa"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_mssql_server" "appb" {
  name                         = "appb-sql"
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = "Password123!"
}

resource "azurerm_mssql_database" "appb" {
  name      = "appbdb"
  server_id = azurerm_mssql_server.appb.id
  sku_name  = "Basic"
}
```


# Tasks

## 1. Identify the Technology
- What language is this code written in?
- What is it used for?



## 2. Explain the Deployment

Briefly explain:

- Which Azure resources are being deployed
- Which resources belong to AppA
- Which resources belong to AppB
- The overall purpose of this configuration



## 3. Implement a Feature Toggle for AppA

Modify the configuration so that deployment of AppA resources can be controlled at execution time.



## 4. Configure Database Tiers Independently

Modify the configuration so that the SQL Database tier can be configured independently for each application.


## Additional task 1 (extra credits): Refactor for redundancy elimination

The current implementation contains duplicated code for AppA and AppB.

Refactor the solution so that applications can be defined using configuration instead of duplicated resources.

Example:

```hcl
applications = {
  appa = {
    enabled = true
    db_tier = "Basic"
  }

  appb = {
    enabled = false
    db_tier = "Premium"
  }
}
```

--- 

# Scoring

* Total score: 100 points
* Passing score: 55 points

| Task | Points |
|--------|--------:|
| Technology Identification | 20 |
| Deployment Explanation | 35 |
| AppA Feature Toggle | 35 |
| Independent Database Tier Configuration | 10 |
| **Total** | **100** |


### Extra Credit Scoring

| Item | Points |
|--------|--------:|
| Generic Configuration Structure | 10 |
| Use of for_each or Similar Pattern | 10 |
| Reduction of Duplicated Code | 10 |
| **Bonus Total** | **30** |

---

# Skills Assessed

- Terraform fundamentals
- Infrastructure as Code (IaC)
- Azure resource deployment
- Terraform variables
- Conditional resource deployment
- Feature toggles
- `count` and `for_each`
- Terraform configuration design
- Code maintainability
- Infrastructure refactoring


