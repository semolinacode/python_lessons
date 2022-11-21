def check(k):
    a=3
    if k==a or k>a  and k!=4 and k!=7:
        return True
    else:
        return False

for i in range(10000000):
    res = check(i)
    if i == 1 or i == 2 or i == 4 or i == 7:
        continue
    if res == False:
        print(i)
