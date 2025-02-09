import random

def roll_dice(): #объявление функции, что не принимает аргументы
    return sum(random.choices(range(1, 7), k=2)) # Бросает кубик дважды и суммирует

def main(): # Объявляем основную функцию main(), в которой будет логика игры.
    balances= {
        "player1": 1000,
        "player2": 1000,
        "bank": 0
    }
    result = {
        "player1": 0,
        "player2": 0
    }
    start_bot()
    dice(balances, result)

def start_bot():
    start_message = ""
    while start_message != "/start":
        start_message = input("Введите /start для начала работы ")
        if start_message != '/start' :
            print('чеел, введи команду, не выёбуся, ок?')

def dice(balances, result):
    while True:
        print(f"Ваш баланс: {int(balances["player1"])}")
        try:
            dice_message = input("Введите /dice, чтобы бросить кости (или введите /q для выхода): ").split()
            if dice_message[0] == "/dice":
                bet = int(dice_message[1])
                if bet <= balances["player1"] and bet > 0:
                    player1_roll = roll_dice()
                    player2_roll = roll_dice()

                    print(f"Ваша ставка: {bet}!")
                    print(f"Вы бросили: 🎲 {player1_roll}")
                    print(f"Второй игрок бросил: 🎲 {player2_roll}")

                    if player2_roll > player1_roll:
                        reward = update_balance("player2", "player1", bet, balances, result)
                        print(f'Второй игрок победил в этом раунде, он получает + {reward}')

                        if int(balances["player1"]) == 0:
                            game_over(balances, result)
                            break


                    elif player1_roll > player2_roll:
                        reward = update_balance("player1", "player2", bet, balances, result)
                        print(f'Вы победили в этом раунде!!! Вы получаете + {reward}')

                        if int(balances["player2"]) <= 0:
                            game_over(balances, result)
                            break

                    elif player1_roll == player2_roll:
                        print('Товарищи, ничья, победила дружба!')
                    else:
                        print("Если вы видите это сообщение, сообщите разработчику")

                else: print("Цифрами ошибся? Бедни бибизяна")
            elif dice_message[0] == "/q":
                game_over(balances, result)
                break

            else: print("Ну ты кринж, хочешь программу сломать, удачи")

        except IndexError:
            print("Хочешь подловить меня на ошибке? Ну ты наивный")
        except ValueError:
            print("Наивный х2, не на того напал, ввели /dice и число для ставки")


def update_balance(winner, loser, amount, balances, result):
    balances[loser] -= amount
    bank_commission = amount * 0.01 # 1% от ставки
    reward = amount - bank_commission
    balances['bank'] += bank_commission
    balances[winner] += reward
    result[winner] += 1
    return reward


def game_over(balances, result):
    if balances["player1"] > balances["player2"]:
        print("Хорош, чувак, победил против ИИ")
        print(f"Ваши результаты: Побед - {result["player1"]}, Баланс - {balances["player1"]}")
        print(f"Банк заработал {balances["bank"]}")
    elif balances["player1"] < balances["player2"]:
        print("К успеху шёл, в следующий раз повезёт")
        print(f"Ваши результаты: Побед - {result["player1"]}, Баланс - {balances["player1"]}")
        print(f"Банк заработал {balances["bank"]}")
    elif result["player1"] == 0 and result["player2"] == 0:
        print("Даже не попробовал сыграть((((")

    print("Спасибо за игру, чел!")




main()