class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        char = sorted(nums)
        n=len(char)
        for i in range(1,n):
            if char[i]==char[i-1]:
                return True

        return False               
        


