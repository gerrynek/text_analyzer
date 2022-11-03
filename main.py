"""
author: Jaroslav List
email: jaroslav.list@kiwi.com
discord: Jara#4939
"""

import re
import sys
from time import sleep
from loading import loading

from database import TEXTS
from auth import authenticate


credentials = input("Enter login and password splitted by colon(:): ")

try:
    authenticate(credentials)
except IndexError:
    print("Wrong format of credentials")
    sys.exit(2)
    
print(f"Welcome {authenticate(credentials)}")
print("Loading database")
print("-"*28)
for i in range(21):
    loading(i)
    sleep(0.02)
    if i == 20:
        print()
print("-"*28)

while True:
    try:
        text_selection = int(input("Select which text you want to analyze (1-3): "))
        if text_selection not in range(1, 4):
            print("This text is not in the database.")
        else:
            break

    except ValueError:
        print("Please insert a number!")

print(TEXTS[text_selection-1])

prepared_text = TEXTS[text_selection-1].replace("-", " ")
raw_split = prepared_text.split()

def eliminateInterpuction(raw_list):
    list_of_words = []
    for i in raw_split:
        x = i.replace(",", "")
        x = x.replace(".", "")
        x = x.replace("!", "")
        list_of_words.append(x)
    return list_of_words
    
print(eliminateInterpuction(raw_split))


"""
počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.

Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
"""