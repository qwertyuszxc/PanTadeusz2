def f(binary_number):
    num = str(binary_number)
    mistake = 0
    for i in range(len(num)):
        if num[i] != '0' and num[i] != '1':
            mistake += 1
    if mistake >= 1:
        return(False)
    else:
        return(True)
