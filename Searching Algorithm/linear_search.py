def linear_search(L, x):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1



if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(linear_search(L, 5))