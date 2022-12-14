from typing import *

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


def reduce_fs(fs, acc):
    if fs["type"] == "file":
        return fs["size"], acc
    size = 0
    for obj in fs["contents"].keys():
        osize, acc = reduce_fs(fs["contents"][obj], acc)
        size += osize
    if size <= 100000:
        acc += size
    return size, acc


def reduce_fs2(fs, target, acc):
    if fs["type"] == "file":
        return fs["size"], acc
    size = 0
    for obj in fs["contents"].keys():
        osize, acc = reduce_fs2(fs["contents"][obj], target, acc)
        size += osize
    if target <= size < acc:
        acc = size
    return size, acc


def day7_part1():
    lines = [line[:-1] for line in open("day7.txt").readlines()]

    cd = []
    fs = {"type": "dir", "contents": {}}

    for line in lines:
        if line == "$ ls":
            continue
        elif line == "$ cd /":
            cd = []
        elif line.startswith("$ cd"):
            target = line.split(" ")[2]
            if target == "..":
                cd = cd[:-1]
            else:
                cd.append(target)
        else:
            cdo = fs
            for d in cd:
                cdo = cdo["contents"][d]
            if line.startswith("dir"):
                line = line.split(" ")
                cdo["contents"][line[1]] = {"type": "dir", "contents": {}}
            else:
                line = line.split(" ")
                cdo["contents"][line[1]] = {"type": "file", "size": int(line[0])}

    print(reduce_fs(fs, 0)[1])


def day7_part2():
    lines = [line[:-1] for line in open("day7.txt").readlines()]

    cd = []
    fs = {"type": "dir", "contents": {}}

    for line in lines:
        if line == "$ ls":
            continue
        elif line == "$ cd /":
            cd = []
        elif line.startswith("$ cd"):
            target = line.split(" ")[2]
            if target == "..":
                cd = cd[:-1]
            else:
                cd.append(target)
        else:
            cdo = fs
            for d in cd:
                cdo = cdo["contents"][d]
            if line.startswith("dir"):
                line = line.split(" ")
                cdo["contents"][line[1]] = {"type": "dir", "contents": {}}
            else:
                line = line.split(" ")
                cdo["contents"][line[1]] = {"type": "file", "size": int(line[0])}

    size = reduce_fs(fs, 0)[0]

    print(reduce_fs2(fs, size - 40000000, 30000000)[1])


def day8_part1():
    lines = [line[:-1] for line in open("day8.txt").readlines()]

    height = [[int(tree) for tree in line] for line in lines]
    visible = [[False for _ in line] for line in lines]

    for i in range(0, len(height)):
        h = -1
        for j in range(0, len(height[0])):
            if height[i][j] > h:
                h = height[i][j]
                visible[i][j] = True
        h = -1
        for j in range(len(height[0]) - 1, -1, -1):
            if height[i][j] > h:
                h = height[i][j]
                visible[i][j] = True
    for j in range(0, len(height[0])):
        h = -1
        for i in range(0, len(height)):
            if height[i][j] > h:
                h = height[i][j]
                visible[i][j] = True
        h = -1
        for i in range(len(height) - 1, -1, -1):
            if height[i][j] > h:
                h = height[i][j]
                visible[i][j] = True

    count = 0
    for i in range(0, len(height)):
        for j in range(0, len(height[0])):
            if visible[i][j]:
                count += 1

    print(count)


def day8_part2():
    lines = [line[:-1] for line in open("day8.txt").readlines()]

    height = [[int(tree) for tree in line] for line in lines]
    result = 0

    for i in range(0, len(height)):
        for j in range(0, len(height[0])):
            up = 0
            down = 0
            left = 0
            right = 0
            for k in range(j - 1, -1, -1):
                if height[i][k] <= height[i][j]:
                    up += 1
                if height[i][k] >= height[i][j]:
                    break
            for k in range(j + 1, len(height[0])):
                if height[i][k] <= height[i][j]:
                    down += 1
                if height[i][k] >= height[i][j]:
                    break
            for k in range(i - 1, -1, -1):
                if height[k][j] <= height[i][j]:
                    left += 1
                if height[k][j] >= height[i][j]:
                    break
            for k in range(i + 1, len(height)):
                if height[k][j] <= height[i][j]:
                    right += 1
                if height[k][j] >= height[i][j]:
                    break

            result = max(result, up * down * left * right)

    print(result)


