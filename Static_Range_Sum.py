# Question link: https://judge.yosupo.jp/problem/static_range_sum

n, q = [int(i) for i in input().split(' ')]
d = {-1: 0}
a = input()
i = 0
ex = True
while ex:

    try:
        tem, a = a.split(' ', 1)

        d[i] = d[i - 1] + int(tem)

    except ValueError:
        d[i] = d[i - 1] + int(a)
        ex = False
    finally:
        i += 1

for i in range(0, q):

    l, r = [int(j) for j in input().split(' ')]
    print(l,r)
    print(i)
    print(d[r - 1] - d[l - 1])
