words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# !!! IMPORTANT !!!:
# copy collection or create new collection if you want modified collection in iteration

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# create copy from users and iterate the copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users) # output {'Hans': 'active', '景太郎': 'active'}

# or create new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
