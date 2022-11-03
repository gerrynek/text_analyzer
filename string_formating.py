from database import TEXTS

def prepareText(text):
    prepared_text = text.replace("-", " ")
    raw_split = prepared_text.split()
    return raw_split

def eliminateInterpuction(raw_list):
    list_of_words = []
    for i in raw_list:
        x = i.replace(",", "")
        x = x.replace(".", "")
        x = x.replace("!", "")
        list_of_words.append(x)
    return list_of_words