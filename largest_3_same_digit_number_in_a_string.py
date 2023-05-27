"""
https://leetcode.com/problems/largest-3-same-digit-number-in-string/

You are given a string num representing a large integer. 
An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

and a strictly greater element appear in nums.
"""

def largest_3_digits(nums):
    # plan:
    # check through each 3 digits and see if valid
    # if valid, compare to current highscore (if larger, make it the highscore)
    result = ""

    for i in range(len(nums)-2):
        window = nums[i] + nums[i+1] + nums[i+2]
        if window[0] == window[1] == window[2]:
            if window > result:
                result = window
    return result

nums = "6777133339" # 777 and 333 are valid, but 777 is longer
nums2 = "2300019"
nums3 = "44423523388"
print(largest_3_digits(nums))
print(largest_3_digits(nums2))
print(largest_3_digits(nums3))