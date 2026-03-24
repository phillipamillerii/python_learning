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
            logger.info('Call to input_number Function Successful')
            # Return the integer value if successful
            return integer_value
        except ValueError:
            # Handle the error if the conversion fails
            logger.warning('Call to input_number Function Failed')
            print(f"'{user_input}' is not a valid integer. Please try again.")

def threading_test():
    # Used for starting a thread that is just sleeping
    def my_task(name, duration):
        print(f'Thread {name} Starting')
        logger.info(f'Thread {name} Started')
        time.sleep(duration)
        print(f'Thread {name} Finished.')
        logger.info(f'Thread {name} Finished')
    
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
        logger.info(f'Thread {name} Started')
        time.sleep(duration)
        print(f"Thread {name} Finished.")
        logger.info(f'Thread {name} Finished')

    t3 = threading.Thread(target=my_task, args=("C", 2))
    t3.start()

    # Sleep process to make sure the thread has time to complete
    time.sleep(5)

    if t3.is_alive():
        print("Thread Alive")
    else:
        print("Thread Dead")
    logger.info(f'thread_status_test Complete')



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


class database:
    def __init__(self):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS Users(
                Account INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_name VARCHAR, 
                user_password BLOB NOT NULL,
                funds INTEGER, 
                currency_code VARCHAR,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                last_access TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        
        self.cur.execute(create_table_query)

    def hash_password(self, password):
        # Passwords must be encoded to bytes
        password_bytes = password.encode('utf-8')

        # bcrypt automatically generates a salt and includes it in the hash
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_bytes
    
    def Add_user(self, username, password):
        create_users_query = """
            INSERT INTO Users (
            user_name = ?, 
            user_password = ?,
            funds = 0,
            currency_code = "USD"
            ) 
        """
        hashed = self.hash_password(password)
        self.cur.execute("INSERT INTO Users (user_name, user_password, funds, currency_code) values (?, ?, 0, 'USD')", (username, hashed))
        self.conn.commit()
        logger.info('User Created')

    def update_userpassword(self, password, account):
        # May want to look into restricting this as it's not performing verifacation before updating the password
        hashed = self.hash_password(password)
        try:
            update_query = """
                UPDATE Users 
                SET user_password = ?, last_access = CURRENT_TIMESTAMP
                WHERE Account = ?
                """
            self.cur.execute(update_query, (hashed, account))

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        
        finally:
            print("Password Updated Successfully")
            if self.conn:
                self.conn.commit()

    def update_username(self, username, password, account):
        if self.verify_account_pass(account, password):
            try:
                update_query = """
                    UPDATE Users 
                    SET user_name = ?, last_access = CURRENT_TIMESTAMP
                    WHERE Account = ?
                    """
                self.cur.execute(update_query, (username, account))

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
            
            finally:
                print("Username Updated Successfully")
                if self.conn:
                    self.conn.commit()
        else:
            print("Update Username failed")
            return False

    def remove_user(self, account):
        delete_query = """
            DELETE FROM Users
            WHERE Account = ?
        """
        self.cur.execute(delete_query, (account,))

    def verify_account_pass(self, account, password):
        verify_query = """
            SELECT user_password 
            FROM Users 
            WHERE Account = ?
        """
        self.cur.execute(verify_query, (account,))
        result = self.cur.fetchone()
        if result:
            stored_hash = result[0]
            # Encode the entered password to bytes
            entered_password_bytes = password.encode('utf-8')
        
            # bcrypt.checkpw handles the comparison and salting automatically
            if bcrypt.checkpw(entered_password_bytes, stored_hash):
                print(f"Password match! Account : {account} - Login successful.")
                return True
            else:
                print("Incorrect Account/Password")
                return False
        else:
            print("Account not found.")
            return False
    
    def user_info(self, account, password):
        user_info_query = """
            SELECT * FROM Users WHERE Account = ?
        """
        if self.verify_account_pass(account, password):
            self.cur.execute(user_info_query, (account,))
            result = self.cur.fetchone()
            if result:
                print(result)
                return True
            else:
                print("Query Failed")
                return False
        else:
            print("Account/Password failed")
            return False
    
    def add_funds(self, account, password, funds):
        current_funds_query = """
            SELECT funds FROM Users WHERE Account = ? 
        """
        if self.verify_account_pass(account, password):
            current_funds = ""
            
    def close(self):
        self.conn.commit()
        self.conn.close()

