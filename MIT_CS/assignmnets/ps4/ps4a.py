# -*- coding: utf-8 -*-
# Problem Set 4A
# Name: <Michael Eusuk Jo>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutation_list = []
    if len(sequence) == 1:
        permutation_list.append(sequence)
    else:
        #create letter_list
        letter_list = []
        for i in range(len(sequence)):
            letter_list.append(sequence[i])


        for i in range(len(sequence)):
            num = len(sequence)
            word_list = [sequence[i]]
            llc = []
            llc.append
            while num != 1:
                word_list_2 = []
                for j in word_list:
                    word_letters =[]
                    llc = []
                    for k in letter_list:
                        if k not in j:
                            llc.append(k)
                    for k in llc:
                        word_list_2.append(j+k)
                word_list = word_list_2
                num -= 1
            permutation_list += word_list

    #중복 제거
    # remove_overlap = []
    # [remove_overlap.append(i) for i in permutation_list if i not in remove_overlap]
    # permutation_list = remove_overlap

    return permutation_list
#
# if __name__ == '__main__':
# #    #EXAMPLE
# #    example_input = 'abc'
# #    print('Input:', example_input)
# #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
# #    print('Actual Output:', get_permutations(example_input))
#
# #    # Put three example test cases here (for your sanity, limit your inputs
# #    to be three characters or fewer as you will have n! permutations for a
# #    sequence of length n)
#
#     example_input = 'abc'
#     print('Input:' example_input)
#     print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#     print('Actuap Output:')

print(get_permutations('abcde'))
print(len(get_permutations('abcde')))
