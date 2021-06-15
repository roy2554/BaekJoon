deliver_cnt = 0

def sugar_delivery(NKG):
    global deliver_cnt
    while True:
        if NKG%5==0:
            deliver_cnt += NKG//5
            return deliver_cnt
            break
        else:
            NKG -=3
            deliver_cnt += 1
        if NKG <0:
            return -1
            break

n = int(input(":"))
sugar_delivery(n)
print(deliver_cnt)
