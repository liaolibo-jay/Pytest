import os
import requests

accountment=[]
with open('gUser.txt') as f:  #打开文件后对数据做初步整理
    raccountment = f.readlines()
for i in raccountment:
    i = i.strip().split()
    accountment.append(i)
nindex =0
name = input('请输入你的名字：') #如果已经有名字，直接输出之前的结果以及记录该名字的次序
for i in range(len(accountment)):
    if name == accountment[i][0]:
        print('%s你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' %(accountment[i][0],int(accountment[i][1]),int(accountment[i][2]),float(int(accountment[i][3])/int(accountment[i][1]))))
        break
    else:
        nindex += 1
if nindex == len(accountment):  #遍历之后没有发现，则添加一个新名字
    accountment.append([name,'0','0','0'])
    print('%s你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' %(name,0,0,0))

while True:
    r = int(requests.get('https://python666.cn/cls/number/guess/').text) #得到底数
    print(r) # 当作没看见
    nRound = 1
    while True:                                 #开始猜数字，至少有一轮，因此开始序数为1
        gNumber = input('请猜一个1-100的数字：')
        if gNumber.isdigit():
            if int(gNumber) == r:
                print('猜对了，你一共猜了%i轮'% (nRound))
                break
            elif int(gNumber) > r:
                print('猜大了，再试试：')
            else:
                print('猜小了，再试试：')
        else:
            print('请输入数字')
        nRound += 1
    
    accountment[nindex][1] = str(int(accountment[nindex][1])+1)  #修改为新结果
    accountment[nindex][3] = str(int(accountment[nindex][3])+nRound)
    if nRound < int(accountment[nindex][2]):                     #比较最快轮数并修改
        accountment[nindex][2] = str(nRound)
    print('%s你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' %(accountment[i][0],int(accountment[i][1]),int(accountment[i][2]),float(int(accountment[i][3])/int(accountment[i][1]))))
    goA = input('是否继续游戏？（输入y继续，其他退出）')
    if goA != 'y':
        print('退出游戏，欢迎下次再来！')
        break

for i in accountment:                                           #整理文件并输出
    i.append("\n")
    accountment[accountment.index(i)] = ' '.join(i)
with open('gUser.txt','w') as f:
    for i in accountment:
        f.writelines(i)
