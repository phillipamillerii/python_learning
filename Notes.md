# Phils Notes and Thoughts

- [Thread Processing](#processing-data-from-thread)
    - [March 13 - Script Output](#march-13---script-output)
- [Lists](#python-list)
    - [Adding Elements to list](#adding-elements-to-a-list)
        - [End of a list](#end-of-a-list)
        - [All elements from one list to another](#all-elements-from-one-list-to-another)
        - [Adding element at a specific location](#adding-element-at-a-specific-location)
    - [Removing Elements from a list](#removing-elements-from-a-list)
- [Project Idea - ATM](#project-idea---atm)

    



## Processing Data from Thread


    def thread_data_pull():
        def my_task(name, duration, queury):
            print(f"Thread {name} starting.")
            queury.put("Start Data From Thread")

            time.sleep(duration)

            # Setting new Data in the thread
            queury.put("New Data From Thread")
            queury.put("Finished Data From Thread")
            print(f"Thread {name} finished.")

        q = queue.Queue()
        t = threading.Thread(target=my_task, args=("Test", 2, q))   
        t.start()
        
        # Reporting data from thread
        print("test : " + q.get())
        t.join()

        # Print the available queries after the thread is dead
        for _ in range(2):
            print(q.get())

        print("Thread data pull complete")

Using this was I able to verify that when data is put into a queue it will stay in there even after new data is added. 

ie. If the thread adds 3 detils to the queue they all will remain after the thread has completed. 

However these details can only be accessed once and then they are automatically removed. If one detail is "get" from the queue it needs to be added to another variable outside of the thread it retain it... 
    
    I wonder if there is a way to get a length of a queue before attempting to pull the data from it? 

Going over the [documentation for the queue module](https://docs.python.org/3/library/queue.html). From there I found the below, which looks to provice me the size of the queue. 

    Queue.qsize() 

    Return the approximate size of the queue. Note, qsize() > 0 doesn’t guarantee that a subsequent get() will not block, nor will qsize() < maxsize guarantee that put() will not block.


Using that I can set a more specific print process
    
    # Print the available queries after the thread is dead
    for _ in range(q.qsize()):
        print(q.get())


### March 13 - script output
    Called Main  Function Successfully
    -----------------------------------------------
    what do you want to input? : phillip
    user input >> phillip
    -----------------------------------------------
    Random Array >>
    array('i', [0, 5, 9, 7, 2])
    Array output:
    0
    5
    9
    7
    2
    -----------------------------------------------
    input a integer : 1
    1
    -----------------------------------------------
    Thread A starting.
    Thread B starting.
    Thread B finished.
    Thread A finished.
    All threads finished.
    -----------------------------------------------
    Thread C starting.
    Thread C finished.
    Thread Dead
    thread_status_test Complete
    -----------------------------------------------
    Thread Test starting.
    test : Start Data From Thread
    Thread Test finished.
    2
    New Data From Thread
    Finished Data From Thread
    Thread data pull complete
    -----------------------------------------------
    Completed Main

Next I'm trying to learn more about lists, dictionaries, sets, and tuples. 

## Python list

[Python list Docs](https://docs.python.org/3/tutorial/datastructures.html)

### Adding elements to a list 

#### End of a list
    
    list_name.append(Adding_element)

#### All elements from one list to another
Adding all elements from one list to another. Requires any type of iterable (list, set, tuple, etc.) in place of the old_list_name

    list_name.extend(old_list_name)

#### Adding element at a specific location 

    list_name.insert(Number_location, Data_adding)


Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

### Removing Elements from a list

    list_name.remove(x)

Remove the first item from the list whose value is equal to x. It will return an error if the value doesn't exist.

## Project Idea - ATM
I started thinking about what ways I might be able to create something that is useful. So I'm going to try and create some kind of an ATM. 

Elements I need: 
- User Interface (UI): A graphical interface (typically JTextArea/JPanels in simulations) managing menu navigation, transaction prompts, and error messages.
    - Authentication Module: Secure input and validation of PINs and card data.
- Functional Transactions:
    - Withdrawals: Communicates with cash dispensers and deducts funds.
    - Deposits: Processes check or cash deposits.
    - Balance Inquiries: Queries the bank database for real-time account balances.
    - Transfers: Moves funds between connected accounts.
- Networking & Backend: Connects the ATM to the bank's core banking system to securely transmit data and authorize transactions.
- Hardware Interface Layer: Software controlling the card reader, keypad, receipt printer, and cash dispenser.
- Logging & Security: Logs transaction logs for auditing and compliance, ensures end-to-end encryption, and manages session timeouts. 

### Progress - 3.15.26
- Created a basic database
    - using sqlite3
    - Contains
        - Account number
            - Auto incremented number, may want to try something else for creating the account number as it currently starts a 1 and goes up from there
        - user_name
            - User provided and doesn't verify there isn't already an Account with the same user_name
            - Currently not being used for loging in, for that we are using the Account number
        - user_password
            - for this I implamented a hash process using bcrypt, so we are saving the hash in the database
                - May want to look into secure hashing methods
        - created_at
            - this using a sql CURRENT_TIMESTAMP when the user is added to the database
        - last_updated
            - For this I'm just updating the timestamp manually when we are updating the users information
                - May want to look into triggers, I attempted this and I wasn't able to get something working
    - Needs
        - account types
            - Banks have different types of accounts, so it mmaybe a good idea to set those
                - Although I'm not sure what the best option would be to allow for an account to have multiple account types ( saving, credit, CD, etc. )  
        - Permissions
            - For users and admins
        