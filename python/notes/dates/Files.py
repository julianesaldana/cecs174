"""
FILES
# to access a file, you must open
    infile = open("input.txt", "r")
    # file has to be located in the same directory as the program
    # the file must exist (and be accessible) otherwise, exception occurs
# to write on a file
    outfile = open("input.txt", "w")
    # if the output file already exists, it overwrites the contents of the output file.
    # if the file doesn't exist, it creates it
# closing file
    infile.close()
    outfile.close()
    # you must close the file after you open if you want to iterate again
# reading
    line = infile.read()
        # read entire file and returns a string
    lines = infile.readlines()
        # read a line of text from the file
    # if the file contains numerical data, int() conversion is required
    # last character of each line is "\n"
# writing
    outfile = open("output.txt", "w")
    # or
    outfile.write("Hello!")
    # you must write "\n" to start a new line
    output.write("Hello!\nWhat's going on>")
# read words
    for line in in_file:
        line = line.rstrip.split()
        print(line)
    # use read(), split(), strip(), must remove "\n"
    line = infile.readline()
    while line != "":
        print(line)
# character strip methods/examples
# reading records
    # a text file can contain a collection of data records in which each record consists of multiple fields
    # when working with text files that contain data records:
        # you must know the data structure
        # read the entire record before you can process it
# with statement
    with open(filename, "r") as infile:
        print(infile.readline())
    # with opens the file with the given name and closes the file when the
      end of the statement has been reached or an exception is raised.)
"""

