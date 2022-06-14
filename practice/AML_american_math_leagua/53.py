result_dict = {}

list_1 = [1,0,1,0,1]
for i in range(22):
    list_1.append(0)

result_dict[10] = [list_1]

def handleTeam(num:int):
    list_last_num = result_dict.get(num+1)
    list_curr_num = []
    for p in list_last_num:
        for i in range(27):
            if i+num*2+2>=27:
                break
            if p[i]==0 and p[i+num+1]==0 and p[i+num*2+2]==0 :
                new_p = p[:]
                new_p[i] = new_p[i+num+1] = new_p[i+num*2+2] = num
                list_curr_num.append(new_p)
    result_dict[num] = list_curr_num

for i in range(9,1,-1):
    handleTeam(i)
print(result_dict)
print(result_dict.get(2)[0])



