h=0.1
oula_1=[0]
oula_2=[0]
y=lambda x:x/(1+x*x)
Y=[0]
x=0
dydx=lambda x,y:(1-2*y*y*(1+x*x))/(1+x*x)
while x<1.95:
    x+=h
    Y.append(y(x))
x=0
while x<1.95:
    oula_1.append(oula_1[-1]+dydx(x,oula_1[-1])*h)
    x+=h

k=1
while k<=20:
    yuxian=oula_2[-1]+dydx((k-1)*h,oula_2[-1])*h
    oula_2.append(oula_2[-1]+h*(dydx((k-1)*h,oula_2[-1])+dydx(k*h,yuxian))/2)
    k+=1
k=0
print("\n{:^16}{:^16}{:^14}{:^13}".format("Xn","Yn","欧拉格式","改进欧拉格式"))
while k<=20:
    print("{:^16.6f}{:^16.6f}{:^16.6f}{:^16.6f}".format(k*h, Y[k], oula_1[k], oula_2[k]))
    k+=1
print(Y,oula_1,oula_2,sep='\n')

