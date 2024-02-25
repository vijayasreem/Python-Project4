import time
from collections import defaultdict
from typing import List, Optional

import maskpass

import sorts
from consts import *
import utils
import interface

import models

def authentication(privilege: str) -> (Optional[models.Users], int):
    """
    login or create new banking account
    """

    interface.clean_terminal_screen()

    print(utils.greeting())
    print(" Welcome to Long's Bank\n")
    print("Please choose 1 if you already have an account or 2 if you want to create a new one")
    print("  ┌─────────────┐  ╭──────────────────╮                  ")
    print("  │             │  │ ▶︎ 1 • Login     │                ")
    print("  │  L O N G    │  ├──────────────────┴────────────╮     ")
    print("  │  T U A N    │  │ ▶︎ 2 • Create New Account     │   ")
    print("  │  B A N K    │  ├──────────────────┬────────────╯     ")
    print("  │             │  │ ▶︎ 3 • Exit      │                ")
    print("  └─────────────┘  │ ▶︎ 4 • Reset Password │                ")
    print("  └─────────────┘  ╰──────────────────╯                  ")

    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in AUTHENTICATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only 1 to 4")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None, -1

    users = models.Users(privilege)
    user_index = -1

    if user_choice == "1":
        # ... existing login code ...

    if user_choice == "2":
        # ... existing account creation code ...

    if user_choice == "3":
        return None, -1

    if user_choice == "4":
        reset_password_flow(users)

    print("Move to the next step")

    return users, user_index

def reset_password_flow(users: models.Users):
    print("You want to reset your password")
    account_number = ""
    failed_attempt = FAILED_ATTEMPT
    while failed_attempt:
        account_number = input("☞ Please enter your bank account: ")
        if account_number not in users.users_set:
            failed_attempt -= 1
            print("Account does not exist!!! Please enter your own account")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to login again")
        return None, -1

    user_index = sorts.binary_search(users.data, ACCOUNT_NUMBER, account_number)
    if user_index == -1:
        print("You enter wrong choice many times, please wait few minutes to login again")
        return None, -1

    user = users.data[user_index]
    email = get_email()
    if email != user[EMAIL]:
        print("The email does not match the one registered with this account.")
        return None, -1

    # Here we would send the reset link to the user's email.
    # This is a placeholder as the implementation would depend on the email service used.
    print("A password reset link has been sent to your email.")

    # For the purpose of this example, we will continue with the password reset process directly.
    password = get_password(user[PASSWORD])
    if not password:
        return None, -1

    # Update the user's password.
    users.update_password(user_index, password)

    print("Successfully reset password!!!")
    print("You can now login with your new credentials.")

# ... existing functions ...
