###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

def sort_decrease(number):
    if len(number) == 1:
        return number

    if len(number) == 2:
        return number if int(number[0]) > int(number[1]) else number[1] + number[0]
    
    max_digit = str(max(int(i) for i in number))
    return max_digit + sort_decrease(number.replace(max_digit, "", 1))


def sort_increase(number):
    if len(number) == 1:
        return number

    if len(number) == 2:
        return number if int(number[0]) < int(number[1]) else number[1] + number[0]
    
    min_digit = str(min(int(i) for i in number))
    return min_digit + sort_increase(number.replace(min_digit, "", 1))


def strange_pattern(number):
    global count

    a = "".join(sorted(number, reverse=True)) # sort_decrease(number)
    b = "".join(sorted(number))
    c = str(int(a) - int(b))

    if c != '495': strange_pattern(c)
    count += 1


def sort_result(result):
    if len(result) == 1:
        return result
    
    if len(result) == 2:
        if result[0][1] != result[1][1]: return 


def main():
    global count

    aux = []
    for item in input().split():
        count = 0
        strange_pattern(item)

        aux.append((count, item))

    result = {}
    for item in aux:
        if item[0] in result.keys():
            result[item[0]].append(item[1])
        else:
            result[item[0]] = [item[1]]

    print(" ".join(z for x in list(sorted(result[y]) for y in sorted(result.keys())) for z in x))

main()