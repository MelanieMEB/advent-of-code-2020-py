import unittest
import advent
import re

#https://regex101.com/

def analyse_batch_file(batch):
    current_password = "-"
    passports = []
    for line in batch:
        if(line == ""):
            current_password = current_password.replace("- ", "")
            current_password = {i.split(':')[0]: i.split(':')[1] for i in current_password.split(' ')}
            passports.append(current_password)
            current_password="-"
        else:
            current_password = current_password + " " + line
    return passports

def analyse_passport(passport):
    mandatories = {"byr": "^(19)[2-9][0-9]|(20)(00|01|02)$",
                   "iyr": "^(20)(1[0-9]|20)$",
                   "eyr": "^(20)(2[0-9]|30)$",
                   "hgt": "^((1[5-9][0-9]cm)|(19[0-3]cm))|(((59)|([6-7][0-9])|7[0-6])(in))$",
                   "hcl": "^#[a-f0-9]{6}$",
                   "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
                   "pid": "^[0-9]{9}$"}
    if len(set(mandatories) - set(passport)) > 0:
        return 0
    return 1 if len([1 for mandatory in mandatories if re.match(mandatories[mandatory], passport[mandatory])]) == len(mandatories) else 0

def find_valid_passports(batch):
    passports = analyse_batch_file(batch)
    return sum([analyse_passport(passport) for passport in passports])

class Tests(unittest.TestCase):
    def test_analyse_batch_file(self):
        # given
        passports =["ecl:gry pid:860033327",
                        "byr:1937",
                        "",
                        "iyr:2013",
                        "hcl:#cfa07d",
                        "",
                    ]
        expect = [{"ecl":"gry", "pid":"860033327", "byr":"1937"},
                  {"iyr": "2013", "hcl":"#cfa07d"} ]
        # when
        soluce = analyse_batch_file(passports)
        # then
        self.assertEqual(soluce, expect)

    def test_analyse_passport_true(self):
        # given
        passport = {"pid":"087499704", "hgt":"74in", "ecl":"grn","iyr":"2012","eyr":"2030","byr":"1980","hcl":"#623a2f"}
        expect = 1
        # when
        print("test")
        soluce = analyse_passport(passport)
        # then
        self.assertEqual(soluce, expect)

    def test_analyse_passport_false_missing_mandatory_field(self):
        # given
        passport = {"pid":"087499704", "hgt":"74in", "iyr":"2012","eyr":"2030","byr":"1980","hcl":"#623a2f"}
        expect = 0
        # when
        soluce = analyse_passport(passport)
        # then
        self.assertEqual(soluce, expect)

    def test_analyse_passport_false_bad_data(self):
        # given
        passport = {"pid":"08749904", "hgt":"74", "ecl":"grn", "iyr":"2012","eyr":"2030","byr":"1980","hcl":"#623a2f"}
        expect = 0
        # when
        soluce = analyse_passport(passport)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple1(self):
        # given
        batch_file =["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                        "byr:1937 iyr:2017 cid:147 hgt:183cm",
                        "",
                        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                        "hcl:#cfa07d byr:1929",
                        "",
                        "hcl:#ae17e1 iyr:2013",
                        "eyr:2024",
                        "ecl:brn pid:760753108 byr:1931",
                        "hgt:179cm",
                        "",
                        "hcl:#cfa07d eyr:2025 pid:166559648",
                        "iyr:2011 ecl:brn hgt:59in",""]
        expect = 2
        # when
        soluce = find_valid_passports(batch_file)
        # then
        self.assertEqual(soluce, expect)


if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_04.txt')
    print('Puzzle : ')
    print(find_valid_passports(batch_file))
    unittest.main()
