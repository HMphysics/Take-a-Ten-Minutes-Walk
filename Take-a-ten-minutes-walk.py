# We introduce a string in the function.
def is_valid_walk(walk):

    # If the list is longer than 10 or shorter than 10 it takes you more or less than 10 minutes.
    # So it will return 'False'.
    if len(walk) > 10 or len(walk) < 10:

        return False

    # If the number of north positions is different to the south positions and the same with east and west
    # it's obvious you won't finish in the same place where you started.
    # So it will return 'False'.
    elif walk.count('n') != walk.count('s') or walk.count('e') != walk.count('w'):

        return False

    # Rest will return 'True'.
    else:

        return True
