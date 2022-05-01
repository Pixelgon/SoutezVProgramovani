# -----------------------------------------------------------
# Hratky s cisly 3. soutezni uloha 
# Vytvoril Matej Matejka
# -----------------------------------------------------------

import math

# Podprogram na urceni prvocisla
def prvocislo(num):
    # Pokud se cislo rovna 1
    if num == 1:
        return False
    # Pokud se cislo rovna 1
    if num == 2:
        return True
    # Pokud se je vetsi nez 2 a module je rovno 0
    if num > 2 and num % 2 == 0:
        return False
    maxDelit = math.floor(math.sqrt(num))
    for i in range(3, 1 + maxDelit, 2):
        if num % i == 0:
            return False
    return True

numorig = int(input("Zadejte prosím číslo: "))
num = numorig
cycl = False
while True:
    while cycl == False:
        num = num - 1
        cycl = prvocislo(num)
    # Prevedeme cislo na seznam
    numsez = [int(x) for x in str(num)]
    # Overime zda se zadne cislo neopakuje
    if len(numsez) == len(set(numsez)):
        print(num)
        break
    else:
        cycl = False
