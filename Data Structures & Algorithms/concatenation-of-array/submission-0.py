class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if nums ==[]:
            return []
        else :
            nums=nums+nums
            return nums