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
    elif len(sequence) == 2:
        permutation_list.extend(sequence, sequence[1]+sequence[0])
    else:
        #create letter_list
        letter_list = []
        for i in range(len(sequence)):
            letter_list.append(sequence[i])

        for i in range(len(sequence)):
            llc = letter_list
            num = len(sequence)
            word_list=[sequence[i]]
            word_list_2
            while num != 0:
                for j in range(num-1):
                    for k in range(len(word_list)):
                        pos = word_list[k]+
                        word_list_2.append()
                num -= 1


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    pass #delete this line and replace with your code here
