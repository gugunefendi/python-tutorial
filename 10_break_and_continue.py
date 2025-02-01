# the break statement to stop iteration in for or while loop
for n in range(2, 10):
    if n == 5:
        print("Stop loop with break")
        break
    else:
        print(n)

# continue statement to continues iteration in loop
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Found an even number\t: {i} ")
        continue
    else:
        print(f"Found an odd number\t: {i}")