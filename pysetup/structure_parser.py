import json
import os
import platform

from progress.bar import IncrementalBar
from datetime import datetime
from time import sleep

from .common import check_string, generate_file
from .files import PYPROJECT_TOML, MIT_LICENSE, README


def read_struct() -> dict:
    """
    Loads the structure of the project from the struct.json file
    ---
    ---
    ### Return
    - dict
        - The structure dictionary.
    ### Raises
    - FileNotFoundError
        - If there's not struct.json file in the current folder
    """
    with open("struct.json", mode="r") as struct_file:
        structure = json.load(struct_file)
    return structure


def build_base(structure: dict) -> None:
    """
    Builds the following:
        -.gitignore file;
        - LICENSE file;
        - pyproject.toml file;
        - README.md file;
        - venv folder;
    ---
    ---
    ### Parameters
    1. structure : dict
        - The structure of the project as in struct.json file.
    """
    proj_name = check_string(structure.get("project_name_required"), True)
    version = check_string(structure.get("project_version"))
    version = "0.0" if version == "//" else version
    description = check_string(structure.get("project_description"))
    author = check_string(structure.get("author"))
    author_email = check_string(structure.get("author_email"))
    homepage = check_string(structure.get("homepage"))
    github = check_string(structure.get("github_link"))
    github_issues = check_string(structure.get("github_issues"))
    gitignore_files = structure.get("gitignore_files")
    dependencies = structure.get("dependencies")

    with IncrementalBar(
        "Building project base", suffix="Ccreating file pyproject.toml", max=5
    ) as bar:
        sleep(0.2)
        generate_file(
            PYPROJECT_TOML.replace("%author%", author)
            .replace("%email%", author_email)
            .replace("%dependencies%", str(dependencies).replace("'", '"'))
            .replace("%homepage%", homepage)
            .replace("%github%", github)
            .replace("%issues%", github_issues)
            .replace("%version%", version)
            .replace("%proj_name%", proj_name)
            .replace("%proj_brief%", description),
            "pyproject.toml",
        )

        sleep(0.2)
        bar.suffix = "Creating file LICENSE"
        bar.next()
        generate_file(
            MIT_LICENSE.replace("%year%", str(datetime.now().year)).replace(
                "%author%", author
            ),
            "LICENSE",
        )

        sleep(0.2)
        bar.suffix = "Creating file .gitignore"
        bar.next()
        generate_file("\n".join(gitignore_files), ".gitignore")

        sleep(0.2)
        bar.suffix = "Creating file README.md"
        bar.next()
        generate_file(README, "README.md")

        sleep(0.2)
        bar.suffix = "Creating virtualenv"
        bar.next()
        if platform.system() == "Windows":
            os.system("python -m venv venv")
        else:
            os.system("python3 -m venv venv")

        sleep(0.2)
        bar.suffix = "Complete"
        bar.next()
        print("")


def install_dependencies(structure: dict) -> None:
    """
    Installs the dependencies
    ---
    ---
    ### Parameters
    1. structure : dict
        - The structure of the project as in struct.json file.
    """
    print("Installing dependencies...")
    dependencies = " ".join(structure.get("dependencies"))
    if dependencies != "":
        os.system(f"venv/bin/pip install {dependencies}")
    print("")


class ModulesBuilder:
    """
    Class made to easily count the iterations of the progress bar
    ---
    ---
    ### Parameters
    1. structure : dict
        - The structure of the project as in struct.json file.
    2. bar : IncrementalBar
        - Used later in functions to get the progress bar to work properly
    3. counter : int
        - The counter of iterations.
    """

    structure: dict
    bar: IncrementalBar
    counter: int = 0

    def initialize(self, structure: dict) -> None:
        """
        Counts the iterations for the progress bar.
        ---
        ---
        ### Parameters
        1. structure : dict
            - The structure of the project as in struct.json file.
        """
        for folder, struct in structure.items():
            self.counter += 1
            for element in struct:
                if isinstance(element, dict):
                    self.initialize(element)

        return None

    def build_inner_structure(self, structure: dict) -> None:
        """
        Parses the struct and creates folders / files for the module / submodules.
        ---
        ---
        ### Parameters
        1. structure : dict
            - The structure of the project as in struct.json file.
        """
        for folder, struct in structure.items():
            self.bar.suffix = "Creating folder " + folder
            self.bar.next()
            sleep(0.2)
            os.mkdir(folder)
            os.chdir(folder)
            for element in struct:
                if isinstance(element, dict):
                    self.build_inner_structure(element)
                else:
                    self.bar.suffix = "Creating file " + element
                    self.bar.next()
                    sleep(0.2)
                    os.system(f"touch {element}")
            os.chdir("..")
        return None

    def build_modules_structure(self) -> None:
        """
        Builds the module structure.
        """

        structure = self.structure.get("structure")
        with IncrementalBar("Building modules structure", max=self.counter - 1) as bar:
            self.bar = bar
            for element in structure:
                if isinstance(element, dict):
                    self.build_inner_structure(element)
                else:
                    self.bar.suffix = "Creating file " + element
                    self.bar.next()
                    sleep(0.2)
                    os.system(f"touch {element}")

            self.bar.suffix = "Complete"
            self.bar.next()
        return None
