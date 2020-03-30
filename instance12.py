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
report.insert(1,['1','平均'])
totcs=[0,0,0,0,0,0,0,0,0]       #每门科目总分

for scores in report[2:]:
    tots = 0
    for i in scores[1:]:
        totcs[int(scores.index(i))-1]+=int(i)
        tots +=int(i)
    scores.append(str(tots))    #插入个人总分
    scores.append(str(tots/10)) #插入个人平均分

for i in totcs:                 #改成平均分
    x = format(int(i)/30,'.2f')
    totcs[totcs.index(i)]=str(x)

report[1] = report[1]+totcs     #插入科目总分
for i in report:
    i.append('\n')

sorted(report[2:],key=lambda x:x[-1]) #按平均分排序（除开头两行）
for i in range(2,32):
    report[i].insert(0,'%i' %(i))

for i in range(3,33):
    for j in range(2,13):
        try:
            if float(report[i][j]) < 60.0:
                report[i][j] = '不及格'
        except:
            pass
print(report[1][2])


with open('result.txt','w') as fl:
    for i in report:
        fl.writelines(i)
