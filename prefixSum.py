class NumArray:

    def __init__(self,nums):
        # consutruir um array de prefix:
        self.prefix = [0]
        for num in nums: 
            self.prefix.append(self.prefix[-1] + num)
        #prefix[1] = soma até o elemento 0
        #prefix[2] = soma até o elemento 1
    
    def sumRange(self,left,right):

        # inclui o da direita
        # subtrai por tudo antes da esquerda
        return self.prefix[right+1] - self.prefix[left] 

obj = NumArray([1,2,3,4,5])
print(obj.sumRange(1,3))
