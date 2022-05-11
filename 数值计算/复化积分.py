list_x=[0,0.25,0.5,0.75,1]
list_y=[2,1.569840,1.042904,0.703272,0.635802]
add_2=add_1=list_y[0]+list_y[len(list_y)-1]
for i in range(1, len(list_y)-1):
    add_1+=(list_y[i]*2)
for i in range(1,len(list_y)-1):
    if i%2==0:
        add_2+=(list_y[i]*2)
    else:
        add_2+=(list_y[i]*4)
add_3=7*(list_y[0]+list_y[4])+32*(list_y[1]+list_y[3])+list_y[2]*12
print("复化梯形公式值为{0:>12}\n复化辛甫生公式值为{1:>12}\n柯特斯法为{2:>12}".format(add_1/8,add_2/12,add_3/90))
input()