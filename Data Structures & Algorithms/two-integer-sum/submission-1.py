class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = []
        count = int
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                count = target - nums[i]
                if nums[j] == count and len(list1)<2:
                    list1.append(i)
                    list1.append(j)
                else:
                    continue
        return list1
