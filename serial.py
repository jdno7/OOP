"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self, start):
        '''setting start to number passed in + initating a currnent number 1 less than start'''
        self.start = start
        self.current = start - 1

    def generate (self):
        '''adding one and returning the current number'''
        self.current += 1
        return self.current 

    def reset (self):
        '''resettin the current number to the start number '''
        self.current = self.start
        return self.current

