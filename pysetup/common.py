from .exceptions import RequiredFieldError


def check_string(text: str, required: bool = False) -> str:
    """
    Check if the string is different from ""

    :param text: The string ot check
    :type text: str
    :param required: Check if the string is required
    :type required: bool

    :return: The text passed if the field is valid or // of text is not required and == ""
    :rtype: str

    :raise: RequiredFieldError if the text is required and == ""
    """

    if text.replace(" ", "") == "":
        if required:
            raise RequiredFieldError
        else:
            return "//"
    return text
