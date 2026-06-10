# PythonProjectStructure

Python Project Organization
A concise reference for folders, modules, imports, and virtual environments in Python.

1. Folders (Packages)
Folders become packages when they contain an __init__.py file (optional in Python 3.3+ but recommended). The __init__.py can be empty or contain package-level setup code.

my_project/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── math_helpers.py
│   └── string_helpers.py
└── services/
    ├── __init__.py
    └── api_client.py
2. Modules
A module is any .py file containing Python code. It enables reusability, organization, and namespace isolation.

# utils/math_helpers.py
PI = 3.14159

def square(x):
    return x * x

def circle_area(r):
    return PI * square(r)
3. Imports
Use imports to load code from other modules.

import utils.math_helpers                      # full path access
from utils.math_helpers import circle_area, PI # direct access
import utils.math_helpers as mh                # alias
from utils.math_helpers import *               # ⚠️ avoid
Python searches for modules in this order:

Script's own directory
PYTHONPATH
Standard library
site-packages (where pip installs packages)
4. Virtual Environments
A virtual environment is an isolated Python install for a project, preventing dependency conflicts.

python -m venv .venv              # create
source .venv/bin/activate         # macOS/Linux
.venv\Scripts\activate            # Windows

pip install requests flask        # install packages
deactivate                        # exit
Always add .venv/ to .gitignore.

How They Connect
Create project folder
    → Add virtual environment
        → Activate it
            → Organize code into packages/modules
                → Use imports to connect them
                    → Use pip to add third-party packages
Real-world example
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
# main.py
from my_app.models import User
from my_app.database.connection import connect
import requests
import json
Quick Reference
Task	Command
Create venv	python -m venv .venv
Activate (macOS/Linux)	source .venv/bin/activate
Activate (Windows)	.venv\Scripts\activate
Install package	pip install <package>
Save deps	pip freeze > requirements.txt
Install from file	pip install -r requirements.txt
Deactivate	deactivate
Concept	What it is	Purpose
Folder	Directory with __init__.py	Groups modules into a package
Module	A .py file	Unit of reusable code
Import	Statement to load code	Access code from other modules
Virtual env	Isolated Python + pip	Prevent dependency conflicts
Recommended Tools
Modern alternatives that combine venvs, dependencies, and project metadata:

uv — extremely fast, Rust-based
Poetry — mature, great for libraries
Hatch — modern, pyproject.toml-driven
pipenv — combines pip + venv
# Example with uv
uv init my_project
cd my_project
uv add requests flask
uv run python main.py
