# Phils Notes and Thoughts

- [Thread Processing](#processing-data-from-thread)
    - [March 13 - Script Output](#march-13---script-output)
- [Lists](#python-list)
    - [Adding Elements to list](#adding-elements-to-a-list)
        - [End of a list](#end-of-a-list)
        - [All elements from one list to another](#all-elements-from-one-list-to-another)
        - [Adding element at a specific location](#adding-element-at-a-specific-location)
    - [Removing Elements from a list](#removing-elements-from-a-list)
    



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


