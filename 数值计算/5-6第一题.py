from math import pow
N=0
x=1.0
niudun=lambda x:(2*pow(x,3)+2*pow(x,2)+10)/(3*pow(x,2)+4*x+10)
while N<4:
    if N==0:
        print("取x0为1，4次牛顿法迭代值为")
        print(x)
    x=niudun(x)
    print("{:.6}".format(x))
    N=N+1
x_list=[0.9,1.0]
fx=lambda x:pow(x,3)+2*pow(x,2)+10*x-10
M=0
while M<6:
    if M==0:
        print("取x0为0.9，x1为1,4次快速弦截值为")
    x_list.append(x_list[-1]-(x_list[-1]-x_list[-2])*
                  fx(x_list[-1])/(fx(x_list[-1])-fx(x_list[-2])))
    print("{:.6}".format(x_list[int(M)]))
    M=M+1
