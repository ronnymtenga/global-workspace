import numpy as np
def precedence_list(operations):
    # Define the order of operations (a dictionary)
    order_of_precedence = {'^': 0, '/': 1, '*': 2, '+': 3, '-': 4}

    # len ets the length of a list, range turns that number into 
    # a range object that looks like: range(0,1,5) where 0 is the 
    # inclusive start point, 1 the step size and 5 the exclusive end
    # list turns the range object into an actual list, in our case an index list 
    indexes = list(range(len(operations)))

    # Sort the indexes based on the order of operations
    # A lambda function has the fpllowing syntax
    '''add = lambda a,b : a+b
       sum = add(5,6)
       print(sum) # output: 11    
    '''
    # get(key, default); dictionary look up via key, returns default when key is absent in the dictionary. 
    # Here operations[x] is the x-th math symbol which is the key in the order_of_precedence list.
    # sort(); sorts a list in ascending order; sort(reverse+True) in descending order
    get_precedence = lambda x : order_of_precedence.get(x, 0)

    precedence = [get_precedence(x) for x in operations]
        
    return precedence

def precedence_list1(operations):
    order_of_precedence = {'^': 0, '/': 1, '*': 2, '+': 3, '-': 4}
    indexes = list(range(len(operations)))

    precedence = [order_of_precedence.get(x, 0) for x in operations]

    return precedence

'''# Example usage:
math_operations = ['*', '/', '-', '/','/']
print(range(len(math_operations)))
result = precedence_list(math_operations)
print(result)

numss = [8,4,6,2]
print(np.argmax(np.array(numss)==8))
'''

def finderr(a_list, x):
    temp_list = [True if item == x else False for item in a_list]
    i = 0
    while temp_list[i] != True:
        i+=1
        if i>=len(temp_list):
            return -1
    
    return i

def finderrr(a_list, x):
    try:
        return a_list.index(x)
    except ValueError:
        return -1
    


def string_to_list(input_string):
    result_list = []
    i = 0

    while i < len(input_string):
        current_char = input_string[i]
        #handles if current character is last character is not a number
        if not current_char.isdigit() and i+1 == len(input_string): 
            result_list.append(current_char)
            break
        #handles if current character is first character can be associated with a number or is a number
        elif ((current_char == '+' or current_char == '-' or current_char=='.') and input_string[i+1].isdigit() and i == 0): 
            while i + 1 < len(input_string) and (input_string[i + 1].isdigit() or (input_string[i + 1]=='.')):
                current_char += input_string[i+1]
                i += 1
            result_list.append(float(current_char))
        #handles if current character is not a number in any arbitrary position
        elif not current_char.isdigit():
            result_list.append(current_char)
        #handles if current character is a number
        if current_char.isdigit():
            flag1 = False
            flag2 = True
            #runs if next character is a number or a decimal point
            while i + 1 < len(input_string) and (input_string[i + 1].isdigit() or (input_string[i + 1]=='.') ):
                #handles if current character is a decimal point
                if input_string[i + 1]=='.':
                    #runs when current decimal point is first occurence
                    if flag1 == False:
                        print('False')
                        current_char+=input_string[i+1]
                    #runs when current decimal point is second occurence and prints it as a character
                    else:
                        result_list.append(current_char)
                        flag2=False
                        print('True')
                        break
                #runs when current character is a number and not a decimal point   
                else:
                    print('here')
                    current_char+=input_string[i+1] 
                    
                i += 1
            #sets value only if we get a number from the while loop
            if flag1 == False and flag2==True: 
                result_list.append(float(current_char))

        i += 1
    print(result_list)
    return result_list

'''input_string = "3/4-0.4^4"
result = string_to_list(input_string)
print(result)'''




