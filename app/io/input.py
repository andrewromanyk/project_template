import pandas as pd


def input_cmd():
    return input("Enter your text:")


def input_file(filename: str):
    with open(filename, "r") as file:
        return file.read()


def input_file_pandas(filename: str):
    return pd.read_csv(filename).to_string()
