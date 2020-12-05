"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        # Generate hash
        hash = self.calculate_hash_value(string)
        # Check whether generated hash is valid
        if hash != -1:
            self.table[hash] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""

        # Generate hash
        hash = self.calculate_hash_value(string)

        # Check whether generated hash is valid
        if hash != -1:
            output = self.table[hash]
            # Return the result if exist
            if output is not None:
                return hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Check whther input is empty
        if len(string) != 0:
            # Generate hash by multiplying first character with 100 and
            # add second character
            first_char = string[0]
            second_char = string[1]
            hash = ord(first_char) * 100 + ord(second_char)
            return hash
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
