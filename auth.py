import sys
from database import user_database


def authenticate(credentials):
    upd_credentials = credentials.lower()
    repl_credentials = upd_credentials.replace(" ", "")
    login = repl_credentials.split(":")[0]
    password = repl_credentials.split(":")[1]

    if login in user_database:
        if password == user_database[login]:
            print(f"\nWelcome in {login}! Now let's analyze some texts.\n")
        else:
            print("Wrong password!")
            sys.exit(1)
    else:
        print("User not in database!")
        sys.exit(1)