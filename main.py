# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *
from config import *


def main():
    logger.info('Called Main Function Successfully')

    """
    print("user input >> " + user_input())
    print("Random Array >> ")
    #Passed a number to the random array function
    random_array(5)
    print(input_number())
    threading_test()
    thread_status_test()
    thread_data_pull()
    list_tests()
    """

    bankdatabase = database()

    bankdatabase.Add_user("phillip", "password")
    # bankdatabase.update_user("phillip Miller", "new_password_again", 3)
    # bankdatabase.remove_user(13)
    # Password tests using hash
    # bankdatabase.verify_account_pass(1, "password")
    # bankdatabase.verify_account_pass(1, "password2")
    # bankdatabase.update_userpassword("password2", 4)
    # bankdatabase.update_username("Phillip 2", "password2", 4)
    
    bankdatabase.close()

    logger.info('Completed Main Function')
    print(space_variable)


def login(bankdatabase):
    account = input("Account Number : ")
    password = input("Password : ")
    bankdatabase.user_info(account, password)


if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

