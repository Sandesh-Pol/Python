import random

class colors:
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'

def cricket_game(batting_team):
    total_runs = 0
    wickets = 0
    overs = 0

    while overs < 20 and wickets < 10:
        balls_in_over = 0
        print("\n" + "=" * 30)
        print(colors.YELLOW + "\n {} Batting \n\n Current Score: {} runs for {} wickets in {:.1f} overs".format(batting_team, total_runs, wickets, overs) + colors.END)
        print("=" * 30)

        while balls_in_over < 6 and wickets < 10:
            input(colors.GREEN + "\nPress Enter to bat..." + colors.END)
            my_list = ['one run', 'two runs', 'three runs', 'four..!', 'six...!', 'out..!', 'dot ball', 'No ball', 'Wide Ball']
            random_element = random.choice(my_list)
            print("You scored:", colors.GREEN + random_element + colors.END)

            if random_element == "out..!":
                wickets += 1
                if wickets == 10:
                    print(colors.RED + "All out!" + colors.END)
                    break
            elif random_element not in ['No ball', 'Wide Ball', 'dot ball']:
                runs_mapping = {'one run': 1, 'two runs': 2, 'three runs': 3, 'four..!': 4, 'six...!': 6}
                runs = runs_mapping.get(random_element, 0)
                total_runs += runs
            balls_in_over += 1

        overs += 0.1
        if balls_in_over == 6:
            overs = int(overs) + 1  

    print("\n" + "=" * 30)
    if overs >= 20:
        print(colors.GREEN + "All overs bowled!" + colors.END)
    print(colors.YELLOW + "Final Score: {} runs for {} wickets in {:.1f} overs".format(total_runs, wickets, overs) + colors.END)
    print("=" * 30)
    print(colors.YELLOW + "Thank you for playing!" + colors.END)

def toss(A, B):
    t = random.choice([A, B])
    print("\n{} won the toss!".format(colors.BLUE + t + colors.END))
    decision = input("\nWhat is your choice? (Press 'bat' or 'bowl'): ").lower()
    if decision == 'bat':
        return t, A if t == B else B
    elif decision == 'bowl':
        return A if t == B else B, t
    else:
        print("Invalid choice! Please choose 'bat' or 'bowl'.")
        return toss(A, B)

input("\n\n# # # # #  START GAME  # # # # # \n\n" + colors.GREEN + "( Press enter to start )" + colors.END)
team1 = input("\nEnter the name of the first team: ")
team2 = input("\nEnter the name of the second team: ")


batting_team, bowling_team = toss(team1, team2)
cricket_game(batting_team)
cricket_game(bowling_team)