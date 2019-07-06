# creating a class to increase a value by an increment
class CountFromBy:
    # dunder init method for initailization of value and increment
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
        
    # increase method to add increment to value
    def increase(self) -> None:
        self.val += self.incr

    # convert interger value of val to string
    def __repr__(self) -> str:
        return str(self.val)

