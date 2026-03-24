from config import *

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
    logger.info("Random Array Created")

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
            # output to logs
            logger.info('Successfully Entered Number')
            # Return the integer value if successful
            return integer_value
        except ValueError:
            # Handle the error if the conversion fails
            logger.warning('Invalid Number Entered')
            print(f"'{user_input}' is not a valid integer. Please try again.")


def threading_test():
    # Used for starting a thread that is just sleeping
    def my_task(name, duration):
        print(f"Thread {name} starting.")
        time.sleep(duration)
        print(f"Thread {name} finished.")
    
    # Create and start threads
    t1 = threading.Thread(target=my_task, args=("A", 5))
    t2 = threading.Thread(target=my_task, args=("B", 3))

    t1.start()
    t2.start()
    # Waits for both to finish before moving on
    t1.join()
    t2.join()
    print("All threads finished.")


def thread_status_test():
    # tests  the thread is_alive process
    def my_task(name, duration):
        print(f"Thread {name} starting.")
        time.sleep(duration)
        print(f"Thread {name} finished.")

    t3 = threading.Thread(target=my_task, args=("C", 2))
    t3.start()

    # Sleep process to make sure the thread has time to complete
    time.sleep(5)

    if t3.is_alive():
        print("Thread Alive")
    else:
        print("Thread Dead")

    print("thread_status_test Complete")


# pulling data from a threaded process
def thread_data_pull():
    def my_task(name, duration, queury):
        print(f"Thread {name} starting.")
        queury.put("Start Data From Thread")

        time.sleep(duration)

        # Setting new Data in the thread
        queury.put("New Data From Thread")
        queury.put("Finished Data From Thread")
        print(f"Thread {name} finished.")

    q = queue.Queue(maxsize=0)
    t = threading.Thread(target=my_task, args=("Test", 2, q))   
    t.start()
    
    # Reporting data from thread
    print("test : " + q.get())
    t.join()

    # Print the size of the queue
    print(q.qsize())
    # Print the available queue after the thread is dead
    for _ in range(q.qsize()):
        print(q.get())
    
    print("Thread data pull complete")


def print_list(list):
    for x in list:
        print(x)


def list_tests():
    # create lists
    empty_list = [] 
    empty_list2 = []
    basic_list = ["lions", "tigers", "bears"]

    empty_list2.extend(basic_list)

    # add elements to a list
    for x in range(6):
        empty_list.append(x)
        basic_list.append(x)
    
    print_list(empty_list)
    print(space_variable)
    
    print_list(basic_list)
    print(space_variable)

    print_list(empty_list2)
    print(space_variable)

    for x in range(5):
        basic_list.remove(x)

    print_list(basic_list)
    print(space_variable)

    