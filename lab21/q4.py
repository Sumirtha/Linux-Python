def checkList(lst, index):
    try:
        print("Element at index", index, "is:", lst[index])
    except IndexError:
        print("Error: Index out of range.")
    except TypeError:
        print("Error: Invalid type for list or index.")

# (a) Number list and index
checkList([55, 69, 87, 78], 2)
# (b) String input and index (strings are indexable)
checkList("sumirtha", 5)
# (c) Boolean value (True) and index - this is not subscriptable, should raise TypeError
checkList(True, 0)
# (d) String input and incorrect index (out of range)
checkList("joyce", 17)