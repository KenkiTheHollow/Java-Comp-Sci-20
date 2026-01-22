import random

WIN_SCORE = 20


def throw_bones():
    points = 0
    output = ""

    if random.randint(0, 1) == 1:
        output += "Rectangles! "
        points += 1
    else:
        output += "Blank "

    if random.randint(0, 1) == 1:
        output += "Squares! "
        points += 1
    else:
        output += "Blank "

    if random.randint(0, 1) == 1:
        output += "Triangles! "
        points += 2
    else:
        output += "Blank "

    if random.randint(0, 1) == 1:
        output += "Circles! "
        points += 3
    else:
        output += "Blank "

    if random.randint(0, 1) == 1:
        output += "Diamonds! "
        points += 4
    else:
        output += "Blank "

    print(output)
    return points


# ---------- PART 1: odds method ----------
def odds(t):
    count = 0

    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    for E in range(2):

                        value = (1*A) + (1*B) + (2*C) + (3*D) + (4*E)

                        if value >= t:
                            count += 1

    return count / 32


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


# ---------- PART 2: improved CPU AI ----------
def cpu_turn(player_throw):
    throws = 0
    cpu_points = 0
    riskTolerance = 0.5

    while throws < 3:
        throws += 1
        print("CPU throw:", throws)

        cpu_points = throw_bones()
        print("CPU points:", cpu_points)

        if throws == 3:
            break

        chanceBeatPlayer = odds(player_throw + 1)
        chanceBeatSelf = odds(cpu_points + 1)

        if chanceBeatPlayer >= riskTolerance or chanceBeatSelf >= riskTolerance:
            continue
        else:
            break

    return cpu_points


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
