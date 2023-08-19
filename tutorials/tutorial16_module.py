if __name__ == '__main__':
    """
    A module is simply a Python file, in which a bunch of functions, classes or variables are defined
    The name of the module is the name of th Python file, like "time" for time.py
    
    You can import a module or import specific functions from it as follows:
        import time
        from time import asctime
    
    You can also import all names from a module:
        from time import *
    
    When you import a module, the Python interpreter searches for the module in the following sequences:
        1. The current directory
        2. If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH
        3. If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
        
    The module search path is stored un tge system module sys as the sys.path variable
    The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default
    
    The PYTHONPATH Variable
    The PYTHONPATH is an environment variable, consisting of a list of directories
    The syntax of PYTHONPATH is the same as that of the shell varibale Path
    set PYTHONPATH = /usr/local/lib/python
    
    Read abt "Packages un Python" section here: https://www.tutorialspoint.com/python/python_modules.htm
    It explains the _init.py_ file, which is to combine other smaller modules into a parent module 
    In a nutshell: (Noi tom gon la)
    Assume we have a dir named "math"
    Under this dir, there are 3 files: trug.py, numeric.py and geometry.py, each with some functions:
        math
            trig.py with func cosine(x)
            numeric.py with func factorial(x)
            geometry.py with func area(x, y)
    Now we need ti combine all these sub-modules trug, numeric and geometry into a single math module
    Under math dir, create _inti.py_, in which put the following:
        from trig import cosine
        from numeric import factorial
        from geometry import area
    Now all those functions become member of math module
    In other Python file, we can import math as follows:
        import math
    or
        from math import cosine    
            
        
    
            
        
    """