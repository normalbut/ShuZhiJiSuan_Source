from math import *

def qiu_1(h):
    return (cos(0.5+h)-cos(0.5-h))/(2*h)

G=[]
h=[0.1,0.1/2,0.1/4,0.1/8]
for i in h:
    G.append(qiu_1((i)))


G1=[];G2=[];G3=[];
for i in range(0,3):
    G1.append(4*G[i+1]/3-G[i]/3)
for i in range(0,2):
    G2.append(16*G1[i+1]/15-G1[i]/15)
for i in range(0,1):
    G3.append(64*G2[i+1]/63-G2[i]/63)
#求G(H)

print("\nh--0.1={:>15.6f}\nh--0.05={:>14.6f}\nh--0.025={:>13.6f}\nh--0.0125={:>12.6f}"
      .format(G[0],G[1],G[2],G[3]))
print("\nG1={:>13.6f} {:>13.6f} {:>13.6f}\nG2={:>13.6f} {:>13.6f}\nG3={:>13.6f}"
      .format(G1[0],G1[1],G1[2],G2[0],G2[1],G3[0]))
print('',"G1、G2、G3原始数据为",G1,G2,G3,sep='\n')
