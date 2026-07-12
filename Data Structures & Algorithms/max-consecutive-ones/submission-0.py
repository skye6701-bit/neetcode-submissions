class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        reg=[]
        for i in range(len(nums)):
            if nums[i]==1:
                cnt=cnt+1
                reg.append(cnt)
            else:
                cnt=0
                reg.append(cnt)
        answer=max(reg)
        return answer
                

