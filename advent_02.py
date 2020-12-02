import unittest

def read_files(filename):
    return open(filename,'r').read().split('\n')

def split_rules_and_password(password):
    [rules, password] = password.split(': ')
    [rule, letter] = rules.split(' ')
    [min, max] = rule.split('-')
    return [int(min, 10), int(max, 10), letter, password]

def rules_for_correct_password(min_and_position, max_and_position, letter, password, rule):
    rule_number_of_letter = password.count(letter) >= min_and_position and password.count(letter) <= max_and_position
    rule_position_of_letter = (password[min_and_position-1]==letter and password[max_and_position-1]!=letter) \
                or (password[min_and_position-1]!=letter and password[max_and_position-1]==letter)
    if rule == 1:
        return rule_number_of_letter
    else:
        return rule_position_of_letter

def find_number_of_valid_password(passwords, rule):
    rules_and_paswords = map(split_rules_and_password, passwords)
    result = [r_and_p for r_and_p in rules_and_paswords if rules_for_correct_password(r_and_p[0],r_and_p[1],r_and_p[2],r_and_p[3], rule)]
    return len(result)


class Tests(unittest.TestCase):
    def test_split_rules_and_password(self):
        # given
        password_info = "1-3 a: abcde"
        expect = [1, 3, "a", "abcde"]
        # when
        soluce = split_rules_and_password(password_info)
        # then
        self.assertEqual(soluce, expect)

    def test_password_exemple1(self):
        # given
        passwords = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
        expect = 2
        # when
        soluce = find_number_of_valid_password(passwords, 1)
        # then
        self.assertEqual(soluce, expect)

    def test_password_exemple2(self):
        # given
        passwords = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
        expect = 1
        # when
        soluce = find_number_of_valid_password(passwords, 2)
        # then
        self.assertEqual(soluce, expect)

if __name__ == '__main__':
    passwords = read_files('puzzle_files/file_02_1.txt')
    print('Puzzle : ')
    print(find_number_of_valid_password(passwords, 1))
    print(find_number_of_valid_password(passwords, 2))
    unittest.main()


