# нечёткое сравнение строк

def compare(s1, s2):
    ngrams = [
            s1[i:i+3] for i in range(len(s1))
    ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count/max(len(s1), len(s2))

def main():
    s1 = input("Введите первую строку:")
    s2 = input("Введите вторую строку:")
    print(compare(s1, s2))

if __name__ == '__main__':
    main()

