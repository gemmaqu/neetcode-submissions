class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(0,len(operations),1):
            if operations[i]== '+' :
                record.append(record[-1]+record[-2]) 
            elif operations[i]== 'D' :
                record.append(record[-1]*2)
            elif operations[i]== 'C' :
                record.pop()
            else:
                num = operations[i]
                intnum = int(num)
                record.append(intnum)
        total_sum = sum(record)

        return total_sum #or directly return sum(record)


#notes:
#we dont want to use operations becasue it has signs such as + and -
#pop() removes the last elemnet in the list
#listneam[-1] gets the last elemnt    
#sum() calculate the sum automatically    