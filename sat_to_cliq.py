import sys
from itertools import product

def strToList(string):
    lst = list(string.split(" "))
    return lst

def list_product(lst1,lst2):
    return list(product(lst1, lst2))

def remove_contradict(lst):
    count = len(lst)
    for index, tuple in enumerate(lst):
        var1 = tuple[0]
        var2 = tuple[1]
        if var1 != var2:
            if (var1 in var2) or (var2 in var1):
                count = count - 1
    return count


if __name__ == "__main__":
    # convert the first argument to list
    argument = sys.argv[1]
    argumentList = strToList(argument)
    
    # 1st clause of variables
    list1 = argumentList[0:3]
    # 2nd clause of variables
    list2 = argumentList[3:6]
    # 3rd clause of variables
    list3 = argumentList[6:]

    # product of 1st and 2nd clause
    product12 = list_product(list1,list2)
    # product of 2nd and 3rd clause
    product23 = list_product(list2,list3)
    # product of 1st and 3rd clause
    product13 = list_product(list1,list3)

    E = remove_contradict(product12) + remove_contradict(product23) + remove_contradict(product13)

    sys.stdout.write(str(E) + '\n')