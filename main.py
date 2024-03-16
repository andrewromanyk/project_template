from app.io.input import *
from app.io.output import *


def main():
    filename = "input.txt"

    cmd = input_cmd()
    output_cmd(cmd)
    output_file(filename, cmd)

    file_text = input_file(filename)
    output_cmd(file_text)
    output_file(filename, file_text)

    file_text_pd = input_file_pandas(filename)
    output_cmd(file_text_pd)
    output_file(filename, file_text_pd)


if __name__ == '__main__':
    main()
