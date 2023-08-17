def cplxsum(a,b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return(real, imag)

if __name__ == '__main__':
    print(cplxsum((3, 5),(-2.6, 6.8)))


