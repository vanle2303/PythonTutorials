def open_close_file(file_name):
    """
    Open a file
    Use open function:
        file object = open(file_name, [access_mode], buffering)

    file_name: (file_name argument) a string value containing the name of the file that we want to access
    access_mode: to determine the mode that the file has to be opened (read, write, append, etc.).
                This param is optional and has a default access mode of read(r)
    buffering: buffering value = 0, NO buffering takes place
               buffering value = 1, line buffering while accessing the file
               buffering value > 1, buffering action is performed with the indicated buffer size
               buffering value < 0, default behavior

    Close a file
        close function: flushes any unwritten info and close the file object, after which NO more writing can be done
            file_object.close()

    :param file_name:
    :return:
    """
    fo = open(file_name, "wb")  # wb is access mode - open a file for writing only in binary format
    print("Name of file: ", fo.name)  # Name of file:  foo.txt
    print("Closed or not: ", fo.closed)  # Closed or not:  False
    print("Opening mode: ", fo.mode)  # Opening mode:  wb
    fo.close()
    return


"""
Read and write files
    1. file_object.write(string)
        fo = open("foo.txt", "wb")
        fo.write( "Python is a great language.\nYeah its great!!\n")
        fo.close()

    2. file_object.read([count])
    Here we have to pass a param count to let Python know the number of bytes to be read from the opened file
        fo = open("foo.txt", "r+")
        str = fo.read(10);
        print "Read String is : ", str
        fo.close()   
"""


def file_position(fime_name):
    """
    File positions:
    1. tell(): tell the current position within the file. In other word, the next read or write will occur at that many
    bytes from the beginning of the file

    2. seek(offset [from]): method to change the current file position.
        offset: indicate the number of bytes to be moved
        from: specify the reference position from where the bytes are to be moved
            from = 0: use the beginning of the file as the reference position
            from = 1: use the current position as the reference position
            from = 2: the end of the file as the the reference position
    :param fime_name:
    :return:
    """
    # Open a file
    fo = open(fime_name, "r+")  # r+ is to open a file for both reading and writing
    str = fo.read(10)   # read the next 10 bytes
    print("Read String is: ", str)  # Read String is:

    # Check current position
    position = fo.tell()  # tell the current position within the file
    print("Current position:", position)  # Current position:  0

    # Repositioning pointer at the beginning once again
    position = fo.seek(0, 0)
    str = fo.read(10)
    print("Again read String is:", str)

    # Close the opened file
    fo.close()


"""
Rename and delete files
    1, rename(): takes 2 args, the current file-name and the new file-name
       Syntax: os.rename(current_file_name, new_file_name)
       E.g:     import os
                os.rename(text1.txt, text2.txt)

    2. remove(): delete a file, take the file-name as an arg 
       Syntax: os.remove(file_name)
       E.g:     import os
                os.remove(text2.txt)
"""

"""
Directories in Python                                                               Syntax
    1. mkdir(): create directories in the current dir                           os.mkdir("new_dir")
    2. chdir(): change the current directory. Take an arg of the new 
                directory name that we want to make the current dir             os.chdir("new_dir")
    3. getcwd(): display the current working dir                                os.getcwd()
    4. rmdir(): delete the dir                                                  os.delete("dir_name")
    
Working with directories in Python, we have to import module `os`, then we use os to call those dir functions
"""

"""
`WITH` STATEMENT: ENSURES THAT WE NEVER LEAVE ANY RESOURCES OPEN
This is used in exception handling to make code clearer and more readable. 
"with" statement ensures proper statements to be executed without throwing any bugs to the program
A bug in a piece of code may cause the whole program to stop and there should be a lot of statements of the prog that 
were not executed properly. Especially, when opening a file and the close statement is not executed. Then this is just 
a waste of the memory space

Right below we have 3 functions, providing 3 approaches to open a file
    1. open_file_without_with_statement_1(): a function to open a file without any try-catch block to handle exceptions
    2. open_file_without_with_statement_2(): this function has some improvements with try-catch block and finally statement
                                            to handle the potential exceptions. However, this approach is not perfectly
                                            compact(gon nhe, xuc tic) still contains so many steps with try_catch blocks
    3. open_file_using_with_statement(): this function takes care of all the exceptions, notice that there are NO calls
                                        to func close(). With "with" statement, our code is a lot more effective in 
                                        handling exceptions and also a lot more clean and clear
"""


def open_file_without_with_statement_1(file_name):
    file = open(file_name, "w")
    file.write("Hello World")
    file.close()
    return


def open_file_without_with_statement_2(file_name):
    file = open(file_name, "w")
    try:
        file.write("Hello World")
    finally:
        file.close()
    return


def open_file_using_with_statement(file_name):
    with open(file_name, "w") as file:
        file.write("Hello World")
    return


import os


if __name__ == '__main__':
    # Input function
    str = input("Entered input: ")  # Entered input: hello
    print("Received input: ", str)  # Received input:  hello

    open_close_file("foo.txt")

    file_position("foo.txt")

    print("Current dir:", os.getcwd())      # /Users/vanle/Desktop/Code/Python/PythonTutorials/tutorials






