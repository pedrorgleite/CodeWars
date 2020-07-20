def hexagonal (n, seq):
    num = 0
    hsum = 0
    max_hsum = 0
    res = []
    for i in range(n*2-1):
        hsum = 0
        ls = []
        for k in range((n*2-1)-abs(i-(n-1))):
           # print(str(seq[num%len(seq)]) + " ",end = "")
            ls.append(seq[num%len(seq)])
            hsum += seq[num%len(seq)]
            num += 1
        ls.extend([0 for q in range(abs(i-(n-1)))])
        res.append(ls)
        if hsum > max_hsum:
            max_hsum = hsum
       # print('\n') 
    #print(res) 
    for index in range(n):
        print(res[index])
        print(sum(res[index]))
        print('\n')
    return max_hsum

hexagonal(4,(2,4,6,8))
