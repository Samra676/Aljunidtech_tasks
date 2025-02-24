#write a python script that demonstrates ,type casting while swaping two variables, and print before and after swapping 
a=5#integer
b=10.7#float 
print('before swapping:',a,type(a),b,type(b))
a,b=float(b),int(a)#typecasting and swaping 
print('after swapping:',a,type(a),b,type(b))