

                        #This function colors the player's cells green, and, in theory, it should still blink rarely.
def PColorIN(TextStr):  #Эта функция окрашивает клетку игрока в зелёный цвет и по идее он должен ещё редко мигать

    TextStr = f"\033[5m\033[32m{TextStr}\033[0m"

    return TextStr


# a1 = "#"
# a2 = '#'
# a3 = '#'

# print(f'{a1:^2}{a2:^2}{a3:^2}')
# print ('{1} привет')
# print(f'{PColorIN(a1):^2}{a2:^2}{a3:^2}')
