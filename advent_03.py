import unittest
import advent

def move(local_geology, position, way):
    possible_way = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2],
    ]
    x_mov = possible_way[way][0]
    y_mov = possible_way[way][1]
    max_x = len(local_geology[0])
    max_y = len(local_geology)
    return [(position[0]+x_mov)%max_x, (position[1]+y_mov)%max_y]

def see_tree(local_geology, position):
    ground = local_geology[position[1]][position[0]]

    return 1 if ground == "#" else 0

def find_all_tree(local_geology, way):
    current_position = [0,0]
    nbr_of_tree = 0
    while current_position[1] < len(local_geology)-1 :
        current_position = move(local_geology, current_position, way)
        nbr_of_tree = nbr_of_tree + see_tree(local_geology, current_position)
    return nbr_of_tree

def multiply_all_solution(local_geology):
    nbr_of_tree_for_each_way = [find_all_tree(local_geology, x) for x in range(5)]
    return advent.multiply(nbr_of_tree_for_each_way)

class Tests(unittest.TestCase):
    def test_find_all_three(self):
        # given
        local_geology =["..##.......",
                        "#...#...#..",
                        ".#....#..#.",
                        "..#.#...#.#",
                        ".#...##..#.",
                        "..#.##.....",
                        ".#.#.#....#",
                        ".#........#",
                        "#.##...#...",
                        "#...##....#",
                        ".#..#...#.#"]
        expect = 7
        # when
        soluce = find_all_tree(local_geology, 1)
        # then
        self.assertEqual(soluce, expect)

    def test_multiply_all_solution(self):
        # given
        local_geology =["..##.......",
                        "#...#...#..",
                        ".#....#..#.",
                        "..#.#...#.#",
                        ".#...##..#.",
                        "..#.##.....",
                        ".#.#.#....#",
                        ".#........#",
                        "#.##...#...",
                        "#...##....#",
                        ".#..#...#.#"]
        expect = 336
        # when
        soluce = multiply_all_solution(local_geology)
        # then
        self.assertEqual(soluce, expect)

if __name__ == '__main__':
    local_geology = advent.read_files('puzzle_files/file_03.txt')
    print('Puzzle : ')
    print(find_all_tree(local_geology, 1))
    print(multiply_all_solution(local_geology))
    unittest.main()
