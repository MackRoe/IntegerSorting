#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    min_num = min(numbers)
    max_num = max(numbers)
    num_range = (max_num - min_num) + 1
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
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    pass

these_nums = [2, 1 , 2, 3, 0, 4, 3, 6]
counting_sort(these_nums)
