# #(1) psサーバーで動くか未確認
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(0.0, 3.1, 1000)

# plt.plot(x, np.cos(2*np.pi*x), color="red", label="cos(2πx)")
# plt.plot(x, np.sin(2*np.pi*x), color="blue", label="sin(2πx)")
# plt.grid()
# plt.legend()
# plt.show()

#(4)_(a)and(b)and(c)
import random
def dice(): #サイコロ1~6の整数をランダムに返す
    return random.randint(1, 6)

#駅番号を管理　空港線用番号(0~19)+七隈線(20~39)+貝塚線(40~59)、余った番号は空番号
#駅がK12と与えられたとき駅番号を返す
def station_number(pos):
    if pos[0]=="K":
        return pos[1]-1
    elif pos[0]=="N":
        return 20+pos[1]-1
    else:
        return 20*2+pos[1]-1
    
def station_name(number):
    if number//20==0:
        line="K"
    elif number//20==1:
        line="N"
    else:
        line="H"
    sta=number%20

    return [line, sta+1]

start=[["K", 1], ["N", 1], ["H", 1]]#西端
term=[["K", 13], ["N", 18], ["H", 7]]#東端
transfer_sta=[["K", 9], ["K", 11], ["N", 18], ["H", 1]]
max_count=100

def test():
    pos=["K", 9] #現在の場所position
    count=0
    while count<max_count:
        if pos in transfer_sta:
            if pos==["K", 9] and dice()==1:
                pos=["H", 1]
            elif pos==["H", 1] and dice()==1:
                pos=["K", 9]
            elif pos==["K", 11] and dice()==1:
                pos=["N", 18]
            elif pos==["N", 18] and dice()==1:
                pos=["K", 11]

        count+=1
        if pos in start:
            pos[1]+=1
        elif pos in term:
            pos[1]-=1
        else:
            if dice()<=3:
                pos[1]+=1
            else:
                pos[1]-=1
    
    return station_number(pos)

N=1000 #試行回数
result=[0 for _ in range(20*3)]
for i in range(N):
    number=test()
    result[number]+=1

max_value=max(result)
max_index=result.index(max_value)
# print(result)
print(*station_name(max_index))
print(result)

Kcount=sum(result[0:20])
Ncount=sum(result[20:40])
Hcount=sum(result[40:60])
max_val=max(Kcount, Ncount, Hcount)
print(Kcount, Ncount, Hcount)

if max_val==Kcount:
    print("空港線", end=" ")   
if max_val==Ncount:
    print("七隈線", end=" ")   
if max_val==Hcount:
    print("箱崎線", end=" ")