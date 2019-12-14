def normalize(num):
    total = sum(num)
    res = []
    for val in num:
        percent = 100 * val / total
        res.append(percent)
    return res


def read_visits(data):
    with open(data) as f:
        for line in f:
            yield int(line)


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


if __name__ == "__main__":
    # visited = [15, 35, 80]
    # percentage = normalize(visited)
    # print(percentage)
    # itr = read_visits("visited.txt")
    # per = normalize(itr)
    # print(per)
    visits = ReadVisits("visited.txt")
    per = normalize(visits)
    print(per)
