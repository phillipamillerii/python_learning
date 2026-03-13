# Import section 
# from file_name import script/module
import random
import array


import threading
import time




# Variable to help with output spacing. 
space_variable = "-----------------------------------------------"


# Used for starting a thread that is just sleeping
def my_task(name, duration):
    print(f"Thread {name} starting.")
    time.sleep(duration)
    print(f"Thread {name} finished.")


def main():
    print("Called Main Successfully")
    print(space_variable)
    print("user input >> " + user_input())
    print(space_variable)
    print("Random Array >> ")

    #Passed a number to the random array function
    random_array(5)
    print(space_variable)
    print(input_number())
    threading_test()
    
    


# User input, return input
# can perform processes on the variable (check that it contains certain characters, is a specific length, etc..)
def user_input():
    variable_input = input('what do you want to input? : ')
    return_variable = variable_input
    return return_variable


# Create an array and populate it with random numbers 0-9 for the number of times passed to the function
def random_array(number_of_entries):

    # Create an integer array with type code 'i' (signed integer)
    # Type codes specify the data type of the array
    int_array = array.array('i', [])
    for _ in range(number_of_entries):
    
        # creating a random integer between 0-9 and appending it to the basic array I initialized above
        int_array.append(random.randint(0, 9))

    # Because I'm printing the array after I return it I've converted it to a string to be output with other text
    # Will want to change this to a basic return in the future 
    print(int_array)
    print_array_elements(int_array)


def print_array_elements(array_to_print):
    
    # runs a process over every array element
    print("Array output: ")
    for x in range(0, len(array_to_print)):
        print(array_to_print[x])


def input_number():

    # makes sure the input is specifically a number. 
    while True:
        # Get input and remove leading/trailing whitespace
        user_input = input("input a integer : ").strip()
        try:
            
            # Attempt to convert the input to an integer
            integer_value = int(user_input)
            # Return the integer value if successful
            return integer_value
        except ValueError:
            
            # Handle the error if the conversion fails
            print(f"'{user_input}' is not a valid integer. Please try again.")


def threading_test():
    # Create and start threads
    t1 = threading.Thread(target=my_task, args=("A", 5))
    t2 = threading.Thread(target=my_task, args=("B", 3))

    t1.start()
    t2.start()
    # Waits for both to finish before moving on
    t1.join()
    t2.join()
    print("All threads finished.")



if __name__ == '__main__':
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

