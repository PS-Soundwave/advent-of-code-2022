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


if __name__ == '__main__':
    day8_part2()
