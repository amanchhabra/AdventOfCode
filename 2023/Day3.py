import re


# Puzzle 1
def solve_puzzle1():
    lines = []
    count = 0
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    pointer = 0
    for line in lines:
        results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", line)]
        for result in results:
            is_valid_part = False
            ir = 0 if result[0] == 0 else result[0] - 1
            er = len(line) if result[1] == len(line) else result[1] + 1
            if pointer != 0:
                old_line = lines[pointer - 1]
                m_string = old_line[ir: er: 1]
                if len(re.findall('^[\d\.]+$', m_string)) == 0:
                    is_valid_part = True
            if pointer < len(lines) - 1:
                old_line = lines[pointer + 1]
                m_string = old_line[ir: er: 1]
                if len(re.findall("^[\d\.]+$", m_string)) == 0:
                    is_valid_part = True
            m_string = line[ir: er: 1]
            if len(re.findall("^[\d\.]+$", m_string)) == 0:
                is_valid_part = True
            if is_valid_part:
                print(result[2])
                count = count + int(result[2])
        pointer = pointer + 1
        print(count)


# Puzzle 2
def solve_puzzle2():
    lines = []
    count = 0
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    pointer = 0
    for line in lines:
        results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\*", line)]
        for result in results:
            matching_parts = []
            if pointer != 0:
                old_line = lines[pointer - 1]
                part_results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", old_line)]
                for part in part_results:
                    if is_connecting_to_star(part, result):
                        matching_parts.append(part)
            if pointer < len(lines) - 1:
                old_line = lines[pointer + 1]
                part_results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", old_line)]
                for part in part_results:
                    if is_connecting_to_star(part, result):
                        matching_parts.append(part)
            part_results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", line)]
            for part in part_results:
                if is_connecting_to_star(part, result):
                    matching_parts.append(part)
            if len(matching_parts) == 2:
                print(matching_parts)
                count = count + (int(matching_parts[0][2]) * int(matching_parts[1][2]))
        pointer = pointer + 1

        print(count)


def is_connecting_to_star(part, star):
    if part[0] - 1 <= star[0] and star[1] <= part[1] + 1:
        return True
    else:
        return False


solve_puzzle2()
