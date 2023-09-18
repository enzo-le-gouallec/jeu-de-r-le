import random
import sys


player_1 = 50
player_2 = 50
potion_number = 3
potion = random.randint(15, 50)
attack_player_one = random.randint(5, 10)
attack_player_two = random.randint(5, 15)


while True:

    if player_2 < 1:
        print("Tu as gagné💪")
        print("Fin du jeu")
        sys.exit()
    if player_1 < 1:
        print("tu as perdu👎")
        print("Fin du jeu")
        sys.exit()

    game = input("Souhetez vous ataquez (1) ou utiliser une potion (2) ?")
    if game == "1":
        player_2 -= attack_player_one
        print(
            f"Vous avez infligé {attack_player_one} point de dégats à l'ennemi ⚔")

        if player_2 <= 0:
            print("Il reste 0 points de vie a l'ennemie")
            print("-" * 80)

        elif player_2 > 0:
            player_1 -= attack_player_two
            print(
                f"L'ennemis vous a infligé {attack_player_two} point de dégats ⚔")
            if player_1 <= 0 :
                print("il vous restes 0  point de vie")
            elif player_1 > 0 :
                print(f"Il vous reste {player_1} points de vie")
            print(f"Il reste {player_2} points de vie a l'ennemie")
            print("-" * 80)
        elif player_2 > 0:
            player_1 -= attack_player_two
            print("-" * 80)
    elif game == "2" and potion_number > 0:
        player_1 = player_1 + potion
        potion_number -= 1
        print(potion_number)
        print(f"Votre vitalité est maintenant de {player_1} ❤")
        print(f'Il vous reste {potion_number} potions 🧪')
        player_1 -= attack_player_two
        print(
            f"L'ennemis vous a infligé {attack_player_two} point de dégats ⚔")
        print(f"Il vous reste {player_1} points de vie ❤")
        print("-" * 80)
        print("Vous passez votre tour")
        player_1 -= attack_player_two
        print(
            f"L'ennemis vous a infligé {attack_player_two} point de dégats ⚔")
        print(f"Il vous reste {player_1} points de vie ❤")
        print("-" * 80)
    elif game == "2" and potion_number == 0:
        print("Il ne vous reste plus de potion")
