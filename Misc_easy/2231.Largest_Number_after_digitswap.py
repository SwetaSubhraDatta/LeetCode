def largest_Integer(num):
    dict_odd_even = {"odd": [], "even": []}

    num = list(map(int, str(num)))
    for i in range(len(num)):
        if num[i] % 2 == 0:
            dict_odd_even["even"].append(num[i])
        else:
            dict_odd_even["odd"].append(num[i])

    odd_sorted = sorted(dict_odd_even["odd"], reverse=True)

    even_sorted = sorted(dict_odd_even["even"], reverse=True)

    for i in range(len(num)):
        if num[i] % 2 == 0:
            num[i] = even_sorted.pop(0)
        else:
            num[i] = odd_sorted.pop(0)

    return int("".join(map(str, num)))


def main():
    print(largest_Integer(1234))


main()
