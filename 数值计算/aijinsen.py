diff= {}
n = int(input('输入插值数目：'))
x_list = input('输入一行x：').split(",")
x_tuple = tuple([float(x_list[i]) for i in range(len(x_list))])
y_list = input('输入一行y：').split(",")
y_tuple = tuple([float(y_list[i]) for i in range(len(y_list))])
#x = float(input('输入x:'))
for i in range(0,n):
    for j in range(i,n):
        diff.update({(i,j):0})
for i in range(0,n):
    diff[(0,i)]=y_tuple[i]
def cacul_diff(n, l):
    if l > 0:
        fx = (cacul_diff(n-1,l-1)-cacul_diff(n,l-1))/(x_tuple[n-l]-x_tuple[n])
        diff[(l,n)]=fx
        return fx
    else:
        return y_tuple[n]

cacul_diff(n-1,n-1)
print('xi','yi',sep='\t\t',end='\t\t')
for i in range(1,n):
    if i !=n-1:
        print(str(i)+'阶',end='\t\t')
    else:
        print(str(i)+'阶',end='\n')
for i in range(0,n):
    print(x_tuple[i],end='\t\t')
    for j in range(0,i+1):
        if j!=i:
            print('%0.1f'%diff[(j,i)],end='\t\t')
        else:
            print('%0.1f'%diff[(j,i)],end='\n')






