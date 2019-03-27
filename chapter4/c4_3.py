# calculating the sum of a list of integers

# the old way using an iterator
def oldCalc(my_list):
    the_sum = 0
    for item in my_list:
        the_sum += item

    return the_sum

# recursive solving
def recCalc(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + recCalc(my_list[1:])

# this works because it returns the last element at the end, 
# adds it to the one already in the queue stack,
# does that over and over

li = [1,3,5,7,9]
print(oldCalc(li))
print(recCalc(li))
