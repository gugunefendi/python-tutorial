# Asynchronus is a programming concept that a process can be execute task with out waiting other task finish early
# in other words asynchronus can be execute more than one task in same time

# The opposite of asynchronus is synchronus
# SYNCHRONUS
# synchronus will execute task one by one
# synchronus must wait other task finish and than excute next task
# synchronus can make application slow

# ASYNCHRONUS
# asynchronus can execute some tasks in same time
# asynchronus no need to wait, program can be execute other task
# asynchronus can make application more responsive


# example code with synchronus
import time # add time

def main():
    greeting("Good morning", 3)
    greeting("Good afternoon", 2)
    greeting("Good night", 1)

def greeting(message, time):
    print(f"{message}, \t: {time} second")

main()


# example code with asynchronus
import asyncio

async def second_main():
    greeting1 = asyncio.create_task(second_greeting("Good morning", 3))
    greeting2 = asyncio.create_task(second_greeting("Good afternoon", 2))
    greeting3 = asyncio.create_task(second_greeting("Good night", 1))

    await greeting1
    await greeting2
    await greeting3

    print(f"Greeting is done!")

async def second_greeting(message, time):
    print(f"Process {message}")
    await asyncio.sleep(time)
    print(f"Done {message} \t: {time} second")

asyncio.run(second_main())
