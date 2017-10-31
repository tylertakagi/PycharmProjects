
# The Dynamic Array Class
# Python has all kinds of powerful stuff that does what your dynamic array needs to do
# No, you CAN'T use any of that
class DynamicArray(object):

    INIT_CAPACITY = 2^4
    RESIZE_MULTIPLIER = 2

    # The __init__ function is run when you instantiate an instance of this object
    def __init__(self):

        # variables beginning with the underscore can denote internal or self referential data
        # That isn't strictly enforced, but merely a nice convention for readability
        self._size = 0
        self._capacity = DynamicArray.INIT_CAPACITY
        self._data = [None] * self._capacity

    #################################
    ## DO YOUR WORK BELOW THIS LINE #
    #################################

    # Return the size of the dynamic array
    def size(self):
        return self._size

    # Return the capacity of the dynamic array
    def capacity(self):
        return self._capacity


    # Add an element to the end of the dynamic array
    def add(self, value):
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = value
        self._size += 1

    # Get the value at the position passed in as a parameter
    def get(self, pos):
        return self._data[pos]

    # Put a value into the dynamic array at the specified position, overwriting what was there
    def put(self, pos, value):
        self._data[pos] = value

    # Swap 2 specified values in the dynamic array
    def swap(self, pos1, pos2):
        pos1_val = self._data[pos1]
        pos2_val = self._data[pos2]
        self._data[pos1] = pos2_val
        self._data[pos2] = pos1_val

    # Remove a value from the dynamic array (and return it)
    def remove(self, pos):
        remove = self._data[pos]

        for i in range(pos, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1
        return remove

    # Resize the underlying array to make room
    def _resize(self):
        self._capacity *= DynamicArray.RESIZE_MULTIPLIER
        temp = [None] * self._capacity
        for i in range(0, self._size):
            temp[i] = self._data[i]
        del self._data
        self._data = temp

    # DO NOT MODIFY THIS PRINT
    # Print the data in a useful way
    def print_data(self):
        print "[ %s ]" % ' | '.join([str(v) for v in self._data])