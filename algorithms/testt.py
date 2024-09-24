import random


def main():
    numList = list(range(100))
    random.shuffle(numList)
    numList = customSort(numList)
    print(numList)


def customSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftSide = arr[:mid]
    rightSide = arr[mid:]
    sortedLeft = customSort(leftSide)
    sortedRight = customSort(rightSide)
    return merge(sortedLeft, sortedRight)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    main()
