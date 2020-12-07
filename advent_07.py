import unittest
import advent


def color_contain_asked_colors(bag_rules, colors):
    color_accepted = []
    for rule in bag_rules:
        for color in colors:
            if color in rule[1]:
                color_accepted.append(rule[0].replace(" bags", ""))
    return color_accepted


def number_of_bag_color_contain_asked_color(batch_file, asked_color):
    bag_rules = [line.split(" contain ") for line in batch_file]
    colors = [asked_color]
    colors_contain_asked_color = []
    while True:
        new_colors = color_contain_asked_colors(bag_rules, colors)
        colors_contain_asked_color = colors_contain_asked_color + new_colors
        colors = new_colors
        if len(new_colors) == 0:
            break
    return len(list(dict.fromkeys(colors_contain_asked_color)))


def number_of_bag_in_bag(bag_rules, color):
    sum_of_bag = []
    for inner_bag in bag_rules[color]:
        multiply = inner_bag.split(" ")[0]
        if(multiply == "no"):
            return 0
        inner_bag_color = inner_bag.split(" ")[1]+" "+inner_bag.split(" ")[2]
        sum_of_bag.append(int(multiply) + int(multiply)*number_of_bag_in_bag(bag_rules, inner_bag_color))
    return sum(sum_of_bag)


def number_of_bag_inside(batch_file, asked_color):
    bag_rules = dict([
                         line.replace("bags ", "").split(" contain ")[0],
                         line.replace(" bags", "").replace(" bag", "").replace(".", "").split(" contain ")[1].split(", ")
                     ]for line in batch_file)
    return number_of_bag_in_bag(bag_rules, asked_color)

class Tests(unittest.TestCase):
    def test_exemple_1(self):
        # given
        batch_file = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        expect = 4
        # when
        soluce = number_of_bag_color_contain_asked_color(batch_file, "shiny gold")
        # then
        self.assertEqual(soluce, expect)

    def test_exemple_2(self):
        # given
        batch_file = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        expect = 32
        # when
        soluce = number_of_bag_inside(batch_file, "shiny gold")
        # then
        self.assertEqual(soluce, expect)


if __name__ == '__main__':
    batch_file = advent.read_files('puzzle_files/file_07.txt')
    print('Puzzle : ')
    print(number_of_bag_color_contain_asked_color(batch_file, "shiny gold"))
    print(number_of_bag_inside(batch_file, "shiny gold"))
    unittest.main()
