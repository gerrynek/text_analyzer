"""
author: Jaroslav List
email: jaroslav.list@kiwi.com
discord: Jara#4939
"""

import sys
from time import sleep
import termplotlib as tpl

from loading import loading
from database import TEXTS
from auth import authenticate
from string_formating import eliminateInterpuction, prepareText
from text_analysis import countOfWords, countOfFirstCapital, countOfCapitalCase, countOfLowerCase, sumOfNumbers, countOfNumbers, countOfOccurencies

#Authentication
credentials = input("Enter login and password splitted by colon(:): ")

try:
    authenticate(credentials)
except IndexError:
    print("Wrong format of credentials!")
    sys.exit(3)

#Some pretty useless stuff
print("\n", "Loading database", "\n")
for step in range(21):
    loading(step)
    sleep(0.02)
    if step == 20:
        print()

#Text selection
while True:
    try:
        text_selection = int(input("\nSelect which text you want to analyze (1-3): "))
        if text_selection not in range(1, 4):
            print("This text is not in the database.")
        else:
            break

    except ValueError:
        print("Please insert a number!")

#Analysis results+String formating
list_for_analysis = eliminateInterpuction(prepareText(TEXTS[text_selection-1]))

print("\n")
print("Total number of words: ", countOfWords(list_for_analysis))
print("Words starting with capital: ", countOfFirstCapital(list_for_analysis))
print("Words in upper case: ",countOfCapitalCase(list_for_analysis))
print("Words in lower case: ",countOfLowerCase(list_for_analysis))
print("Numbers: ",countOfNumbers(list_for_analysis))
print("Sum of numbers is: ",sumOfNumbers(list_for_analysis))
print("\n")

#Plotting
count_of_lengths_sorted = countOfOccurencies(list_for_analysis)

x = []
y = []

for key, value in count_of_lengths_sorted.items():
    x.append(value)
    y.append(key)

print("|len|", "|count|")
fig = tpl.figure()
fig.barh(x, y)
fig.show()