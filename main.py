# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *



# Global Variables - output spacing 
space_variable = "-----------------------------------------------"


def main():
    print("Called Main  Function Successfully")
    print(space_variable)
    """
    print("user input >> " + user_input())
    print(space_variable)
    print("Random Array >> ")

    #Passed a number to the random array function
    random_array(5)
    print(space_variable)
    print(input_number())
    print(space_variable)
    threading_test()
    print(space_variable)
    thread_status_test()
    print(space_variable)
    thread_data_pull()
    """
    list_tests()
    print("Completed Main")
    print(space_variable)
    

def print_list(list):
    for x in list:
        print(x)


def list_tests():
    # create lists
    empty_list = [] 
    basic_list = ["lions", "tigers", "bears"]

    # add elements to a list
    for x in range(6):
        empty_list.append(x)
        basic_list.append(x)
    
    print_list(empty_list)
    print(space_variable)
    
    print_list(basic_list)
    print(space_variable)




     

if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

