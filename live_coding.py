the_array = [15, 22, 84, 14, 88, 23]

def minmax(array):
    minimum = array[0]
    maximum = array[0]
    difference = 0

    for number in array:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    difference = maximum - minimum

    return difference
