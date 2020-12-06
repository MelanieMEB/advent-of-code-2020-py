import unittest
import advent
from collections import Counter

def split_group_string(batch_file):
    current_answers_group = ""
    answers = []
    for line in batch_file:
        if(line == ""):
            answers.append(current_answers_group)
            current_answers_group=""
        else:
            current_answers_group = current_answers_group + line
    answers.append(current_answers_group)
    return answers

def split_group_array(batch_file):
    answers_for_group = []
    groups = []
    for line in batch_file:
        if(line == ""):
            groups.append(answers_for_group)
            answers_for_group = []
        else:
            answers_for_group.append(line)
    groups.append(answers_for_group)
    return groups

def remove_duplicate(string):
  return "".join(dict.fromkeys(string))

def common_char(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    commonDict = dict1 & dict2
    if len(commonDict) == 0:
        return ''
    commonChars = list(commonDict.elements())
    return ''.join(commonChars)

def number_of_yes_answer_for_one_group(group):
    common_answers = group[0]
    for i in range(1, len(group)):
        common_answers = common_char(common_answers, group[i])
    return len(common_answers)

def sum_of_yes_answers_by_anyone(batch_file):
    groups = split_group_string(batch_file)
    return sum([len(remove_duplicate(group)) for group in groups])

def sum_of_yes_answers_by_everyone(batch_file):
    groups = split_group_array(batch_file)
    return sum([number_of_yes_answer_for_one_group(group) for group in groups])

class Tests(unittest.TestCase):
    def test_exemple_1(self):
        # given
        batch_file = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
        expect = 11
        # when
        soluce = sum_of_yes_answers_by_anyone(batch_file)
        # then
        self.assertEqual(soluce, expect)

    def test_number_of_yes_answer_for_one_group(self):
        # given
        group = ['ab', 'ac']
        expect = 1
        # when
        soluce = number_of_yes_answer_for_one_group(group)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_2(self):
        # given
        batch_file = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
        expect = 6
        # when
        soluce = sum_of_yes_answers_by_everyone(batch_file)
        # then
        self.assertEqual(soluce, expect)


if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_06.txt')
    print('Puzzle : ')
    print(sum_of_yes_answers_by_anyone(batch_file))
    print(sum_of_yes_answers_by_everyone(batch_file))
    unittest.main()
