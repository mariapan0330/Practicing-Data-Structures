"""
takes array of nums
return true if any number is even, otherwise false

in 3 ways:
1: anything
2: no built-in functions
3: no for loop
"""

nums = [1,4,5,5,3,7]
nums1 = [1,5,5,3,7]
nums2 = [2,3,5,5,3,7]

def even_detector1(nums):
    # ANYTHING
    # for each number, if it is even, return true
    for x in nums:
        if x % 2 == 0:
            return True
    return False

print(even_detector1(nums))
print(even_detector1(nums1))


def even_detector2(nums):
    # return True if length of this list with only the odds equals the length of the original list
    return len([x for x in nums if x % 2 != 0]) != len(nums)

print(even_detector2(nums))
print(even_detector2(nums1))
print(even_detector2(nums2))


# time: O(n) if n is length of nums
def even_detector3(nums):
    # plan: while there's still something in the list,
    # remove the last element if it's even
    if len(nums) == 0:
        return False
    
    curr = nums.pop()

    if curr % 2 == 0:
        # print('found one')
        return True
    else:
        # print(nums)
        return even_detector3(nums)


print(even_detector3(nums))
print(even_detector3(nums1))
print(even_detector3(nums2))