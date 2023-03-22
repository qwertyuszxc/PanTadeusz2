
def twoSum(nums, target):
    j = 1
    l = []
    while j != len(nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                j = 1 
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
                    return(l)
                
print(twoSum([3,2,4], 6))
                         
           