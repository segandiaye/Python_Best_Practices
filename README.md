# 📘 Clean code : best practice

[![codecov](https://codecov.io/gh/segandiaye/Python_Best_Practices/branch/main/graph/badge.svg)](https://codecov.io/gh/segandiaye/Python_Best_Practices)



A brief description of good practices.

# 🚀 Installation

```bash
pip install -r requirements.txt # Installer les dépendances
```

# Manage environment

With pyenv :

```bash
pyenv virtualenv my_env # To create or 
pyenv activate my_env # to activate my_env
```
***With python :***

```bash
python -m venv my_env
```

***With poetry which is the modern alternative to `pip + virtualenv + setuptools`:***

    When NOT to use Poetry :
        - If your project is super minimal, and you prefer pip + venv
        - If you're using a platform that doesn't yet fully support pyproject.toml workflows (rare in 2025)

`pyproject.toml` replaces `setup.py`, `requirements.txt`, and others : a simple example :

```toml
[tool.poetry]
name = "my-awesome-project"
version = "0.1.0"
description = "A Python project managed by Poetry"
authors = ["You <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.2.0"
black = "^24.3.0"
```

| Command               | What it does                                |
| --------------------- | ------------------------------------------- |
| `poetry init`         | Create a new `pyproject.toml` interactively |
| `poetry add numpy`    | Add a dependency                            |
| `poetry remove numpy` | Remove a dependency                         |
| `poetry install`      | Install all dependencies from lock file     |
| `poetry update`       | Update all packages                         |
| `poetry run pytest`   | Run a tool in the project's virtualenv      |
| `poetry shell`        | Activate Poetry-managed shell               |
| `poetry build`        | Build your package                          |
| `poetry publish`      | Publish to PyPI                             |

***With Conda :*** TODO

# Pre-commit

```bash
pre-commit install # Set up Git pre-commit hooks for your project using the pre-commit
```

# Linting

| Feature                 | Flake8 | Pylint    | Ruff                  |
| ----------------------- | ------ | --------- | --------------------- |
| Speed                   | ⚡ Fast | 🐢 Slower | ⚡⚡ Very fast          |
| Style checking          | ✅      | ✅         | ✅                     |
| Logic errors            | ✅      | ✅✅        | ✅                     |
| OOP/class design issues | ❌      | ✅✅        | ❌                     |
| Naming conventions      | ❌      | ✅✅        | ✅ (via Pylint plugin) |
| Config flexibility      | Medium | High      | High                  |
| Plugin ecosystem        | ✅✅     | ✅         | ✅✅✅                   |

# Tests and CI/CD

```bash
pytest tests # Run the tests
```

# Documentation

```bash
mkdocs new . # Create mkdocs.yml
mkdocs build # Build site/docs
mkdocs gh-deploy # Deploy site
```

# Pytest commands utils

```bash
pip install pytest pytest-cov # Necessary modules for tests
pytest --cov=src --cov-branch --cov-report=xml # Run tests and display coverage in CI/CD
PYTHONPATH=src pytest --cov=src tests
PYTHONPATH=src pytest --cov=src --cov-report=term-missing tests # Run tests and display coverage
```

```bash
TODO: add more documentation
```
