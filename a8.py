def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))


def main():
	list = eval(input("Enter a list of numbers: "))
	print(maximum(list))

main()
