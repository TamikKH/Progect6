if __name__ == '__main__':
    def insert_letter_after_i(word, podstava):
        indexi = word.find('и')
        new_word = word[:indexi + 1] + podstava + word[indexi + 1:]
        return new_word
    wordi = input("Введите слово, оканчивающее символом «.»: ")
    if wordi.endswith('.'):
        podstava = input("Введите букву для вставки после первой буквы и: ")
        result_word = insert_letter_after_i(wordi, podstava)
        print("Результат:", result_word)
    else:
        print("Слово не оканчивается символом «.».")