#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    nums = len(argv)
    if nums == 1:
        print("{}".format(nums - 1))
    elif nums > 1:
        for i in range(len(argv)):
            if i == 0:
                continue
            sum += int(argv[i])
        print("{}".format(sum))
