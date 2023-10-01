# Description: methods for ccwc counting bytes, characters, lines, and words.
# Be consistent. Return strings, not integers.


# ccwc -c test.txt
def count_bytes(input_string):
    return f"{len(input_string.encode('utf-8'))}"


# ccwc -c test.txt
def count_characters(input_string):
    return f"{len(input_string)}"


# ccwc -l test.txt
def count_lines(input_string):
    lines = input_string.rstrip().split("\n")
    return f"{len(lines)}"


# ccwc -w test.txt
def count_words(input_string):
    return f"{len(input_string.split())}"


# ccwc test.txt
#   equivalent to -c, -l, and -w options together
def count_all(input_string):
    lines = count_lines(input_string)
    words = count_words(input_string)
    chars = count_characters(input_string)
    return f"{lines} {words} {chars}"
