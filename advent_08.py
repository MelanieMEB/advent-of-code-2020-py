import unittest
import advent
import numpy as np

def instruction(instructions, accumulator, index):
    if index >= len(instructions) or index < 0:
        return [accumulator, -1]
    [operation, argument] = instructions[index].split(" ")
    operator = argument[0]
    number = int(argument[1:])
    if operation == 'nop':
        return [accumulator, index + 1]
    if operation == 'acc':
        accumulator = accumulator + number if operator == '+' else accumulator - number
        return [accumulator, index + 1]
    if operation == 'jmp':
        return [accumulator, index + number if operator == '+' else index - number]

def check_if_duplicate_instruction(instructions):
    for elem in instructions:
        if instructions.count(elem) > 1:
            return True
    return False

def find_accumulator_and_stop(instructions):
    list_of_already_run_instructions = [0]
    index = 0
    accumulator = 0
    infinite_loop = False
    while True:
        [accumulator, index] = instruction(instructions, accumulator, index)
        if(index == -1):
            break
        list_of_already_run_instructions.append(index)
        if check_if_duplicate_instruction(list_of_already_run_instructions):
            infinite_loop = True
            break
    return [accumulator, infinite_loop]


def launch_accumulator(batch_file):
    instructions = batch_file
    return find_accumulator_and_stop(instructions)[0]

def accumulator_from_correct_program(batch_file):
    instructions = np.array(batch_file)
    modified_instructions = instructions.copy()
    for index in range(len(instructions)):
        modified_instructions[index] = modified_instructions[index].replace("nop","jmp") \
            if "nop" in modified_instructions[index] \
            else modified_instructions[index].replace("jmp","nop")
        [accumulator, infinite_loop] = find_accumulator_and_stop(modified_instructions)
        if infinite_loop == False:
            return accumulator
        modified_instructions[index] = instructions[index]
    return -1

class Tests(unittest.TestCase):
    def test_exemple_1(self):
        # given
        batch_file = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]
        expect = 5
        # when
        soluce = launch_accumulator(batch_file)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_2(self):
        # given
        batch_file = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"
        ]
        expect = 8
        # when
        soluce = accumulator_from_correct_program(batch_file)
        # then
        self.assertEqual(soluce, expect)


if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_08.txt')
    print('Puzzle : ')
    print(launch_accumulator(batch_file))
    print(accumulator_from_correct_program(batch_file))
    unittest.main()
