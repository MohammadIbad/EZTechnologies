import sys
stack=[]
str=input()
l=len(str)
c=0
if(str[0]==')' or str[0]==']' or str[0]=='}') or l%2!=0:
    print("Unbalanced")
    sys.exit()
else:
    for i in range(l):
        if(str[i]=='(' or str[i]=='[' or str[i]=='{'):
            stack.append(str[i])
            c+=1
        elif(str[i]==')' or str[i]==']' or str[i]=='}'):
            if(stack==[]):
                break
            elif((str[i]==')' and stack[-1]=='(' )or (str[i]==']' and stack[-1]=='[' )or (str[i]=='}' and stack[-1]=='{')):
                stack.pop()
                c-=1
            else:
                break
if c==0:
    print("Balanced")
else:
    print("Unbalanced")
