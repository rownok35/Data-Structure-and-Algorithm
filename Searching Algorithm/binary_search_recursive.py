def binary_search_recursive(L, left, right, item):

    if left > right:
        return -1

    mid = (left + right) // 2
    if L[mid] == item:
        return mid
    
    if L[mid] < item:
        return binary_search_recursive(L, mid+1, right, item)
    else:
        return binary_search_recursive(L, left, mid-1, item)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    left = 0
    right = len(L) - 1

    print(binary_search_recursive(L, left, right, 5))

