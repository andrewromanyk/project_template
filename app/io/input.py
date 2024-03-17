import pandas as pd


def input_cmd():
    """
    Queries text from command line and returns it.

    Returns:
        string. Text that the user inputted.
    """
    return input("Enter your text:")


def input_file(filename: str):
    """
    Returns text from a file.

    Args:
        filename (str): name of the file, from which function will read

    Returns:
        string. Contents of the file.

    Raises:
        ValueError: if filename is invalid
        FileNotFoundError: if the file does not exist
    """

    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")

    with open(filename, "r") as file:
        return file.read()


def input_file_pandas(filename: str):
    """
    Returns text from a file. (Uses pandas library)

    Args:
        filename (str): name of the file, from which function will read

    Returns:
        string. Contents of the file.

    Raises:
        ValueError: if filename is invalid
        FileNotFoundError: if the file does not exist
    """
    # I could not a normal way to read text from a .txt file using pandas, only this one,
    # but it works poorly
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")

    return pd.read_csv(filename, header=None, names=['Text']).to_string()
