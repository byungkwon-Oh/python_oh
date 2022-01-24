def print_gugudan(num):
    if type(num) != int:
        return
    elif 1 <= num <= 9:
        gugu = [ ]
        for i in range(1, 10):
            gugu.append(i*num)
        print(gugu)
    else:
        return
print_gugudan(2)




