def countOfWords(data):
    count_of_words = len(data)
    return count_of_words

def countOfFirstCapital(data):
    count_of_first_capital = 0
    for word in data:
        if word.istitle():
            count_of_first_capital+=1
    return count_of_first_capital

def countOfCapitalCase(data):
    count_of_capital_case = 0
    for word in data:
        if word.isupper():
            if word.isalpha():
                count_of_capital_case+=1
    return count_of_capital_case

def countOfLowerCase(data):
    count_of_lower_case = 0
    for word in data:
        if word.islower():
            count_of_lower_case+=1
    return count_of_lower_case

def countOfNumbers(data):
    count_of_numbers = 0
    for word in data:
        if word.isnumeric():
            count_of_numbers+=1
    return count_of_numbers

def sumOfNumbers(data):
    sum_of_numbers = 0
    for word in data:
        if word.isnumeric():
            sum_of_numbers+=int(word)
    return sum_of_numbers

def countOfOccurencies(data):
    count_of_lengths = {}
    count = 0
    list_of_lengths=[]
    for word in data:
        list_of_lengths.append(len(word))

    for length in list_of_lengths:
        count = list_of_lengths.count(length)
        count_of_lengths.update({length:count})

    count_of_lengths_sorted = dict(sorted(count_of_lengths.items()))
    return count_of_lengths_sorted
