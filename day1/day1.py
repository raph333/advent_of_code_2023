REPLACE = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(line: str, is_reverse: bool = False) -> str:
    i = 0

    while i < len(line):
        if line[i].isdigit():
            return line[i]

        for search_string, digit in REPLACE.items():
            if is_reverse:
                search_string = search_string[::-1]
            end_pos = i + len(search_string)
            if end_pos <= len(line) and line[i:end_pos] == search_string:
                return digit
        i += 1


def get_int(line: str) -> int:
    return int(f"{get_first_digit(line)}{get_first_digit(line[::-1], is_reverse=True)}")


with open("input.txt", "r") as f:
    lines = f.readlines()

print(sum([get_int(line) for line in lines]))
