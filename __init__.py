import word

menu = "Вы находитесь в главном меню."
user_game = "Играть (y/p) "
user_exit = "Выход (e/q)"
button = [["y", "p"], ["e", "q"]]
print("Добро пожаловать на казнь!")

def main_menu():
    user = input(f"\n{menu}\n{user_game:_^30}\n{user_exit:_^30}\nВаш выбор :")
    if user.lower() in button[0]:
        return game()
    elif user.lower() in button[1]:
        exit()
    else:
        return main_menu()


def game():
    slovo = word.random_word()
    wrong = 0
    gallows = ["",
                   "_________        ",
                   "        |        ",
                   "        0        ",
                   "       /|\       ",
                   "       / \       "
                   ]
    rleaters = list(slovo)
    code_word = ["_"] * len(slovo)
    win = False

    while wrong < len(gallows) - 1:
        print(f"\nотгадайте слово: {''.join(code_word)}")
        msg = "Введите букву: "
        char = input(msg)
        if char.lower() in rleaters:
            temp = rleaters.index(char)
            code_word[temp] = char
            rleaters[temp] = "$"
            print("".join(code_word))
        else:
            wrong += 1
            print(*gallows[0:wrong + 1], sep="\n")
        if "_" not in code_word:
            win = True
            print(f"Вы выйграли! Было загадано слово: {''.join(code_word)}")
            return main_menu()
    if win is not True:
        print(f"Вы проиграли :-(\nБыло загадано слово: {slovo}")
        return main_menu()

main_menu()