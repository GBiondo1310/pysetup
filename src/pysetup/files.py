PYPROJECT_TOML = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "%proj_name%"
version = "%version%"
authors = [
    { name="%author%", email="%email%"},
]
description = "%proj_brief%"
readme = "README.md"
dependencies = %dependencies%

requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "%homepage%"
Github = "%github%"
Issues = "%issues%"
"""

MIT_LICENSE = """MIT License

Copyright (c) "%year%" "%author%"

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GITIGNORE = """__pycache__
venv
tests
*.egg-info
"""

README = """# Install in editable mode:
```
pip install -e .
```

# Install from github:
```
pip install project_name@git+"github_link#egg=<project_name>"
```
"""

STRUCT = """{
    "project_name_required":"Your project name here",
    "project_version": "0.0",
    "project_description":"Project brief description",
    "author":"Author",
    "author_email":"Your email here",
    "homepage":"Homepage of the project",
    "github_link":"Github repo link",
    "github_issues":"Github issues link here",
    "gitignore_files":["venv", "tests", "*egg.info", "scripts", "__pycache__"],
    "dependencies":["loguru==0.7.2"],
    "structure":[
        {
            "scripts":[
                "main.py"
            ]
        },
        {
            "src":[
                "__init__.py",
                {
                    "package_name":[
                        "__init__.py",
                        "__main__.py",
                        {
                            "subpackage1":[
                                "__init__.py"
                            ],
                            "subpackage2":[
                                "__init__.py"
                            ]
                        }
                    ]
                },
                {
                    "tests":[
                        "test.py"
                    ]
                }
            ]
        },
        "other.file",
        "other.file2"
    ]

}"""
