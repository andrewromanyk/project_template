

def output_cmd(text: str):
    print(text)


def output_file(filename: str, text: str):
    with open(filename, 'a') as file:
        file.write(text)

