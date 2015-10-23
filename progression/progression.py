"""
From my mam:

Task:
Given some real numbers check whether it is possible to get a progression.

Input:
A single string containing numbers isolated with whitespace.

Output:
Program should print YES if positive, NO if negative.
After answer new line character should be printed.
"""


def has_progression(num_list):
    """
    Checks whether lists contains a fragment of progression.
    Not all list elements need to be a part of the progresion.
    """
    num_list = [float(num) for num in sorted(num_list)]
    if len(num_list) < 3:
        return False
    for nx, x in enumerate(num_list):
        start_y = nx + 1
        for ny, y in enumerate(num_list[start_y:]):
            start_z = start_y + ny + 1
            for z in num_list[start_z:]:
                if y == round((x + z) / 2.0, 5):
                    return True
    return False


def is_progression(num_list, sort_list=True):
    """Check whether given list of numbers is a progression"""
    if sort_list:
        num_list = [float(num) for num in sorted(num_list)]
    if len(num_list) < 3:
        return False
    if num_list[1] == (num_list[0] + num_list[2]) / 2.0:
        if len(num_list) == 3:
            return True
        return is_progression(num_list[1:], sort_list=False)
    return False


if __name__ == '__main__':
    numbers_str = input('Type numbers separated with whitespace > ')
    num_list = [float(num) for num in numbers_str.split(' ')]
    if has_progression(num_list):
        print('YES\n')
    else:
        print('NO\n')

