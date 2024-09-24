import random


def main():
    numList = list(range(100))
    random.shuffle(numList)
    result1 = binarySearch(numList, 4)
    result2 = linearSearch(numList, 4)
    print(result1, result2)


def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    main()
