import string
def count_words(sentence):
    word_list = {}

    #Replace all punctuation with a whitespace to simplify the split
    for i in string.punctuation.replace("'", ""):
        sentence = sentence.replace(i, " ")
    
    sentence = sentence.lower().split()

    for word in sentence:
        striped_word = word.strip("'")
        if striped_word != "":
            if striped_word in word_list:
                word_list[striped_word] += 1
            else:
                word_list[striped_word] = 1

    return word_list