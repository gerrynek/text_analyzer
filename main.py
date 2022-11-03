"""
author: Jaroslav List
email: jaroslav.list@kiwi.com
discord: Jara#4939
"""

import sys
from time import sleep
from loading import loading

from database import TEXTS
from auth import authenticate
from string_formating import eliminateInterpuction, prepareText


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

print("\n",TEXTS[text_selection-1], "\n")

list_for_analysis = eliminateInterpuction(prepareText(TEXTS[text_selection-1]))

count_of_words = 0
count_of_words = len(list_for_analysis)
print("Total number of words: ",count_of_words)

count_of_first_capital = 0
for word in list_for_analysis:
    if word.istitle():
        count_of_first_capital+=1
print("Words starting with capital: ",count_of_first_capital)

count_of_capital_case = 0
for word in list_for_analysis:
    if word.isupper():
        count_of_capital_case+=1
print("Words in upper case: ",count_of_capital_case)

count_of_lower_case = 0
for word in list_for_analysis:
    if word.islower():
        count_of_lower_case+=1
print("Words in lower case: ",count_of_lower_case)

count_of_numbers = 0
sum_of_numbers = 0
for word in list_for_analysis:
    if word.isnumeric():
        count_of_numbers+=1
        sum_of_numbers+=int(word)
print("Numbers: ",count_of_numbers)
print("Sum of numbers is: ",sum_of_numbers)

dict_ = {}
count = 0

for word in list_for_analysis:
    count = list_for_analysis.count(i)
    dict_.update({word:count})

print(dict_)

"""
Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
"""