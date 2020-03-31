import os

def splist(slst):               #分割成列表
    slst = slst.split()
    return slst

with open('report.txt') as f:
    areport = f.readlines()
report = []
for i in areport:               #把多行换成列表
    i = splist(i.strip())
    report.append(i)
report[0] = report[0]+['总分','平均分']
report[0].insert(0,'名次')
report.insert(1,['平均'])
totcs=[0,0,0,0,0,0,0,0,0]       #每门科目总分

for i in range(1,len(report[2])):
    for j in range(2,len(report)):
        totcs[i-1] += int(report[j][i])

for i in totcs:                 #改成平均分
    x = format(int(i)/30,'.2f')
    totcs[totcs.index(i)]=str(x)

report[1] = report[1]+totcs     #插入科目均分

for scores in report[1:]:
    tots = 0
    for i in scores[1:]:
        tots +=float(i)
    scores.append(str(tots))   #插入个人总分
    scores.append(str(format((tots/9),'.2f'))) #插入个人平均分

for i in report:
    i.append('\n')

report[2:]=sorted(report[2:],key=lambda x:x[-2],reverse=True) #按平均分排序（除开头两行）
for i in range(1,32):
    report[i].insert(0,'%i' %(i-1))

for i in range(2,33):
    for j in range(2,13):
        try:
            if float(report[i][j]) < 60.0:
                report[i][j] = '不及格'
        except:
            pass

for i in report:
    report[report.index(i)] = ' '.join(i)

with open('result.txt','w') as fl:
    for i in report:
        fl.writelines(i)
