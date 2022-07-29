id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

reports = {x:0 for x in id_list}

answer = [0] * len(id_list)
k =2

for r in set(report):
    reports[r.split()[1]] +=1

for r in set(report):
    if reports[r.split()[1]] >= k:
        answer[id_list.index(r.split()[0])] +=1

print(answer)

