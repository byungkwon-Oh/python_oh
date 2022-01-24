def print_triangle_withdeco(num, deco = "%"):
    for i in range(1, num+1):
        print(" "*(num-i), deco*i)


print_triangle_withdeco(2)
print_triangle_withdeco(5, "*")

