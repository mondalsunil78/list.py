exp = [2600, 2365, 4582, 4789, 6548]
total = 0
for i in range(len(exp)) :
    print('month:', (i+1), 'expence:', exp[i])
    total = total + exp[i]

print('total expence is:', total)
