def perform_operation(num1,num2,operation):
    if operation=="add":
       result=num1+num2
    elif operation=="subtract" :
       result=abs(num1-num2)
    elif operation=='multiply':
       result=num1*num2
    elif operation=='divide':
       if num2==0:
          print('enter avalid number: ')
          num2=float(input('enter the valid number:'))  
          result=num1/num2
       result=num1/num2
    return result
