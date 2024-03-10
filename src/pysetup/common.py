from .exceptions import RequiredFieldError


def check_string(text: str, required: bool = False) -> str:
    """
    Check if the string is different from "".
    ---
    ---
    ### Parameters
    1. text : str
        - The string to check
    2. required : bool
        - Check if the string is required
    ---
    ### Returns
    - The text passed if the field is valid
    - "//" if the text is not required == ""
    ---
    ### Raises
    - RequiredFieldError
        - If the text is required and == ""
    """
    if text.replace(" ", "") == "":
        if required:
            raise RequiredFieldError
        else:
            return "//"
    return text


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
