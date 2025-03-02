while True:
    num : str = input("Enter a Number: ")[::-1]
    if not num.isdigit():
        print("Please enter a valid number!")
        continue
    numlen: int = len(num)
    formatted: list[str] = []
    j: int = 0
    for i in range(numlen):
        j +=1
        formatted.append(num[i])
        if j == 3 and i != numlen - 1:
            j = 0
            formatted.append(",")
    formatted = "".join(formatted)
    print(formatted[::-1])
