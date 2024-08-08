

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sizeA = len(a)
        sizeB = len(b)
        lista = [int(digit) for digit in a]
        listb = [int(digit) for digit in b]
        
        if(sizeA < sizeB):
            diff = sizeB - sizeA
            lista = [0]*diff + lista
        elif(sizeB < sizeA ):
            diff = sizeA - sizeB
            listb = [0]*diff + listb

        result = []
        carry = 0
        charToInsert =""
        for i in range(len(lista)-1,-1,-1):
            sum = lista[i] + listb[i] + carry
            if(sum == 2):
                carry = 1
                charToInsert = "0"
            elif(sum == 3):
                carry = 1
                charToInsert = "1"
            else:
                carry = 0
                charToInsert = str(sum)
            
            result.insert(0, charToInsert)
            
        
        if carry == 1:
            result.insert(0, "1")

        return ''.join(result)