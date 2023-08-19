"""
Python provides 2 important features to handle any unexpected errors and to add debugging capabilities to them
    1. Exception Handling: like other kinds of exceptions in Java
   -- The syntax of handling exceptions in Python:
        try:
            ...
        except Exception_type (as e1):
            ...
        except Exception_type (as e2):
            ...
        else:
            If there are no exceptions in the try-except block, execute this block

    -- NOTE: We can use "except" with:   1, NO exception types, just except itself (except:)
                                         2, Multiple exceptions (except Exception1, Exception2, Exception3,...)

    -- try-finally block: Like in Java, what inside finally block will ALWAYS be executed no matter what

    -- When working with open and close files, there's another way to make our code more clean and clear. That is to use
     "with" statement, which ensures that we never leave any resources open. For more details, see tutorial17_file_io.py

    -- Argument of an exception:
            try:
                ...
            except Exception_type, Argument:
                we can print value of Argument here

    -- Raising Exceptions: is kinds like throws exceptions in Java
            raise [Exception, [args, [traceback]
            ->> Exception: type of the exception
                args: (optional) is the value for exception argument
                traceback: (optional)


    2. Assertion: is basically a solid check if we can turn on or turn off when we're done with our testing of our prog
                Assertions are often placed at the start of the function to check for valid input and after the function
                call to check for valid output
                Syntax:     assert Expression(args)

                When encounter "assert" keyword, Python evaluates all the accompanying expressions, which is hopfully
                true. If it's false, Python raises AssertionError

`Exception` is the base class for all exceptions

"""


def kevin_to_fahrenheit(temp):
    """
    This function is to transfer Kevin temp to Fahrenheit temp and the func only takes non-negative inputs
    Therefore, we have to use assert keyword to make sure that no negative inputs are used
    :param temp:
    :return:
    """
    assert (temp >= 0), "Colder than absolute zero"     # This is to make sure that the input temp is not negative
    return ((temp-273)*1.8)+32


def write_into_a_file(file_name):
    """
    This function demos the use of handling exceptions using try-except-else block
    :param file_name:
    :return:
    """
    try:
        file = open("foo.txt", "r")
        file.write("This is a test of exceptions")
    except IOError:
        print("Error: Can't find file or read data")
    else:   # This will be executed if there are no exceptions caught within the try block
        print("Written content in the file successfully")


def get_level(level):
    """
    This demos the use of raise statement
    :param level:
    :return:
    """
    if level < 1:
        raise "Invalid level!"(level)
        # The code below to this would not be executed if we raise an exception


if __name__ == '__main__':
    print(kevin_to_fahrenheit(273))
    print(int(kevin_to_fahrenheit(505.23)))
    # print(kevin_to_fahrenheit(-3))  ->> AssertionError: Colder than absolute zero

    # This is a short demo of try-except block
    write_into_a_file("foo.txt")    # Error: Can't find file or read data

    """
    This is the practice from Cau's Github
    """

    # To catch all the exceptions, but don't specify any types of exceptions after the word "except"
    # This demos the use of except with no exception types
    try:
        file = open("foo.txt", "r")     # open a file but for read-only
        file.write("Hello, it's Van")   # then try to write sth into the file
    except:     # NO specific exceptions here, so it will catch all types of exceptions
        print("Some IOError occurred")
    else:
        print("Wrote something to the file")
    finally:
        print("This is executed no matter what, like finally block in Java")
        file.close()

    # Use arguments of exceptions. This is to assign an exception to a var for later use
    try:
        file = open("foo.txt", "r")
        file.write("Hello, it's Van")
    except IOError as err:
        print("Some IOError occurred:")
        print(err)
    finally:
        file.close()

    # Raise an exception
    try:
        raise ValueError("Some invalid errors")
    except ValueError as err:
        print(err)  # Some invalid errors

