

def output_cmd(text: str):
    """
    Prints text to command line.

    Args:
        text (str): Text to output

    Raises:
        ValueError: If text is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Text must be a string")
    print(text)


def output_file(filename: str, text: str):
    """
    Writes text to a specified file. Creates a new file if the specified one doesn't exist.

    Args:
        text (str): Text to output
        filename (str): Name of file to write to

    Raises:
        ValueError: If text or file name is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Text must be a string")
    if not isinstance(filename, str):
        raise ValueError("File name must be a string")
    with open(filename, 'w') as file:
        file.write(text)

