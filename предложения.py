if __name__ == '__main__':
    print("Напишите любое предложение")
    x=input()
    y="нм"
    k=0
    for i in range(0,len(x)):
        if x[i] in y:
            k=k+1
            print(x[i])
    print(k)