"""
author: Jaroslav List
email: jaroslav.list@kiwi.com
discord: Jara#4939
"""

import sys
from time import sleep
from loading import loading
import termplotlib as tpl
import numpy as np

from database import TEXTS
from auth import authenticate
from string_formating import eliminateInterpuction, prepareText
from text_analysis import countOfWords, countOfFirstCapital, countOfCapitalCase, countOfLowerCase, sumOfNumbers, countOfNumbers



credentials = input("Enter login and password splitted by colon(:): ")

try:
    authenticate(credentials)
except IndexError:
    print("Wrong format of credentials")
    sys.exit(2)

print("\n", "Loading database", "\n")
print("-"*28)
for step in range(21):
    loading(step)
    sleep(0.02)
    if step == 20:
        print()
print("-"*28)

while True:
    try:
        text_selection = int(input("\nSelect which text you want to analyze (1-3): "))
        if text_selection not in range(1, 4):
            print("This text is not in the database.")
        else:
            break

    except ValueError:
        print("Please insert a number!")

list_for_analysis = eliminateInterpuction(prepareText(TEXTS[text_selection-1]))

print("Total number of words: ", countOfWords(list_for_analysis))
print("Words starting with capital: ", countOfFirstCapital(list_for_analysis))
print("Words in upper case: ",countOfCapitalCase(list_for_analysis))
print("Words in lower case: ",countOfLowerCase(list_for_analysis))
print("Numbers: ",countOfNumbers(list_for_analysis))
print("Sum of numbers is: ",sumOfNumbers(list_for_analysis),"\n")

count_of_lengths = {}
count = 0
list_of_lengths=[]
for word in list_for_analysis:
    list_of_lengths.append(len(word))

for length in list_of_lengths:
    count = list_of_lengths.count(length)
    count_of_lengths.update({length:count})

count_of_lengths_sorted = dict(sorted(count_of_lengths.items()))

x = []
y = []

for key, value in count_of_lengths_sorted.items():
    x.append(value)
    y.append(key)

print("|len|", "|count|")
fig = tpl.figure()
fig.barh(x, y)
fig.show()