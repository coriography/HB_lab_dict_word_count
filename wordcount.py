# put your code here.


# create a function with a parameter of filename
def count_words(filename):
    # open file & assign to variable
    file = open(filename)
    # initialize dictionary
    words = {}
        # key = word, value = count of word

    num_lines = 0
    # iterate through by line
    for line in file:
        # split line by space and put in list variable
        line_words = line.lower().rstrip().split(' ')
            # enhancement:
                # remove non-alpha characters (extra enhancement if time allows)
        # loop through list
        for word in line_words:
            # add word to dictionary/update count (in dictionary)
            words[word] = words.get(word, 0) + 1

    # unpack to print key/value pairs (using f string to print)
    # enhancement idea - sort by word count
    for unique_word, word_count in words.items():
        print(f'{unique_word} {word_count}')