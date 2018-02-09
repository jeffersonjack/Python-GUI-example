import pickle

users = {}
usersPath = "users.dat"

# Load the users dictionary from disk
def loadUsers():
    try:
        usersFile = open(usersPath, 'rb')
        users = pickle.load(usersFile)
        usersFile.close()
    except:
        # ignore errors, start with empty users dictionary
        pass


# Write the users dictionary to disk
def saveUsers():
    usersFile = open(usersPath, 'wb')
    pickle.dump(users, usersFile)
    usersFile.close()

    
# Add a user with a given username and password.
# Return values:
#  * 0 success
#  * 1 user already exists
def addUser(username, password):
    # check if the user already exists
    if username in users:
        return 1

    users[username] = password
    
    # success
    return 0


# Remove the specified user if the password is correct.
# Return values:
#  * 0 user removed
#  * 1 username not found
#  * 2 incorrect password
def removeUser(username, password):
    if username not in users:
        return 1

    if users[username] == password:
        del users[username]
        return 0
    else:
        return 2


def verify(username, password):
    if username in users:
        if users[username] == password:
            return 0
    return 1
