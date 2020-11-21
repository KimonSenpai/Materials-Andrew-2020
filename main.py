# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random as rd
f = open("input.txt", 'r')
n = int(f.readline())
arr = [int(v) for v in f.readline().split()]
print(n, arr)
f2 = open("output.txt", 'w')
f2.write(''.join([['X', 'Y', 'Z'][rd.randint(0,2)] for _ in range(10**6)]))
