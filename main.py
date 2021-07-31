# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def maxValue(list):
    max = list[0]
    for value in list:
        if value > max:
            max = value
    return max


if __name__ == '__main__':
    list = [1, 3, 6, -8, 0, 5]
    print("max is: ", maxValue(list))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
