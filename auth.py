import sys
from database import user_database


def authenticate(credentials):
    credentials.lower()
    login = credentials.split(":")[0]
    password = credentials.split(":")[1]

    if login in user_database:
        if password == user_database[login]:
            print("Welcome in! Now let's analyze some texts.")
        else:
            print("Wrong password!")
            sys.exit(1)
    else:
        print("User not in database!")
        sys.exit(1)
    return login