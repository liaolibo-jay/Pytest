import os
import requests

accountment=[]
with open('gUser.txt') as f:
    raccountment = f.readlines()
for i in raccountment:
    i = i.strip().split()
    accountment.append(i)
nindex =0
name = input('请输入你的名字：')
for i in range(len(accountment)):
    if name == accountment[i][0]:
        print('%s你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' %(accountment[i][0],int(accountment[i][1]),int(accountment[i][2]),float(int(accountment[i][3])/int(accountment[i][1]))))
        break
    else:
        nindex += 1
if nindex == len(accountment):
    accountment.append([name,'0','0','0'])
    print('%s你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' %(name,0,0,0))

r = requests.get('https://python666.cn/cls/number/guess/').text
nRound = 1
while True:
    gNumber = input('请猜一个1-100的数字：')
    if gNumber.isdigit():
        if gNumber == r:
            print('猜对了，你一共猜了%i轮'% (nRound))
            break
        elif gNumber > r:
            print('猜大了，再试试：')
        else:
            print('猜小了，再试试：')
    nRound += 1

accountment[nindex][1] = str(int(accountment[nindex][1])+1)
accountment[nindex][3] = str(int(accountment[nindex][3])+nRound)
if nRound < int(accountment[nindex][2]):
    accountment[nindex][2] = str(nRound)

for i in accountment:
    i.append("\n")
    accountment[accountment.index(i)] = ' '.join(i)
with open('gUser.txt','w') as f:
    for i in accountment:
        f.writelines(i)
