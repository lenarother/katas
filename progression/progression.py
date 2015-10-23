"""
From my mam:

Task:
Given some real numbers check whether it is possible to get a progression.

Input:
A single string containing numbers isolated with whitespace.

Output:
Program should print TAK if positive, NIE if negative.
After answer new line character should be printed.
"""


def is_progression(num_list, sort_list=True):
    if sort_list:
        num_list = [float(num) for num in sorted(num_list)]
    if len(num_list) < 3:
        return False
    if num_list[1] == (num_list[0] + num_list[2]) / 2.0:
        if len(num_list) == 3:
            return True
        return is_progression(num_list[1:], sort_list=False)
    return False
