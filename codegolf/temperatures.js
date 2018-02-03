readline()
print(readline().split(' ').reduce((m,n)=>n*n-n<m*m?n:m)||0);
