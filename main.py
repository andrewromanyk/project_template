from app.io.input import *
from app.io.output import *


def main():
    filename_input = "input.txt"
    filename_output = "output.txt"

    cmd = input_cmd()
    output_cmd(cmd)
    output_file(filename_output, cmd)

    file_text = input_file(filename_input)
    output_cmd(file_text)
    output_file(filename_output, file_text)

    file_text_pd = input_file_pandas(filename_input)
    output_cmd(file_text_pd)
    output_file(filename_output, file_text_pd)


if __name__ == '__main__':
    main()
