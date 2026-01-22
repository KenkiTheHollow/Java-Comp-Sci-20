import random

WIN_SCORE = 20


def throw_bones():
    points = 0
    output = ""

    # Bone 1: Rectangles (1 point)
    if random.randint(0, 1) == 1:
        output += "Rectangles! "
        points += 1
    else:
        output += "Blank "

    # Bone 2: Squares (1 point)
    if random.randint(0, 1) == 1:
        output += "Squares! "
        points += 1
    else:
        output += "Blank "

    # Bone 3: Triangles (2 points)
    if random.randint(0, 1) == 1:
        output += "Triangles! "
        points += 2
    else:
        output += "Blank "

    # Bone 4: Circles (3 points)
    if random.randint(0, 1) == 1:
        output += "Circles! "
        points += 3
    else:
        output += "Blank "

    # Bone 5: Diamonds (4 points)
    if random.randint(0, 1) == 1:
        output += "Diamonds! "
        points += 4
    else:
        output += "Blank "

    print(output)
    return points


def player_turn():
    throws = 0
    last_points = 0
    choice = "y"

    while throws < 3 and choice == "y":
        throws += 1
        print("Player throw:", throws)

        last_points = throw_bones()
        print("Your points:", last_points)

        if throws < 3:
            choice = input("Do you want to throw again (y/n)? ")

    return last_points


def cpu_turn(player_points):
    throws = 0
    last_points = 0

    while throws < 3:
        throws += 1
        print("CPU throw:", throws)

        last_points = throw_bones()
        print("CPU points:", last_points)

        if last_points >= player_points:
            break

    return last_points


def main():
    player_score = 0
    cpu_score = 0

    print("Welcome to the Bone Game")
    print("========================")

    while player_score < WIN_SCORE and cpu_score < WIN_SCORE:
        print("Player:", player_score, "CPU:", cpu_score)
        print("========================")

        p = player_turn()
        player_score += p

        c = cpu_turn(p)
        cpu_score += c

        print("Scores:")
        print("Player:", player_score)
        print("CPU:", cpu_score)
        print()

    if player_score > cpu_score:
        print("Player wins!")
    elif cpu_score > player_score:
        print("CPU wins!")
    else:
        print("It's a tie!")


main()
