import random


class Barrel:
    def __init__(self, num_barrels, start=0):
        self.i = start
        self.num_barrels = num_barrels
        self.stock = [_ for _ in range(1, num_barrels)]

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.num_barrels:
            random.shuffle(self.stock)
            item = random.choice(self.stock)
            self.stock.remove(item)
            return item
        else:
            print("No more barrels.")
            raise StopIteration


class Card:
    def __init__(self, player, card):
        self.player = player
        self.card = card

    def check_card_number(self, number):
        for x in self.card:
            for num in x:
                if num == number:
                    return True
        return False

    def cross_number(self, number):
        for x in self.card:
            for i, num in enumerate(x):
                if num == number:
                    x[i] = '-'
                    return True
        return False

    def check_for_win(self):
        for x in self.card:
            for num in x:
                if num != '' and num != '-':
                    return False
        return True

    def show_card(self):
        if self.player == "Your":
            s = 11                                   # разделитель карт игроков, для удобства
        else:
            s = 7
        print(f"{'-' * 10}{self.player} card{'-' * s}")
        for el in self.card:
            for nums in el:
                print(f'{nums:<2}', end='  ')
            print("")
        print(f"{'-' * 30}")


def generate_card():
    tmp = sorted(random.sample(range(1, 90), 15))       # числа в картах не должны повторяться,
    numbers = [tmp[0:5], tmp[5:10], tmp[10:15]]         # (поэтому генерирую их вместе)
    card = [[''] * 9 for _ in range(0, 3)]              # пустая карта
    for i in range(3):
        pos = sorted(random.sample(range(0, 8), 5))     # случайные позиции номеров в картах
        for j in range(5):
            num = numbers[i][j]
            card[i][pos[j]] = num
    return card


def start_game():
    barrel_obj = Barrel(90, 0)
    user = Card("Your", generate_card())
    computer = Card("Computer", generate_card())
    for num in barrel_obj:
        print(f"\nNew barrel: {num} (left: {barrel_obj.num_barrels - barrel_obj.i})")
        user.show_card()
        computer.show_card()
        decision = 0
        while decision != 'y' and decision != 'n':
            decision = input("Cross out the number? y/n ")
        if decision == 'y':
            if user.check_card_number(num):
                if user.cross_number(num):
                    if user.check_for_win():
                        print("You won.")
                        break
            else:
                print("You loose. You couldn't cross out the number.")
                break
            if computer.cross_number(num):
                if computer.check_for_win():
                    print("Computer won.")
                    break
        elif decision == 'n':
            if user.check_card_number(num):
                print("You loose. You should have crossed out the number.")
                break
            if computer.cross_number(num):
                if computer.check_for_win():
                    print("Computer won.")
                    break


start_game()
