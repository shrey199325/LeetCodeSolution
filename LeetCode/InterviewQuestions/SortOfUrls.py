class Website(object):
    def __init__(self, site):
        self.URL = site


class Internet(object):
    def __init__(self):
        self.url_list = dict()

    def add_url(self, website):
        if website.URL in self.url_list:
            self.url_list[website.URL] += 1
        else:
            self.url_list[website.URL] = 1

    def solution(self):
        return sorted(self.url_list.items(), key=lambda i: (-i[1], i[0]))


def solve(S, N):
    net = Internet()
    for s in S:
        net.add_url(s)
    return net.solution()


# write your code here

N = int(input())
S = []
for _ in range(N):
    S.append(Website(input()))

out_ = solve(S, N)
print(len(out_))
for i_out_ in out_:
    print(i_out_[0])