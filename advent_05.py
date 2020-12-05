import unittest
import advent

def find_row(line) :
    row_information = line[0:7]
    min = 0
    max = 127
    for letter in row_information:
        middle = int((max-min) / 2)
        min = min if letter == "F" else min+middle+1
        max = max if letter == "B" else min+middle
    return min

def find_column(line) :
    row_information = line[7:10]
    min = 0
    max = 7
    for letter in row_information:
        middle = int((max-min) / 2)
        min = min if letter == "L" else min+middle+1
        max = max if letter == "R" else min+middle
    return min

def analyse_seats(lines) :
    return [find_row(line) * 8 + find_column(line) for line in lines]

def find_max_seat(lines) :
    return max(analyse_seats(lines))

def find_my_seat(lines) :
    already_taken_seat = analyse_seats(lines)
    my_seat = -1
    current_seat = 0
    while my_seat<0:
        possible_set = already_taken_seat[current_seat]+1
        my_seat = possible_set if ((possible_set-1) in already_taken_seat
                                   and (possible_set+1) in already_taken_seat
                                   and not (possible_set) in already_taken_seat) else my_seat
        current_seat = current_seat + 1
    return my_seat

class Tests(unittest.TestCase):
    def test_find_row(self):
        # given
        line ="FBFBBFFRLR"
        expect = 44
        # when
        soluce = find_row(line)
        # then
        self.assertEqual(soluce, expect)

    def test_find_column(self):
        # given
        line ="FBFBBFFRLR"
        expect = 5
        # when
        soluce = find_column(line)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_part_1(self):
        # given
        lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        expect = [567, 119, 820]
        # when
        soluce = analyse_seats(lines)
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_part_1(self):
        # given
        lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        expect = 820
        # when
        soluce = find_max_seat(lines)
        # then
        self.assertEqual(soluce, expect)


if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_05.txt')
    print('Puzzle : ')
    print(find_max_seat(batch_file))
    print(find_my_seat(batch_file))
    unittest.main()
