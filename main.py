# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *

import sqlite3


# Global Variables - output spacing 
space_variable = "-----------------------------------------------"
db_file = './data/bank.sqlite'

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
    list_tests()
    """

    bankdatabase = database()

    # bankdatabase.Add_user("phillip", "super_new_password_again")
    # bankdatabase.update_user("phillip Miller", "new_password_again", 3)
    bankdatabase.remove_user(13)
    bankdatabase.close()

    print("Completed Main")
    print(space_variable)

class database:
    def __init__(self):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS Users(
                Account INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_name VARCHAR, 
                user_password VARCHAR, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                last_access TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        
        self.cur.execute(create_table_query)
    
    def Add_user(self, username, password):
        create_users_query = """
            INSERT INTO Users (
            user_name = ?, 
            user_password = ?
            ) 
        """
        self.cur.execute("INSERT INTO Users (user_name, user_password) values (?, ?)", (username, password))
        self.conn.commit()

    def update_user(self, username, password, account):
        try:
            
            update_query = """
                UPDATE Users 
                SET user_name = ?, user_password = ?, last_access = CURRENT_TIMESTAMP
                WHERE Account = ?
                """
            self.cur.execute(update_query, (username, password, account))

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        
        finally:
            if self.conn:
                self.conn.commit()
    def remove_user(self, account):
        delete_query = """
            DELETE FROM Users
            WHERE Account = ?
        """
        self.cur.execute(delete_query, (account,))

    def close(self):
        self.conn.commit()










if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

