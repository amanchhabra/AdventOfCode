class Move:
    def __init__(self):
        pass

    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def compare(move1, move2):
        if (move1 == Move.ROCK or move1 == Move.SCISSOR) and (move2 == Move.ROCK or move2 == Move.SCISSOR):
            return -1 if move1 == move2 else 0 if move1 < move2 else 1
        return -1 if move1 == move2 else 0 if move1 > move2 else 1


class Score:
    def __init__(self):
        pass

    WIN = 6
    DRAW = 3
    LOSE = 0


def solve_puzzle1():
    total_count = 0

    while True:
        move1 = 0
        move2 = 0
        line = input()
        if line:
            match line[0]:
                case 'A':
                    move1 = Move.ROCK
                case 'B':
                    move1 = Move.PAPER
                case 'C':
                    move1 = Move.SCISSOR
            match line[2]:
                case 'X':
                    move2 = Move.ROCK
                case 'Y':
                    move2 = Move.PAPER
                case 'Z':
                    move2 = Move.SCISSOR

            match Move.compare(move1, move2):
                case -1:
                    total_count = total_count + move2 + Score.DRAW
                case 0:
                    total_count = total_count + move2 + Score.LOSE
                case 1:
                    total_count = total_count + move2 + Score.WIN
        else:
            print(f"Max count are {total_count}")
            break


def solve_puzzle2():
    total_count = 0

    while True:
        move1 = 0
        move2 = 0
        line = input()
        if line:
            match line[0]:
                case 'A':
                    move1 = Move.ROCK
                case 'B':
                    move1 = Move.PAPER
                case 'C':
                    move1 = Move.SCISSOR
            match line[2]:
                case 'X':
                    move2 = Move.SCISSOR if move1 == Move.ROCK else Move.PAPER if move1 == Move.SCISSOR else Move.ROCK
                case 'Y':
                    move2 = Move.ROCK if move1 == Move.ROCK else Move.SCISSOR if move1 == Move.SCISSOR else Move.PAPER
                case 'Z':
                    move2 = Move.ROCK if move1 == Move.SCISSOR else Move.SCISSOR if move1 == Move.PAPER else Move.PAPER

            match Move.compare(move1, move2):
                case -1:
                    total_count = total_count + move2 + Score.DRAW
                case 0:
                    total_count = total_count + move2 + Score.LOSE
                case 1:
                    total_count = total_count + move2 + Score.WIN
        else:
            print(f"Max count are {total_count}")
            break


solve_puzzle2()
