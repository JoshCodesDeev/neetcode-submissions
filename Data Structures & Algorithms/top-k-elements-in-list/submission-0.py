class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash =  {}
        
        for num in nums:
            if num not in hash:
                hash[num] = 0
            hash[num] += 1

        result = []

        for key, val in hash.items():
            result.append([key, val])

        result = sorted(result, key=lambda x: x[1])
        result = result[len(result)-k: len(result)]

        output = []
        for item in result:
            output.append(item[0])
        
        return output