def day9_part1():
    lines = [line[:-1] for line in open("day9.txt").readlines()]

    result = set()
    head = [0, 0]
    tail = [0, 0]
    result.add(tuple(tail))

    for line in lines:
        line = line.split(" ")
        dir = (0, 0)
        if line[0] == "L":
            dir = (-1, 0)
        elif line[0] == "R":
            dir = (1, 0)
        elif line[0] == "U":
            dir = (0, -1)
        elif line[0] == "D":
            dir = (0, 1)
        for _ in range(0, int(line[1])):
            head[0] += dir[0]
            head[1] += dir[1]
            if head[0] == tail[0]:
                if head[1] == tail[1] + 2:
                    tail[1] += 1
                elif head[1] == tail[1] - 2:
                    tail[1] -= 1
            elif head[1] == tail[1]:
                if head[0] == tail[0] + 2:
                    tail[0] += 1
                elif head[0] == tail[0] - 2:
                    tail[0] -= 1
            elif abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                if head[0] > tail[0]:
                    tail[0] += 1
                elif head[0] < tail[0]:
                    tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                elif head[1] < tail[1]:
                    tail[1] -= 1
            result.add(tuple(tail))

    print(len(result))


def day9_part2():
    lines = [line[:-1] for line in open("day9.txt").readlines()]

    result = set()
    knots = [[0, 0] for _ in range(0, 10)]
    result.add(tuple(knots[-1]))

    for line in lines:
        line = line.split(" ")
        dir = (0, 0)
        if line[0] == "L":
            dir = (-1, 0)
        elif line[0] == "R":
            dir = (1, 0)
        elif line[0] == "U":
            dir = (0, -1)
        elif line[0] == "D":
            dir = (0, 1)
        for _ in range(0, int(line[1])):
            knots[0][0] += dir[0]
            knots[0][1] += dir[1]
            for i in range(0, 9):
                if knots[i][0] == knots[i + 1][0]:
                    if knots[i][1] == knots[i + 1][1] + 2:
                        knots[i + 1][1] += 1
                    elif knots[i][1] == knots[i + 1][1] - 2:
                        knots[i + 1][1] -= 1
                elif knots[i][1] == knots[i + 1][1]:
                    if knots[i][0] == knots[i + 1][0] + 2:
                        knots[i + 1][0] += 1
                    elif knots[i][0] == knots[i + 1][0] - 2:
                        knots[i + 1][0] -= 1
                elif abs(knots[i][0] - knots[i + 1][0]) > 1 or abs(knots[i][1] - knots[i + 1][1]) > 1:
                    if knots[i][0] > knots[i + 1][0]:
                        knots[i + 1][0] += 1
                    elif knots[i][0] < knots[i + 1][0]:
                        knots[i + 1][0] -= 1
                    if knots[i][1] > knots[i + 1][1]:
                        knots[i + 1][1] += 1
                    elif knots[i][1] < knots[i + 1][1]:
                        knots[i + 1][1] -= 1
            result.add(tuple(knots[-1]))

    print(len(result))


def day10_part1():
    lines = [line[:-1] for line in open("day10.txt").readlines()]

    x = 1
    signal = []
    for instr in lines:
        signal.append(x)
        if instr == "noop":
            continue
        else:
            signal.append(x)
            x += int(instr.split(" ")[1])
    signal.append(x)

    print(20 * signal[19] + 60 * signal[59] + 100 * signal[99] + 140 * signal[139] + 180 * signal[179] + 220 * signal[219])


def day10_part2():
    lines = [line[:-1] for line in open("day10.txt").readlines()]

    x = 1
    signal = []
    for instr in lines:
        signal.append(x)
        if instr == "noop":
            continue
        else:
            signal.append(x)
            x += int(instr.split(" ")[1])
    signal.append(x)

    for i in range(0, len(signal)):
        if abs((i % 40) - signal[i]) < 2:
            print("#", end="")
        else:
            print(".", end="")
        if (i + 1) % 40 == 0:
            print()


