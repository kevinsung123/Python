from itertools import islice


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result


def index_words_iter(text):
    if text:
        yield 0
    for idx, letter in enumerate(text):
        if letter == ' ':
            yield idx+1


def index_file(text):
    offset = 0
    for line in text:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


if __name__ == "__main__":
    address = 'Four score and seven years ago'
    res = index_words(address)
    res2 = list(index_words_iter(address))
    print(res)
    print(res2)
    with open('address.txt', 'r') as f:
        it = index_file(f)
        res3 = islice(it, 0, 7)
        print(list(res3))
