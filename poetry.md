# Install poetry

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

The installer installs the poetry tool to Poetry’s bin directory. 
On Unix it is located at $HOME/.poetry/bin and on Windows at %USERPROFILE%\.poetry\bin.

This directory will be automatically added to your $PATH environment variable, 
by appending a statement to your $HOME/.profile configuration (or equivalent files).

You may have to restart your session or do `source ~/.profile`.

## Create a new project

```shell
poetry new project-name
```

This will create the `project-name` directory with the following content:

```
project-name
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

The `pyproject.toml` file is what is the most important here. 
This will orchestrate your project and its dependencies. For now, it looks like this:

```pyproject.toml
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]

[tool.poetry.dependencies]
python = "*"

[tool.poetry.dev-dependencies]
pytest = "^3.4"
```



## Initialising a pre-existing project

Instead of creating a new project, Poetry can be used to ‘initialise’ a 
pre-populated directory. To interactively create a `pyproject.toml` file in 
directory `pre-existing-project`:

```shell
cd pre-existing-project
poetry init
```

## Specifying dependencies

If you want to add dependencies to your project, you can specify them in the 
`tool.poetry.dependencies` section.

```pyproject.toml
[tool.poetry.dependencies]
pendulum = "^1.4"
```

As you can see, it takes a mapping of package names and version constraints.

Poetry uses this information to search for the right set of files 
in package "repositories" that you register in the `tool.poetry.repositories` section, 
or on PyPI by default.

Also, instead of modifying the `pyproject.toml` file by hand, you can use the add command.

```shell
poetry add pendulum
```

## Activating the virtual environment

The easiest way to activate the virtual environment is to create 
a new shell with `poetry shell`. To deactivate the virtual environment 
and exit this new shell type `exit`. To deactivate the virtual environment 
without leaving the shell use `deactivate`.

## Installing dependencies

To install the defined dependencies for your project, run `poetry install`.
This will create `poetry.lock` file. If this file is already present, Poetry will
install the exact versions of the packages listed in `poetry.lock`.

## Incrementing the version in `pyproject.toml`

```shell
poetry version <RULE>
```

where `<RULE>` can be many values, see the documentation for the 
[version](https://python-poetry.org/docs/cli/#version) command.

## Building

```shell
poetry build
```

This creates the source distribution, and the wheel file.

## Testing deployment

Create an account on [test.pypi.org]()

```shell
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

Test deploying to `test.pypi.org`:

```shell
poetry publish -r testpypi
```

## Deploy

```shell
poetry publish
```

## Configuring credentials

See [configuring credentials](https://python-poetry.org/docs/repositories/#configuring-credentials)
in the documentation.

