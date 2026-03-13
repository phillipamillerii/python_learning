# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *



# Global Variables - output spacing 
space_variable = "-----------------------------------------------"


def main():
    print("Called Main  Function Successfully")
    print(space_variable)
    
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
    

    print(space_variable)
    print("Completed Main")
    
    


     

if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

