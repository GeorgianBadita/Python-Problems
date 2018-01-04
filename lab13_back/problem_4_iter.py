"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   1/4/2018 18:24
    Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele (ordinea
    elementelor este menținută) strict crescătoare.

"""

my_lst = []
sol = []

def print_sol(solution):
    """
    Function tht prints a found solution
    :param solution: the solution
    :return: nothing
    """

    print(*solution)


def check_sol(solution):
    """
    Function
    :param solution: solution to be checked
    :return: True if the solution is valid, False otherwise
    :condition: We need to check if the last two components are in increasing order, if there are
    2 ore more elements
    """
    if len(solution) < 2:
        return True

    dim = len(solution) - 1
    if solution[dim] <= solution[dim - 1]:
        return False
    return True

def back_iter(list, dim):
    """
    The backtracking function
    :return:
    """
    sol = [None]
    start = 0
    while len(sol) > 0:
        choosed = False
        for elem in range(start, len(list)):
            sol[-1] = list[elem]
            choosed = check_sol(sol)

            if choosed is True:
                start = list.index(sol[-1]) + 1
                break

        if choosed:
            if len(sol) == dim:
                print_sol(sol)
            sol.append(None)
        else:
            sol = sol[:-1]
            if len(sol) != 0:
                start = list.index(sol[-1]) + 1




def read_data():
    """
    Funtion that reads the input
    :return: the number of elements of the list
    """
    n = int(input("Please give the number of elements: "))

    for elem in range(n):
        x = int(input("Give a number: "))
        my_lst.append(x)
    return n


def solve(n):
    """
    Function that solves the problem using iterative backtracking
    :param n: number of elements in list
    :return:
    """

    for i in range(n):
        print("The increasing sub-sequences with " + str(i+1) + " element(s) are: ")
        back_iter(my_lst, i + 1)
        print("\n")


solve(read_data())
