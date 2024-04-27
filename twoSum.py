'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly 
one solution, and you may not use the same element twice.
'''

def twoSum(nums, target):
    org_arr = nums[:]
    nums.sort()
    print(nums)
    start = 0
    end = len(nums) -1
    result = []
    while(start < end):
        if(nums[start] + nums[end] == target):
            #this condition is for duplicate array element
            # print(nums[start] , nums[end])
            start_index = start_index = org_arr.index(nums[start])
            end_index = -1
            for i in range(0, len(nums)):
                if(nums[end] == org_arr[i] and i != start_index):
                    end_index = i
            
            
            print(start_index)
            result.append(start_index)
            result.append(end_index)
            return result
        if(nums[start] + nums[end] < target):
            start = start + 1   
        if(nums[start] + nums[end] > target):
            end = end - 1       


print(twoSum([-1,-2,-3,-4,-5], -8))          
