def sum(num1 , num2):
    result= num1+num2
    def square(take_result):
        return take_result*take_result
    return square(result)
print(sum(num1=10, num2=20)) 
    

    #optimized

def sum(num1,num2):
    result = num1 + num2
    def square():
        return result * result
    return square()

print(sum(num1=10,num2=20))



 

