import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    obj = np.array(nums, dtype=object)

    mask3 = nums % 3 == 0
    mask5 = nums % 5 == 0

    obj[mask3] = "fizz"
    obj[mask5] = "buzz"
    obj[mask3 & mask5] = "fizzbuzz"

    return obj
