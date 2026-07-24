class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            if i!="C" and i!="+" and i!="D" :
                score.append(int(i))
            elif i=="C":
                score.pop()
            elif i=="D":
                score.append(2*score[-1]) 
            elif i=="+":
                score.append(score[-1]+score[-2])
        summation=0
        for i in score:
            summation=summation+i
        return summation                      