import random

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def cricket_game():
    total_runs = 0
    wickets = 0
    overs = 0

    while overs < 1 and wickets < 5:
        balls_in_over = 0
        print("\n" + "=" * 30)
        print(colors.YELLOW + "Current Score: {} runs for {} wickets in {:.1f} overs".format(total_runs, wickets, overs) + colors.END)
        print("=" * 30)

        while balls_in_over < 6 and wickets < 5:
            input(colors.GREEN + "\nPress Enter to bat..." + colors.END)
            my_list = ['one run', 'two runs', 'three runs', 'four..!', 'six...!', 'out..!', 'dot ball', 'No ball', 'Wide Ball']
            random_element = random.choice(my_list)
            print("You scored:", colors.GREEN + random_element + colors.END)

            if random_element == "out..!":
                wickets += 1
            elif random_element not in ['No ball', 'Wide Ball', 'dot ball']:
                runs_mapping = {'one run': 1, 'two runs': 2, 'three runs': 3, 'four..!': 4, 'six...!': 6}
                runs = runs_mapping.get(random_element, 0)
                total_runs += runs
            balls_in_over += 1

        overs += 0.1
        if balls_in_over == 6:
            overs = int(overs) + 1  

    print("\n" + "=" * 30)
    if wickets == 5:
        print(colors.RED + "All out!" + colors.END)
    else:
        print(colors.GREEN + "All overs bowled!" + colors.END)
    print(colors.YELLOW + "Final Score: {} runs for {} wickets in {:.1f} overs".format(total_runs, wickets, overs) + colors.END)
    print("=" * 30)
    print(colors.YELLOW + "Thank you for playing!" + colors.END)

cricket_game()
