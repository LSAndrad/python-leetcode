'''
Padrão: range(len(nums2) - 1, -1, -1)
range(start, stop, step)

start: onde começa (inclusivo)
stop: onde para (exclusivo)
step: quanto pula a cada iteração
'''


def nextGreaterElementOne(nums1,nums2):

    next_greater= {}
    stack =[]
    
    for num in nums2:
        #pop elementos menores
        #precisa ter elementos na lista -> verifica se o último elemento da lista é menor do que o que está vindo
        while stack and stack[-1]<num:
            # como é menor do que está vindo, tiro ele do stack, e adiciono ele e o maior ao dict next_greater
            smaller=stack.pop()
            next_greater[smaller] = num
        stack.append(num)
        print("stack:",stack)
        print("next_greater", next_greater)
        
    result = []
    for num in nums1:
        result.append(next_greater.get(num,-1))
    return result
nums1= [4,1,2]
nums2 = [7,3,1,2]

print(nextGreaterElementOne(nums1,nums2))

#output: [-1]

#não posso dar um sort?
# procura o elemento de nums1 em nums2
#se achar e não for o maior, retorna o próximo, senão retorna -1