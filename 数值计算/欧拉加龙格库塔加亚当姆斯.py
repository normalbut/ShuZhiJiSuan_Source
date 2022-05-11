import math

h1=0.1
h2=0.2
h3=0.2
oula_1=[0]
oula_2=[0]
longge_4=[0]
yadang_2_xian=[0]
yadang_2_yin=[0]
yadangxitong=[0]

#原数据
y=lambda x:x+math.exp(-x)
Y=[1]

#求y‘
dydx=lambda x,y:1-2*y

x=0
while x<1.95:
    x+=h1
    Y.append(y(x))

#欧拉
x=0
while x<1.95:
    oula_1.append(oula_1[-1]+dydx(x,oula_1[-1])*h1)
    x+=h1

#改进的欧拉
k=1
while k<=10:
    yuxian=oula_2[-1]+dydx((k-1)*h2,oula_2[-1])*h2
    oula_2.append(oula_2[-1]+h2*(dydx((k-1)*h2,oula_2[-1])+dydx(k*h2,yuxian))/2)
    k+=1
#二阶显式亚当姆斯
yadang_2_xian.append(0.165)
k=2

while k<=5:
    yadang_2_xian.append(yadang_2_xian[-1]+h3/2*(3*dydx((k-1)*h3,yadang_2_xian[-1])-dydx((k-2)*h3,yadang_2_xian[-2])))
    k+=1

#二阶亚当隐式
yadang_2_yin.append(0.165)
k=2
while k<=5:
    yuxian=yadang_2_yin[-1]+dydx((k-1)*h2,yadang_2_yin[-1])*h2
    yadang_2_yin.append(yadang_2_yin[-1]+h2*(dydx((k-1)*h2,yadang_2_yin[-1])+dydx(k*h2,yuxian))/2)
    k+=1
#4阶龙格
k=1

while k<=5:
    k1=dydx((k-1)*h3,longge_4[-1])
    k2=dydx((k-0.5)*h3,longge_4[-1]+h3/2*k1)
    k3=dydx((k-0.5)*h3,longge_4[-1]+h3/2*k2)
    k4=dydx(k*h3,longge_4[-1]+h3*k3)
    longge_4.append(longge_4[-1]+h3*(k1/6+k2/3+k3/3+k4/6))
    k+=1

#亚当系统
k=4
c=p=0
for i in range(1,4):
    yadangxitong.append(longge_4[i])
while k<=5:
    p1=yadangxitong[-1]+h3/24*(55*dydx((k-1)*h3,yadangxitong[-1])-59*dydx((k-2)*h3,yadangxitong[-2])+
                               37*dydx((k-3)*h3,yadangxitong[-3])-9*dydx((k-4)*h3,yadangxitong[-4]))
    m1=p1+251/270*(c-p)
    c1=yadangxitong[-1]+h3/24*(9*dydx(k*h3,m1)+19*dydx((k-1)*h3,yadangxitong[-1])-5*dydx((k-2)*h3,yadangxitong[-2])
                               +dydx((k-3)*h3,yadangxitong[-3]))
    yadangxitong.append(c1-19/270*(c1-p1))
    p=p1
    c=c1
    k+=1
#输出
k=0
print("\n{:^16}{:^16}{:^14}{:^13}{:^12}".format("Xn","Yn","欧拉格式","改进欧拉格式","4阶龙格-库塔"))
while k<=20:
    if k%4==0:
        print("{:^16.5f}{:^16.5f}{:^16.5f}{:^16.5f}{:^16.5f}".format(k*h1, Y[k], oula_1[k], oula_2[int(k/2)],longge_4[int(k/4)]))
    elif k%2==0:
        print("{:^16.5f}{:^16.5f}{:^16.5f}{:^16.5f}".format(k*h1, Y[k], oula_1[k], oula_2[int(k/2)]))
    else :
        print("{:^16.5f}{:^16.5f}{:^16.5f}".format(k*h1, Y[k], oula_1[k]))
    k+=1
print(yadang_2_xian,yadang_2_yin,yadangxitong,sep='\n')
print("显式二阶亚当：",end='')
for i in range(0,6):
    print("{:^10.5f}".format(yadang_2_xian[i]),end='')
print('\n')
print("隐式二阶亚当：",end='')
for i in range(0,6):
    print("{:^10.5f}".format(yadang_2_yin[i]),end='')
print('\n')
print("亚当综合系统的y4，y5：","{:^10.5f}".format(yadangxitong[4]),"{:^10.5f}".format(yadangxitong[5]))
# print(len(Y),len(oula_1),len(oula_2),len(longge_4))

