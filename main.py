# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *
from config import *


def main():
    # info('Called Main Function Successfully')
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
    """

    master_mind(random_number_list(3))
    # info('Completed Main Function')
    print(space_variable)


def login(bankdatabase):
    account = input("Account Number : ")
    password = input("Password : ")
    bankdatabase.user_info(account, password)


def master_mind(answer_list):
    # print(answer_list)

    # show the number of inputs required
    list_len = len(answer_list)
    input_list = []
    previous_list = []
    for _ in range(list_len):
        input_list.append('_')

    def empty_line():
        size = shutil.get_terminal_size()
        empty_line = ""
        for _ in range(size.columns):
            empty_line += " "
        return empty_line

    def clear_entry(number_of_lines):
        for _ in range(number_of_lines):
            print("\033[F", end="", flush=True)
            print(empty_line())
            print("\033[F", end="", flush=True)
    
    def check_number():
        while True:
            number_input = input("\n: ")
            try:
                # Attempt to convert the input to an integer
                integer_value = int(number_input)
                # output to logs
                # info('Call to input_number Function Successful')
                # Return the integer value if successful
                return integer_value
            except ValueError:
                # Handle the error if the conversion fails
                # warning('Call to input_number Function Failed')
                clear_entry(2)
                print(f"'{number_input}' is not a valid integer. Please try again.")

    correct_answers = 0
    correct_location = 0

    while True:
        # take the inputs
        print(f'\rYou need to match {list_len} numbers\n{input_list}', end="", flush=True)
        print(f'\rNumber of Correct Answers : {correct_answers}, with {correct_location} in the correct location ', end="", flush=True)
        print(f"\n{input_list}", end="")
        
        if input_list.count('_') > 0:
            input_number = check_number()
            first_empty = input_list.index('_')
            input_list.pop(first_empty)
            input_list.insert(first_empty, int(input_number))
            clear_entry(4)

        else:
                   
            if input_list == answer_list:
                clear_entry(5)
                print("You Win!")
                break
            
            else:
                clear_entry(2)
                print(input_list)
                unique_list = list(dict.fromkeys(input_list))
                correct_answers = 0
                correct_location = 0
                for x in unique_list:
                    if answer_list.count(x) > 0:
                        correct_answers += answer_list.count(x)
                
                if correct_answers > 0:
                    for x in range(len(input_list)):
                        if input_list[x] == answer_list[x]:
                            correct_location += 1

                input_list.clear()   
                for _ in range(list_len):
                    input_list.append('_')
                
  
if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

