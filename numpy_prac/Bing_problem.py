ls = []
longest_continue = 1
for i in range(100, 1000):
    if i%(i//100+(i//10)%10+i%10) == 0:
        ls.append(i)
difference = 1
for i in range(1, len(ls)):
    print('number is %s' % ls[i] + '    ' + 'difference is %s' % (ls[i]-ls[i-1]-1))
    # print('difference is %s' % (ls[i]-ls[i-1]-1))
    if ls[i]-ls[i-1] > difference:
        difference = ls[i]-ls[i-1]-1
print('========== longest consective integers that meet requirement is %d ==========' % (difference))
