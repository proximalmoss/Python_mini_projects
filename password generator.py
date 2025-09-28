import random
pass_len=int(input("enter the length of password: "))
s="abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
p="".join(random.sample(s,pass_len))
print(p)