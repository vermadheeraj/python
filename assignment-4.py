
                #ANSWER ------- 1

def commonElements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = commonElements(arr1, arr2, arr3)
print(result)  # Output: [1, 5]





                #ANSWER ------- 2



def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    return [diff1, diff2]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)  # Output: [[1, 3], [4, 6]]



                 #ANSWER ------- 3


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transpose.append(transposed_row)

    return transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]




                #ANSWER --------- 4



def arrayPairSum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i + 1])

    return max_sum

nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)  # Output: 4





                #ANSWER --------- 5




def arrangeCoins(n):
    left, right = 1, n

    while left <= right:
        midpoint = (left + right) // 2
        coins_needed = (midpoint * (midpoint + 1)) // 2

        if coins_needed > n:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return right

n = 5
result = arrangeCoins(n)
print(result)  # Output: 2





            #ANSWER ---------- 6



def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result

nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]





            #ANSWER ---------- 7


def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)  # Output: 4




            #ANSWER ---------- 8


def shuffle(nums, n):
    x = nums[:n]
    y = nums[n:]
    result = []

    for i in range(n):
        result.append(x[i])
        result.append(y[i])

    return result

nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)  # Output: [2, 3, 5, 4, 1, 7]















