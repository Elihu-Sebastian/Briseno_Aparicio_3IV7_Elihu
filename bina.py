
def bin_dec(n):
    S = 0
    i = 0
    f = 0
    print("El binario", n)
    while(n >= 1):
        d = n%10;
        n = int(n/10);
        S = S+d*pow(2, i);
        i = i +1
        f = S
    print(f)
bin_dec(1101)
