import unittest
import advent
import itertools as it
import numpy as np

def exist_two_number_for_sum(numbers_for_sum, sum_result):
    possible_couple = [seq for seq in it.combinations(numbers_for_sum, 2) if sum(seq) == sum_result]
    return sum_result if len(possible_couple) > 0 else None

def first_number_not_sum_of_other(batch_file, preamble):
    numbers = [int(line) for line in batch_file]
    impossible_sum = 0
    for index in range(preamble, len(numbers)):
        numbers_for_sum = numbers[index-preamble:(index-preamble)+preamble]
        result = exist_two_number_for_sum(numbers_for_sum, numbers[index])
        if result is None:
            impossible_sum = numbers[index]
            break
    return impossible_sum

def find_encryption_weakness(batch_file, preamble):
    impossible_sum = first_number_not_sum_of_other(batch_file, preamble)
    numbers = [int(line) for line in batch_file]
    contiguous_number_for_impossible_sum = []
    for i in range(0, len(numbers)):
        for j in range(2, len(numbers) - i + 1):
            if sum(numbers[i:i+j]) == impossible_sum:
                contiguous_number_for_impossible_sum=numbers[i:i+j]
                break
        if contiguous_number_for_impossible_sum != []:
            break
    sorted_contiguous_numbers = np.sort(contiguous_number_for_impossible_sum)
    return sorted_contiguous_numbers[0]+ sorted_contiguous_numbers[-1]


class Tests(unittest.TestCase):
    def test_exemple_1(self):
        # given
        batch_file = [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576"
        ]
        expect = 127
        # when
        soluce = first_number_not_sum_of_other(batch_file, 5)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_1(self):
        # given
        batch_file = [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576"
        ]
        expect = 62
        # when
        soluce = find_encryption_weakness(batch_file, 5)
        # then
        self.assertEqual(soluce, expect)

if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_09.txt')
    print('Puzzle : ')
    print(first_number_not_sum_of_other(batch_file, 25))
    print(find_encryption_weakness(batch_file, 25))
    unittest.main()
