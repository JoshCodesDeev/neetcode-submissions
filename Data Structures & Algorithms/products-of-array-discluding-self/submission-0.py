class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0 for _ in range(len(nums))]

        curr = 1
        for num in nums:
            curr *= num
            prefix.append(curr)

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            curr *= nums[i]
            suffix[i] = curr
        
        result = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            prev = 1
            post = 1
            if i == 0:
                prev = 1
            else: 
                prev = prefix[i - 1]

            if i == len(nums) - 1:
                post = 1
            else:
                post = suffix[i+1]

            result[i] = prev * post
        
        return result


