import json

from .common import check_string
from .files import STRUCT


def univoque(text: str) -> str:
    """Text passed is returned as univoque string

    :param text: The text to pass
    :type text: str

    :return: The modified text
    :rtype: str
    """
    return text.lower().replace(" ", "")


def input_confirmation(user_input: str, *checks) -> bool:
    """Checks if the user_input is valid

    :param user_input: User's input
    :type user_input: str

    :return: Wether the user_input is valid
    :rtype: bool
    """
    for check in checks:
        if univoque(check_string(user_input)) == univoque(check):
            return True

    return False


def continuous_input(input_string: str, break_string: str) -> list[str]:
    """Starts a continous loop in which the user will input separate strings

    :param input_string: The text to display as input
    :type input_string: str
    :param break_string: The string which will stop the loop in passed as user input
    :type break_string: str

    :return: A list of strings which user passed as input
    :rtype: list[str]
    """
    returned = []
    user_input = input(f"{input_string} ({break_string} to finish)")
    while univoque(user_input) != break_string:
        returned.append(user_input)
    return returned


def manage_user_input(
    input_string: str, additional_function: any = None, *input_parameters
) -> str:
    """Iterates an input until the input parameters are checked and returns the user input

    :param input_string: The text to display as input
    :type input_string: str
    :param additional_function: An additional function to use in while loop
    :type additional_function: fucntion

    :return: The user input
    :rtype: str
    """

    user_input = input(f'{input_string} ({"/".join(input_parameters)})')
    while not input_confirmation(user_input, *input_parameters):
        user_input = input(f'{input_string} ({"/".join(input_parameters)})')
        if additional_function:
            additional_function()

    return user_input


# ===== ACTUAL ASKS


def ask_git() -> bool:
    """Asks if the user wants to create a git repo with this project

    :return: Wether the project has git initialized or not
    :rtype: bool"""

    user_input = manage_user_input("Initialize git?", None, "y", "n")

    if univoque(user_input) == "y":
        return True
    return False


def ask_git_branches() -> list[str]:
    """Asks the user which branches to use in this project

    :return: a list of branch names
    :rtype: list[str]"""

    branches = continuous_input("Add a git branch:", "//")
    return branches


def ask_github() -> bool:
    """Asks if the user wants to use github

    :return: Wether the projects will use github or not
    :rtype: bool
    """

    user_input = manage_user_input("Use github?", None, "y", "n")

    if univoque(user_input) == "y":
        return True
    return False


def ask_github_remote() -> list[str]:
    """Asks for github remote name and link

    :return: A list: [remote_name, remote_link]
    :rtype: list[str]
    """

    remote = input("Github remote name: ")
    while check_string(remote) == "//":
        print("Please enter a valid name")
        remote = input("Github remote name: ")

    link = input("Github remote link: ")
    while check_string(link) == "//":
        print("Please enter a valid url")
        remote = input("Github remote link")

    return [remote, link]


def ask_sphinx() -> bool:
    """Asks if user wants to use sphinx for documentation

    :return: Wether the projects will use sphinx as documentation or not
    :rtype: bool"""

    user_input = manage_user_input("Use sphinx for documentation?", None, "y", "n")

    if univoque(user_input) == "y":
        return True
    return False


def ask_dependencies() -> list[str]:
    """Asks user for project dependencies to insert into pyproject.toml

    :return: A list of dependencies
    :rtype: list[str]
    """

    dependencies = continuous_input(
        "Add a project dependency in format dependency_name==dependency_version", "//"
    )
    return dependencies


def ask_gitignore() -> list[str]:
    """Asks the user for files to insert into .gitignore

    :return: A list of files / directories to ignore
    :rtype: list[str]
    """
    gitignore = continuous_input(".gitignore files:", "//")
    return gitignore
