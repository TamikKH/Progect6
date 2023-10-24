if __name__ == '__main__':
    print("Напишите любое предложение")
    x=input()
    zi="жы"
    shi="шы"
    if zi in x or shi in x:
        print("Ошибка")
    else:
        print("Предложение написано правильно")