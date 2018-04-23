# -*- coding: utf-8 -*-
# Problem Set 4A
# Name: <Michael Eusuk Jo>
# Collaborators:
# Time Spent: x:xx
# This only deals with words that does not have overlapping words

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
            word_num_list =['/%d/'%i]
            while num != 1:
                word_list_2 = []
                word_num_list_2=[]
                for j in range(len(word_num_list)):
                    llc = []
                    llcl=[]
                    for k in range(len(letter_list)):
                        if '/%d/'%k not in word_num_list[j]:
                            llc.append(letter_list[k])
                            llcl.append('/%d/'%k)
                    for k in range(len(llc)):
                        word_list_2.append(word_list[j]+llc[k])
                        word_num_list_2.append(word_num_list[j]+llcl[k])
                word_list = word_list_2
                word_num_list = word_num_list_2
                num -= 1
            for word in word_list:
                if word not in permutation_list:
                    permutation_list.append(word)

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
word = 'abcdefghij'
permu = get_permutations(word)
print(permu)
print(len(permu))
