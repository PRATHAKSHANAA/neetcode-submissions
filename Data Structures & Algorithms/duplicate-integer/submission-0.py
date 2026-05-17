class Solution:
    def hasDuplicate(self, num: List[int]) -> bool:
        for i in range (len(num)):
            for j in range (i+1,len(num)):
                if num[i] == num[j]:
                    return True
        return False