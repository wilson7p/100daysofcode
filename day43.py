#Write a program that uses multithreading to perform tasks concurrently.
print ("\nWilson - Day 43 of #100DaysOfCode\n") 
print("\nprogram that uses multithreading to perform tasks concurrently\n")

import threading

def print_message_with_thread_id(message):
    thread_id = threading.current_thread().name
    print(f"thread {thread_id}: {message}")

messages = ["hi", "hello", "everyone", "welcome", "to", "wills", "gaming", "guys"]

threads = []

for message in messages:
    thread = threading.Thread(target=print_message_with_thread_id, args=(message,), name=message)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all threads have finished.")

