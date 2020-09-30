#Module handles user input to create custom lists of handles for queries
def getCustomList():
    output = []
    print("Let's create a custom List to Search")
    while True:
        handle = input("Enter a Twitter handle for your list! (Enter 0 if you're done)")
        if handle == "0":
            return output
        else:
            if handle[0] != "@":
               handle = "@" + handle
            output.append(handle)
