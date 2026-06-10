# 📦 Python Project Structure

A concise guide to organizing Python projects using packages, modules, imports, and virtual environments.

---

## 📖 Overview

A well-structured Python project is easier to maintain, scale, and collaborate on. This guide covers:

* Packages and folders
* Modules
* Importing code
* Virtual environments
* Dependency management
* Modern Python project tools

---

## 📁 Packages (Folders)

A folder becomes a **package** when it contains an `__init__.py` file.

> **Note:** Since Python 3.3+, `__init__.py` is optional, but including it is considered best practice.

### Example Structure

```text
my_project/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── math_helpers.py
│   └── string_helpers.py
└── services/
    ├── __init__.py
    └── api_client.py
```

### Why Use Packages?

* Organize related code
* Prevent naming conflicts
* Improve project scalability
* Enable cleaner imports

---

## 🧩 Modules

A **module** is any Python file (`.py`) containing code.

Modules help:

* Reuse functionality
* Improve code organization
* Provide namespace isolation

### Example

```python
# utils/math_helpers.py

PI = 3.14159

def square(x):
    return x * x

def circle_area(r):
    return PI * square(r)
```

---

## 🔗 Imports

Imports allow you to access code from other modules.

### Different Import Styles

```python
import utils.math_helpers

from utils.math_helpers import circle_area, PI

import utils.math_helpers as mh

from utils.math_helpers import *  # Not recommended
```

### Python Module Search Order

Python searches for modules in the following order:

1. Current script directory
2. `PYTHONPATH`
3. Standard Library
4. `site-packages` (installed packages)

---

## 🐍 Virtual Environments

A virtual environment creates an isolated Python installation for a project.

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

### Install Packages

```bash
pip install requests flask
```

### Exit Environment

```bash
deactivate
```

> **Best Practice:** Add `.venv/` to `.gitignore`.

---

## 🔄 How Everything Connects

```text
Create Project Folder
        ↓
Create Virtual Environment
        ↓
Activate Environment
        ↓
Organize Code into Packages & Modules
        ↓
Connect Code Using Imports
        ↓
Install Dependencies with pip
```

---

## 🌍 Real-World Example

```text
my_project/
├── .venv/
├── pyproject.toml
├── main.py
└── my_app/
    ├── __init__.py
    ├── models.py
    └── database/
        ├── __init__.py
        └── connection.py
```

### main.py

```python
from my_app.models import User
from my_app.database.connection import connect

import requests
import json
```

---

## ⚡ Quick Reference

| Task                       | Command                           |
| -------------------------- | --------------------------------- |
| Create virtual environment | `python -m venv .venv`            |
| Activate (macOS/Linux)     | `source .venv/bin/activate`       |
| Activate (Windows)         | `.venv\Scripts\activate`          |
| Install package            | `pip install <package>`           |
| Save dependencies          | `pip freeze > requirements.txt`   |
| Install dependencies       | `pip install -r requirements.txt` |
| Deactivate environment     | `deactivate`                      |

---

## 📚 Core Concepts

| Concept             | Description                  | Purpose                                 |
| ------------------- | ---------------------------- | --------------------------------------- |
| Package             | Directory with `__init__.py` | Groups related modules                  |
| Module              | Python `.py` file            | Reusable code unit                      |
| Import              | Statement that loads code    | Access functionality from other modules |
| Virtual Environment | Isolated Python installation | Avoid dependency conflicts              |

---

## 🛠 Recommended Modern Tools

Modern Python tools that manage environments, dependencies, and project metadata.

### 🚀 UV

Fast Rust-based Python package manager and environment tool.

**Features**

* Extremely fast dependency resolution
* Virtual environment management
* Package installation
* Python version management

```bash
uv init my_project
cd my_project
uv add requests flask
uv run python main.py
```

---

### 📦 Poetry

Ideal for Python applications and libraries.

**Features**

* Dependency management
* Virtual environments
* Publishing support

---

### 🐣 Hatch

Modern, `pyproject.toml`-driven workflow.

**Features**

* Environment management
* Build system support
* Plugin ecosystem

---

### 🔧 Pipenv

Combines `pip` and `venv` into a unified workflow.

**Features**

* Dependency locking
* Environment management
* Simpler project setup

---

## ✅ Best Practices

* Use a virtual environment for every project.
* Keep dependencies documented.
* Organize code into packages and modules.
* Avoid wildcard imports (`import *`).
* Use `pyproject.toml` for modern Python projects.
* Add `.venv/` and other generated files to `.gitignore`.

---

This document is provided for educational purposes and may be freely adapted for personal or academic projects.

