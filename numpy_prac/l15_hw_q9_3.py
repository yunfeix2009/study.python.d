count = 0
for m in range(1, 7):
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i+j+k>16:
                    count += 1
                    print(m, i, j, k)

print(count)
print(count/1296)

 
# count = 0
# i = 6
#
# for j in range(1, 7):
#     for k in range(1, 7):
#         if i+j+k>9:
#             count+=1
#             print(i, j, k)
#
# print(count)