

# def MCM(arr, n):
import itertools
n = [1, 2, 3, 4, 5]
n = n[::-1]
l = itertools.accumulate(n)
print(list(l))
