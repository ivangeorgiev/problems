# Repository configuration

## Business Scenario

You have a Git repository created for a Python project.


# Tasks

## Task 1: Configure Git Repository for Python Development

Design an appropriate Git repository configuration for a Python project. Consider common Python development artifacts which need to be excluded from source control.


## Task 2: Development-Only (Local) Data

Developers want to reserve a directory named `local/` for development purposes only and exclude it from source control.



## Task 3: Python Virtual Environment Support

Configure the repository to support Python virtual environments.

Assume developers may use:

```bash
python -m venv .venv
```

or

```bash
uv venv
```



## Task 4: Terraform Support

The project uses Terraform for Infrastructure-as-Code (IaC).

Configure the repository appropriately for Terraform development.

Which files would you exclude from source control? Why?



## Additional Tak 1 (exra credits): On commit quality gate

How would you implement a quality gate on commit, so that:
* Tests are executed on commit
* Guarantee minimum test coverage
* Liters are executed on commit against changed files

