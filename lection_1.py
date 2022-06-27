import math


"""
Задача № 1
Написать метод domain_name, который вернет домен из url адреса
"""


def domain_name(url):
    parts = url.split(".")
    return parts[1] if "www" in parts[0] else parts[0].split("//")[1]


# assert domain_name("http://google.com") == "google"
# assert domain_name("http://google.co.jp") == "google"
# assert domain_name("www.xakep.ru") == "xakep"
# assert domain_name("https://youtube.com") == "youtube"


"""
Задача № 2
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса
"""


def int32_to_ip(int32):
    x = 2**24
    y = 2**16
    z = 2**8
    a = int32//x
    b = (int32-a*x)//y
    c = (int32-a*x-b*y)//z
    d = int32-a*x-b*y-c*z
    return f"{a}.{b}.{c}.{d}"


# assert int32_to_ip(2154959208) == "128.114.17.104"
# assert int32_to_ip(0) == "0.0.0.0"
# assert int32_to_ip(2149583361) == "128.32.10.1"


"""
Задача № 3
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа
"""


def zeros(n):
    res = 0
    a = 5
    count = 1
    while n//a >= 1:
        res += n//a
        count += 1
        a = a**count
    return res


# assert zeros(0) == 0
# assert zeros(6) == 1
# assert zeros(30) == 7


"""
Задача № 4
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке
"""


def bananas(s, word):
    res = []

    if word == '':
        res.append(''.rjust(len(s), '-'))
        return res

    left_s = ''
    for si in range(len(s)):
        if word[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]
            if s[si+1:] == '' and word[1:] == '':
                res.append(left_s)
            else:
                right_s_list = bananas(s[si+1:], word[1:])
                for right_s in right_s_list:
                    res.append(left_s + right_s)
    return res


# assert bananas("banann") == set()
# assert bananas("banana") == {"banana"}
# assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
#                      "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
#                      "-ban--ana", "b-anana--"}
# assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
# assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


"""
Задача № 5
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL
"""


def count_find_num(primesL, limit):

    if math.prod(primesL) < limit:
        count = 1
        max_ = [math.prod(primesL)]

        for i in primesL:
            primesL_new = primesL.copy()
            while math.prod(primesL_new) <= limit:
                primesL_new.append(i)
                print(primesL_new)
                if math.prod(primesL_new) <= limit:
                    count += 1
                    max_.append(math.prod(primesL_new))
                else:
                    break
        max_.sort()
        return [count, max_[-1]]
    return []


# primesL = [2, 3]
# limit = 200
# assert count_find_num(primesL, limit) == [13, 192]
#
# primesL = [2, 5]
# limit = 200
# assert count_find_num(primesL, limit) == [8, 200]
#
# primesL = [2, 3, 5]
# limit = 500
# assert count_find_num(primesL, limit) == [12, 480]
#
# primesL = [2, 3, 5]
# limit = 1000
# assert count_find_num(primesL, limit) == [19, 960]
#
# primesL = [2, 3, 47]
# limit = 200
# assert count_find_num(primesL, limit) == []
