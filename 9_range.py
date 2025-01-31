for i in range(5):
    print(i)

# end point never be a part in values
# sample range(5); print 0,1,2,3,4
# second sample range(3); print 0,1,2

# === IMPORTANT ===
# range function can be 3 argument
# range(start, stop, step)

# range with start and stop
print(list(range(5, 10))) # output [5, 6, 7, 8, 9]

# range with start, stop and positive step. 
print(list(range(0, 10, 3))) # output [0, 3, 6, 9]

# range with start, stop and negative step.
print(list(range(-10, -100, -30))) # output [-10, -40, -70]

# to iterate indices of a sequence, you can combine range() and len()
userList = ['Mary', 'Juan', 'Tamara', 'Ben']

for i in range(len(userList)):
    print(i, userList[i])