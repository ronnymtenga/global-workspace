import numpy as np
import some_functions as sf

class Calculator():
    def __init__(self):
        self.statement = []

    def calculate(self, equation):
        self.statement = sf.string_to_list(equation)
        self.ops = []
        self.nums = []
        for element in self.statement:
            if type(element) == int or type(element) == float : 
                self.nums.append(element)
            else: 
                self.ops.append(element)

        print(self.nums, self.ops)

        #bodmas is a list containing the order of precedence for each of the math operations in cal.ops while retaining their indexes 
        bodmas = np.array(sf.precedence_list1(self.ops)).tolist()
        #print(bodmas)

        p_order = 0
        while len(self.ops) > 0 :
            o = sf.finderr(bodmas, p_order)
            if o != -1: b = bodmas[o]  
            else: b = -1  
            
            #print(b, p_order,o)
            match b:
                case 0:
                    temp = self.nums[o]**self.nums[o+1]
                    self.nums.pop(o)
                    self.ops.pop(0)
                    bodmas.pop(o)
                    self.nums[o] = temp
                case 3:
                    temp = self.nums[o]+self.nums[o+1]
                    self.nums.pop(o)
                    self.ops.pop(o)
                    bodmas.pop(o)
                    self.nums[o] = temp
                    #print('added', self.ops, bodmas)

                case 4:
                    temp = self.nums[o]-self.nums[o+1]
                    self.nums.pop(o)
                    self.ops.pop(0)
                    bodmas.pop(o)
                    self.nums[o] = temp
                    #print('subtracted', self.ops, bodmas)

                case -1:
                    #print(p_order,o)
                    p_order = p_order + 1

                case 1:
                    temp = self.nums[o]/self.nums[o+1]
                    self.nums.pop(o)
                    self.ops.pop(0)
                    bodmas.pop(o)
                    self.nums[o] = temp
                    #print('division', self.ops, bodmas)

                case 2:
                    temp = self.nums[o]*self.nums[o+1]
                    self.nums.pop(o)
                    self.ops.pop(0)
                    bodmas.pop(o)
                    self.nums[o] = temp
                    #print('product', self.ops, bodmas)

        return self.nums[0]

cal = Calculator()

#getting math statement from user and processing it into the three calculator lists
equation = input("enter statement: ")

print(cal.calculate(equation))


