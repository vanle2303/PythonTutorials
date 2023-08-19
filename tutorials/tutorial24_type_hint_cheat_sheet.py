if __name__ == '__main__':
    def sum(x: int, y: int) -> int:
        """
        This declaration means that func sum takes 2 params of type int and return an int result
        """
        return x+y

    # Positional and keyword arguments
    def quux(x: int, /, *, y: int) -> None:
        """
        Anything before / must be positional args
        Anything after * must be keyword args
        """
        pass    # Like in Java, using "abstract" to create a method with no bodies
        #        In Python, we use "pass" to notify a func with no bodies, but we still can add code to it later

    quux(3, y=5)   # OK
    # quux(2, 4)     # error: too many positional args
    # quux(x=1, y=6) # unexpected keyword args x

    # Use keyword "any" to allow arbitrary types
    class A:
        def __setattr__(self, key: int, value: any):
            pass