def day11_part1():
    lines = [line[:-1] for line in open("day11.txt").readlines()]

    monkeys = []
    for i, line in enumerate(lines):
        if line.startswith("Monkey"):
            monkey: dict[Union[str, bool], Union[str, int, list[Union[str, int]]]] = {"items": [int(item) for item in lines[i + 1].split(":")[1].split(",")]}
            exp = lines[i + 2].split("=")[1]
            if "+" in exp:
                monkey["op"] = "+"
            elif "*" in exp:
                monkey["op"] = "*"
            exp = exp.split(monkey["op"])
            monkey["arg"]: List[Union[str, int]] = []
            if "old" in exp[0]:
                monkey["arg"].append("old")
            else:
                monkey["arg"].append(int(exp[0]))
            if "old" in exp[1]:
                monkey["arg"].append("old")
            else:
                monkey["arg"].append(int(exp[1]))
            monkey["test"] = int(lines[i + 3].split(" ")[-1])
            lines = lines
            monkey[True] = int(lines[i + 4].split(" ")[-1])
            monkey[False] = int(lines[i + 5].split(" ")[-1])
            monkey["inspect"] = 0
            monkeys.append(monkey)

    for _ in range(0, 20):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                item = monkey["items"][0]
                monkey["items"] = monkey["items"][1:]
                monkey["inspect"] += 1
                arg0 = monkey["arg"][0]
                arg1 = monkey["arg"][1]
                if arg0 == "old":
                    arg0 = item
                if arg1 == "old":
                    arg1 = item
                if monkey["op"] == "+":
                    item = arg0 + arg1
                elif monkey["op"] == "*":
                    item = arg0 * arg1
                item //= 3
                monkeys[monkey[item % monkey["test"] == 0]]["items"].append(item)

    business = sorted([monkey["inspect"] for monkey in monkeys], reverse=True)

    print(business[0] * business[1])


def day11_part2():
    lines = [line[:-1] for line in open("day11.txt").readlines()]

    monkeys = []
    for i, line in enumerate(lines):
        if line.startswith("Monkey"):
            monkey: dict[Union[str, bool], Union[str, int, list[Union[str, int]]]] = {"items": [int(item) for item in lines[i + 1].split(":")[1].split(",")]}
            exp = lines[i + 2].split("=")[1]
            if "+" in exp:
                monkey["op"] = "+"
            elif "*" in exp:
                monkey["op"] = "*"
            exp = exp.split(monkey["op"])
            monkey["arg"]: List[Union[str, int]] = []
            if "old" in exp[0]:
                monkey["arg"].append("old")
            else:
                monkey["arg"].append(int(exp[0]))
            if "old" in exp[1]:
                monkey["arg"].append("old")
            else:
                monkey["arg"].append(int(exp[1]))
            monkey["test"] = int(lines[i + 3].split(" ")[-1])
            lines = lines
            monkey[True] = int(lines[i + 4].split(" ")[-1])
            monkey[False] = int(lines[i + 5].split(" ")[-1])
            monkey["inspect"] = 0
            monkeys.append(monkey)

    modulus = 1
    for monkey in monkeys:
        modulus *= monkey["test"]

    for _ in range(0, 10000):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                item = monkey["items"][0]
                monkey["items"] = monkey["items"][1:]
                monkey["inspect"] += 1
                arg0 = monkey["arg"][0]
                arg1 = monkey["arg"][1]
                if arg0 == "old":
                    arg0 = item
                if arg1 == "old":
                    arg1 = item
                if monkey["op"] == "+":
                    item = (arg0 + arg1) % modulus
                elif monkey["op"] == "*":
                    item = (arg0 * arg1) % modulus
                monkeys[monkey[item % monkey["test"] == 0]]["items"].append(item)

    business = sorted([monkey["inspect"] for monkey in monkeys], reverse=True)

    print(business[0] * business[1])


if __name__ == '__main__':
    day11_part2()
