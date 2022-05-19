N=100
wucha=0.00001
def gauss(Input):
    output=[0,0,0,0]
    count=0
    flag=0
    while (count<N) & (flag ==0):
        flag=1
        count+=1
        output[0]=(3*Input[3]-Input[2])/11
        output[1]=(3*Input[2]+11-output[0])/8
        output[2]=(3*output[0]+2*output[1]+Input[3]-27)/10
        output[3]=(output[1]-output[0]-2*output[2]+17.5)/7
        for i in range(0,len(output)):
            if(abs(output[i]-Input[i])>wucha):
                flag=0
                break
        if flag==1:
            print("误差为0.00001,高斯赛德尔迭代收敛为{},共计算{}次".format(output,count))
            return
        Input=output.copy()
    print('无法收敛')
    pass
def jacobi(Input):
    output=[0,0,0,0]
    count=0
    flag=0
    while (count<N) & (flag ==0):
        flag=1
        output[0]=(3*Input[3]-Input[2])/11
        output[1]=(3*Input[2]+11-Input[0])/8
        output[2]=(3*Input[0]+2*Input[1]+Input[3]-27)/10
        output[3]=(Input[1]-Input[0]-2*Input[2]+17.5)/7
        for i in range(0,len(output)):
            if(abs(output[i]-Input[i])>wucha):
                flag=0
                break
        if flag==1:
            print("误差为0.00001,Jacob迭代收敛为{},共计算{}次".format(output,count))
            return
        Input=output.copy()
        count+=1
    print('无法收敛')
    pass
def songchi_1_3(Input):
    output=[0,0,0,0]
    count=0
    flag=0
    while (count<N) & (flag ==0):
        flag=1
        count+=1
        output[0]=(3*Input[3]-Input[2])/11
        output[0]=1.3*output[0]-0.3*Input[0]
        output[1]=(3*Input[2]+11-output[0])/8
        output[1]=1.3*output[1]-0.3*Input[1]
        output[2]=(3*output[0]+2*output[1]+Input[3]-27)/10
        output[2]=1.3*output[2]-0.3*Input[2]
        output[3]=(output[1]-output[0]-2*output[2]+17.5)/7
        output[3]=1.3*output[3]-0.3*Input[3]
        for i in range(0,len(output)):
            if(abs(output[i]-Input[i])>wucha):
                flag=0
                break
        if flag==1:
            print("松弛因子为1.3,误差为0.00001,高斯赛德尔迭代收敛为{},共计算{}次".format(output,count))
            return
        Input=output.copy()
    print('无法收敛')
    pass

def songchi_0_9(Input):
    output=[0,0,0,0]
    count=0
    flag=0
    while (count<N) & (flag ==0):
        flag=1
        output[0]=(3*Input[3]-Input[2])/11
        output[0]=0.9*output[0]+0.1*Input[0]
        output[1]=(3*Input[2]+11-output[0])/8
        output[1]=0.9*output[1]+0.1*Input[1]
        output[2]=(3*output[0]+2*output[1]+Input[3]-27)/10
        output[2]=0.9*output[2]+0.1*Input[2]
        output[3]=(output[1]-output[0]-2*output[2]+17.5)/7
        output[3]=0.9*output[3]+0.1*Input[3]
        for i in range(0,len(output)):
            if(abs(output[i]-Input[i])>wucha):
                flag=0
                break
        if flag==1:
            print("松弛因子为0.9,误差为0.00001,J迭代收敛为{},共计算{}次".format(output,count))
            return
        Input=output.copy()
        count+=1
    print('无法收敛')
    pass

x=input('依次输入4个初始值，以逗号隔开：').split(',')
X = list([float(x[i]) for i in range(len(x))])
print(X)
jacobi(X)
gauss(X)
songchi_1_3(X)
songchi_0_9(X)            
    
