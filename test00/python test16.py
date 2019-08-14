#-*-coding: utf-8 -*-

grade = {"이름":["철수","영희","민수","지현"],
"국어":[80,82,91,77],
"영어":[92,80,73,64],
"수학":[90,77,62,80],
"과학":[88,82,70,64]
}

tpl="{0},{1},{2},{3},{4}\n"
keys= list(grade.keys())

p=","
title=p.join(keys)

with open("grade.csv","w",encoding="euc-kr") as f:
    f.write(title+"\n")

    for i in range(0, len(grade['이름'])):
        tmp = tpl.format(grade['이름'][i],grade['국어'][i],
                         grade['영어'][i],grade['수학'][i],
                         grade['과학'][i])
        f.write(tmp)
