def day1_part1():
    lines = [line[:-1] for line in open("day1.txt").readlines()]

    elves = []
    inv = 0

    for line in lines:
        if line == "":
            elves.append(inv)
            inv = 0
        else:
            inv += int(line)

    print(max(elves))


def day1_part2():
    lines = [line[:-1] for line in open("day1.txt").readlines()]

    elves = []
    inv = 0

    for line in lines:
        if line == "":
            elves.append(inv)
            inv = 0
        else:
            inv += int(line)

    elves.sort(reverse=True)
    print(elves[0] + elves[1] + elves[2])


def day2_part1():
    lines = [line[:-1] for line in open("day2.txt").readlines()]

    score = 0
    for line in lines:
        opp, play = line.split(" ")
        score += {'X': 1, 'Y': 2, 'Z': 3}[play]
        if opp == {'X': 'A', 'Y': 'B', 'Z': 'C'}[play]:
            score += 3
        elif opp == {'X': 'C', 'Y': 'A', 'Z': 'B'}[play]:
            score += 6

    print(score)


def day2_part2():
    lines = [line[:-1] for line in open("day2.txt").readlines()]

    score = 0
    for line in lines:
        opp, play = line.split(" ")
        score += {'X': 0, 'Y': 3, 'Z': 6}[play]
        if play == 'Y':
            throw = {'A': 'X', 'B': 'Y', 'C': 'Z'}[opp]
        elif play == 'X':
            throw = {'A': 'Z', 'B': 'X', 'C': 'Y'}[opp]
        else:
            throw = {'A': 'Y', 'B': 'Z', 'C': 'X'}[opp]
        score += {'X': 1, 'Y': 2, 'Z': 3}[throw]

    print(score)


def day3_part1():
    lines = [line[:-1] for line in open("day3.txt").readlines()]

    result = 0
    for line in lines:
        comp1 = set()

        for i, c in enumerate(line):
            if i < len(line) / 2:
                comp1.add(c)
            elif c in comp1:
                o = ord(c)
                if o <= ord('Z'):
                    result += o - ord('A') + 27
                else:
                    result += o - ord('a') + 1
                break

    print(result)


def day3_part2():
    lines = [line[:-1] for line in open("day3.txt").readlines()]

    result = 0
    s = set()
    d = {}
    i = 0
    for line in lines:
        i += 1
        for c in line:
            s.add(c)

        for c in s:
            d[c] = d.setdefault(c, 0) + 1

            if d[c] == 3:
                o = ord(c)
                if o <= ord('Z'):
                    result += o - ord('A') + 27
                else:
                    result += o - ord('a') + 1
                d = {}
                break

        s = set()

    print(result)


def day4_part1():
    lines = [line[:-1] for line in open("day4.txt").readlines()]

    result = 0
    for line in lines:
        first, second = line.split(",")
        s1, e1 = [int(c) for c in first.split("-")]
        s2, e2 = [int(c) for c in second.split("-")]
        if s1 >= s2 and e1 <= e2 or s1 <= s2 and e1 >= e2:
            result += 1

    print(result)


def day4_part2():
    lines = [line[:-1] for line in open("day4.txt").readlines()]

    result = 0
    for line in lines:
        first, second = line.split(",")
        s1, e1 = [int(c) for c in first.split("-")]
        s2, e2 = [int(c) for c in second.split("-")]
        if s1 <= e2 and e1 >= s2:
            result += 1

    print(result)


def day5_part1():
    lines = [line[:-1] for line in open("day5.txt").readlines()]

    baseline = -1
    stack_count = -1
    for i, line in enumerate(lines):
        if line.startswith(" 1"):
            stack_count = int(line.split(" ")[-1])
            baseline = i
            break

    if baseline < 0 or stack_count < 0:
        return

    stacks = [[] for _ in range(0, stack_count)]

    for i in range(baseline - 1, -1, -1):
        for j in range(0, stack_count):
            if 4 * j + 1 > len(lines[i]):
                continue
            crate = lines[i][4 * j + 1]
            if crate != " ":
                stacks[j].append(crate)

    for line in lines[baseline + 2:]:
        _, count, _, src, _, dst = line.split(" ")
        count = int(count)
        src = int(src)
        dst = int(dst)
        stacks[dst - 1].extend(reversed(stacks[src - 1][-count:]))
        stacks[src - 1] = stacks[src - 1][:-count]

    result = ""
    for stack in stacks:
        result += stack[-1]

    print(result)


def day5_part2():
    lines = [line[:-1] for line in open("day5.txt").readlines()]

    baseline = -1
    stack_count = -1
    for i, line in enumerate(lines):
        if line.startswith(" 1"):
            stack_count = int(line.split(" ")[-1])
            baseline = i
            break

    if baseline < 0 or stack_count < 0:
        return

    stacks = [[] for _ in range(0, stack_count)]

    for i in range(baseline - 1, -1, -1):
        for j in range(0, stack_count):
            if 4 * j + 1 > len(lines[i]):
                continue
            crate = lines[i][4 * j + 1]
            if crate != " ":
                stacks[j].append(crate)

    for line in lines[baseline + 2:]:
        _, count, _, src, _, dst = line.split(" ")
        count = int(count)
        src = int(src)
        dst = int(dst)
        stacks[dst - 1].extend(stacks[src - 1][-count:])
        stacks[src - 1] = stacks[src - 1][:-count]

    result = ""
    for stack in stacks:
        result += stack[-1]

    print(result)


def day6_part1():
    line = [line[:-1] for line in open("day6.txt").readlines()][0]
    for i in range(0, len(line) - 3):
        s = set()
        s.add(line[i])
        s.add(line[i + 1])
        s.add(line[i + 2])
        s.add(line[i + 3])
        if len(s) == 4:
            print(i + 4)
            return


def day6_part2():
    line = [line[:-1] for line in open("day6.txt").readlines()][0]
    for i in range(0, len(line) - 3):
        s = set()
        s.add(line[i])
        s.add(line[i + 1])
        s.add(line[i + 2])
        s.add(line[i + 3])
        s.add(line[i + 4])
        s.add(line[i + 5])
        s.add(line[i + 6])
        s.add(line[i + 7])
        s.add(line[i + 8])
        s.add(line[i + 9])
        s.add(line[i + 10])
        s.add(line[i + 11])
        s.add(line[i + 12])
        s.add(line[i + 13])
        if len(s) == 14:
            print(i + 14)
            return


if __name__ == '__main__':
    day4_part2()
