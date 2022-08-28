class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # If this method is not implemented, then == compares the memory addresses of the two objects by default
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
