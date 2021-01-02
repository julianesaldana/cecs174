"""
DICTIONARIES:
# a container that keeps associations between keys and values
# can use any type of item
# enclosed in braces/brackets
    # key and value pair
#empty dictionary
# creating / duplicating dictionaries
    # completely new values
        contacts = {key:value}
        dupe_contacts = dict(contacts)
        # if you cahange the value of original contacts, it will NOT change dupe_contacts
    # using reference
        contacts = {key:value}
        new_contacts = contacts
        # if you change the value of the original contacts, it will change new_contacts
# accessing Dictionary values []
    #use [] to return the value associated with the key
    # dictionary is not a sequence type container like a list
        # cannot access the items byt index or position
# checking membership, default value
    # use in or not in operator
        if "john" in contacts:
            print("Johns number is", contacts["John"])
        else:
            print("John is not in my contact list")
    # dict.get(key, default)
# adding/modifying items
    dictionary[key] = value
# removing elements
    dictionary.pop(key)
    del dictionary(key)
# traversing a dictionary
    # can iterate over the individual keys in a dictionary using for loop
    # can iterate over the keys in order using sorted(dictionary)
    # using items()
        dictionary = {keys : values, keys : values}
        for key, value in dictionary.items():
            print("The keys = ", key, "The values = ", value)
        # makes dictionaries ideal for storing json data
        #replacing .items() with .getkeys() or .getvalues() gives you the keys only or values only, respectively
# a dictionary of lists
    # can store lists in dictionaries
# nested dictionary
    # can store a dictionary inside another dictionary
    dictionary = {}
    dictionary[key1] = {'key':'value', 'key2':'value2'}
    for key, value in dictonary.items():
        print(key, value)
        # prints key, value which is a dictionary
    for key, value in dictionary.items():
        print(value + ":")
        for key, value in value.items():
            print("\t", key, value)




"""