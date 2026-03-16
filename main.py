# Import section 
# example pull from file : from file_name import script/module
from tested_functions import *

import sqlite3
import bcrypt

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

    bankdatabase.Add_user("phillip", "password")
    # bankdatabase.update_user("phillip Miller", "new_password_again", 3)
    # bankdatabase.remove_user(13)
    # Password tests using hash
    # bankdatabase.verify_account_pass(1, "password")
    # bankdatabase.verify_account_pass(1, "password2")
    # bankdatabase.update_userpassword("password2", 4)
    # bankdatabase.update_username("Phillip 2", "password2", 4)
    
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


def login(bankdatabase):
    account = input("Account Number : ")
    password = input("Password : ")
    bankdatabase.user_info(account, password)

if __name__ == "__main__":
    # Used to execute code only when the file is run as a standalone script
    # Main entry point block
    main()

