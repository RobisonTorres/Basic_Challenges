print('From Code Wars')
print()

def is_isogram(string):

    # This function determines if a string is or not a isogram.
    return True if len(set(string.lower())) == len(list(string.lower()))\
        else False

print(is_isogram('moOse'))  # Outputs - False
print(is_isogram('isogram'))  # Outputs - True
