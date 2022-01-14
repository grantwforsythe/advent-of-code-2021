from typing import List


def load_data() -> List:
    """ 
    load the input data
    """
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data