import app.io.input as ip

test_text = [
    "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit, sed do eiusmod tempor\nincididunt ut labore et dolore "
    "magna aliqua.",
    """[1] In the beginning God created the heaven and the earth.
             [2] And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
             [3] And God said, Let there be light: and there was light.
             [4] And God saw the light, that it was good: and God divided the light from the darkness.
             [5] And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
             [6] And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.""",
    ""]

filename = "input.txt"


def test_input_file_1():
    text = test_text[0]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file(filename) == text


def test_input_file_2():
    text = test_text[1]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file(filename) == text


def test_input_file_3():
    text = test_text[2]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file(filename) == text


# All pandas tests are supposed to fail since the functions can not normally read the file
def test_input_file_pandas_1():
    text = test_text[0]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file_pandas(filename) == text


def test_input_file_pandas_2():
    text = test_text[1]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file_pandas(filename) == text


def test_input_file_pandas_3():
    text = test_text[2]
    with open(filename, "w") as file:
        file.write(text)
    assert ip.input_file_pandas(filename) == text
