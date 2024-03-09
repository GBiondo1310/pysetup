import os
from .files import MIT_LICENSE, PYPROJECT_TOML, GITIGNORE, README


def generate_file(content: str, path: str) -> bool:
    """
    Creates the file in path with its content.
    ---
    ---
    ### Parameters
    1. content : str
        - The content of the file.
    2.path : str
        - The path of the file.
    --
    ### Returns
    - True
        - If the file is created succesfully, else False
    """
    try:
        with open(path, mode="w") as new_file:
            new_file.write(content)
        return True
    except Exception:
        return False


def create_env() -> None:
    """
    Creates the environment in the current folder.
    """
    generate_file(MIT_LICENSE, "LICENSE")
    generate_file(PYPROJECT_TOML, "pyproject.toml")
    generate_file(README, "README.md")
    generate_file(GITIGNORE, ".gitignore")
    os.mkdir("src")
    os.mkdir("src/project_name")
    os.mkdir("src/tests")
    os.mkdir("scripts")
    os.chdir("src")
    generate_file("", "__init__.py")
    os.chdir("project_name")
    generate_file("", "__init__.py")
    os.chdir("../..")
    try:
        os.system("python -m venv venv")
    except Exception:
        os.system("python3 -m venv venv")

    return None


if __name__ == "__main__":
    create_env()
