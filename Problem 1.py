''' Sum of multiples of 3 in 1000
999 is highest multiple
996 + 3 = 999
993 + 6 = 999
...
999 0
996 3
999 // 2 = ?

'''


# int(100/(3 * 2)) * 99 + midpoint if applicable + multiple
def best_solution(f, l, n):
    # f = first term, l = last term, n = number of terms
    return (n * (f + l)) / 2

def my_solution(n, high):
    h_mult = int(high / n) * n
    pairs = int(h_mult / (n*2))
    if h_mult % 2 == 0:
        mid = h_mult / 2
        pairs -= 1
    else:
        mid = 0
    return (pairs * h_mult) + mid + h_mult
# print(int(1000/15) * 15)
# print(my_solution(3, 1000) + my_solution(5, 1000))

def find_n(n):
    tot = 0
    for i in range(n):
        tot += i

    print(tot)

find_n(33)






















