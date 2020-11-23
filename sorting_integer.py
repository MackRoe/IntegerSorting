#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    print('Input List: ', numbers)
    if numbers != []:
        min_num = min(numbers)
        max_num = max(numbers)
        num_range = (max_num - min_num) + 1
    else:
        num_range = 0
    print('Number Range: ', num_range)

    # Create list of counts with a slot for each number in input range
    counting_list = []
    for i in range(num_range):
        counting_list.append(0)
    print("New List Before Counting: ", counting_list)
    # Loop over given numbers and increment each number's count
    for num in numbers:
        counting_list[num] += 1
    print('Accumulated count list', counting_list)
    # TODO: Loop over counts and append that many numbers into output list
    output_list = []
    for i in range(len(counting_list)):
        while counting_list[i] > 0:
            output_list.append(i)
            counting_list[i] = counting_list[i] -1
    print('Output List: ', output_list)
    return output_list

def mutating_counting_sort(numbers):
    # Stretch challenge:
    # Improve counting_sort to mutate input instead of creating new output list
    pass


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum values)
    print('')
    print("***** Begin Bucket Sort *****")
    print("Input list: ", numbers)
    if numbers != []:
        min_val = min(numbers)
        max_val = max(numbers)
    print('min value is: ', min_val, ' and max value is: ', max_val)
    # Create list of buckets to store numbers in subranges of input range
    print('Number of buckets to be created is: ', num_buckets)
    buckets = []
    for i in range(num_buckets):
      print('i: ', i)
      buckets.append([])
      print('Bucket ', i, ' Created')
    # TODO: Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        x = i + 1
        value = numbers[i]
        if value <= len(numbers)//(10 + x):
            buckets[i].append(numbers[i])
            print('Bucket ', i, ' has been assigned', value)

    # Sort each bucket using counting_sort method & append the sorted buckets
    # to the output list variable: sorted_numbers
    sorted_numbers = []
    for i in range(len(buckets)):
        sorted_numbers.append(counting_sort(buckets[i]))

    # Stretch challenge:
    # FIXME: Improve this to mutate input instead of creating new output list
    return sorted_numbers

these_nums = [2, 1 , 2, 3, 0, 4, 3, 6]
counting_sort(these_nums)

nums = [7, 3, 9, 2, 19, 23, 91, 8, 12]
bucket_sort(nums)
