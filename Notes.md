# Phils Notes and Thoughts
[Thread Processing](#processing-data-from-thread)


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

