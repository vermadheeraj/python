

           #ANSWER-------1



def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return target

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            else:
                right -= 1

    return closestSum

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))




            #ANSWER-------2





def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]

                if currentSum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))



      #ANSWER-------3






def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
       
        nums[i], nums[j] = nums[j], nums[i]


    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

nums = [1, 2, 3]
print(nextPermutation(nums))




             #ANSWER-----4



def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2




            #ASNWER------5






def plusOne(digits):
    carry = 1
    n = len(digits)

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

        if carry == 0:
            break

    if carry == 1:
        digits.insert(0, carry)

    return digits

digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]





            #ANSWER------6






def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


nums = [2, 2, 1]
print(singleNumber(nums))



        #ANSWER------7





def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            if start == num - 1:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(num - 1))
            start = num + 1

    if start <= upper:
        if start == upper:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(upper))

    return result

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))





        #ANSWER-----8


def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))  # Output: False














