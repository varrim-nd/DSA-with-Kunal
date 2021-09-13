class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i%2 == 0]
        odd = [i for i in nums if i%2 != 0] 
        
        even.extend(odd)
        return even
