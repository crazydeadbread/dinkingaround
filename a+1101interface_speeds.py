# Interface devices names and speeds

import random, os, json, sys

serial = {
    1: "802.11a", 
    2: "802.11b",
    3: "802.11g",
    4: "802.11n",
    5: "802.11ac",
    6: "802.11ax",
    7: "USB 1.1 low",
    8: "USB 1.1 high",
    9: "USB 2.0",
    10: "USB 3.0",
    11: "USB 3.1 Gen 1",
    12: "USB 3.1 Gen 2",
    13: "USB 3.2 Gen 1x2",
    14: "USB 3.2 Gen 2x2",
    15: "Thunderbolt v1", 
    16: "Thunderbolt v2",
    17: "Thunderbolt v3",
    18: "USB-C",
    19: "DVI Single Link",
    20: "DVI Dual Link",
    21: "Sata Revision 1.0",
    22: "Sata Revision 2.0",
    23: "Sata Revision 3.0",
    24: "Sata Revision 3.2",
    25: "eSata (external SATA)"
}


speed = {
    "802.11a": "54 Mbit/s",
    "802.11b": "11 Mbit/s",
    "802.11g": "54 Mbit/s",
    "802.11n": "600 Mbit/s",
    "802.11ac": "866 Mbit/s",
    "802.11ax": "1201 Mbit/s",
    "USB 1.1 low": "1.5 MBPS",
    "USB 1.1 high": "12 MBPS",
    "USB 2.0": "480 MBPS",
    "USB 3.0": "5 GBPS",
    "USB 3.1 Gen 1": "5 Gbit/s",
    "USB 3.1 Gen 2": "10 Gbit/s",
    "USB 3.2 Gen 1x2": "10 Gbit/s",
    "USB 3.2 Gen 2x2": "20 Gbit/s",
    "Thunderbolt v1": "10 Gbit/s",
    "Thunderbolt v2": "20 Gbit/s",
    "Thunderbolt v3": "40 Gbit/s",
    "USB-C": "10 Gbit/s",
    "DVI Single Link": "3.7 GBPS",
    "DVI Dual Link": "7.4 GBPS",
    "Sata Revision 1.0": "1.5 Gbit/s",
    "Sata Revision 2.0": "3.0 Gbit/s",
    "Sata Revision 3.0": "6.0 Gbit/s",
    "Sata Revision 3.2": "16 GBit/s",
    "eSata (external SATA)": "Matches SATA version"
}


# Is there a better data validation? 
def validate_choice(comparison: dict or int):
    choice = input()
    while choice != type(int):
        try: 
            # can we change it? 
            choice = int(choice)
            # Validate that it's within the range of options
            if choice not in range(len(comparison) + 1) or choice == "":
                print(f"Invalid selection, please enter an option between 1 and {len(comparison)}: ", end="")
                choice = input()
            else:
                return choice
        except:
            print(f"Invalid. Please enter an option between 1 and {len(comparison)}: ", end="")
            choice = input()
    return True


def progress():
    cont = False
    while cont == False:
        inquire = input("Continue? 1 or Y").upper()
        if inquire == 1 or inquire == "y".upper():
            cont = True
        else:
            continue



def menu_action(choice: int, comparison):
    # menu = {1: "Learn about one", 2: "Quiz on one", 3: "Quiz on all"}
    for i in range(choice + 1):
        if choice == 0:
            quit(choice)
        elif choice == 1:
            os.system('cls')
            print(f"{comparison[choice]}:\n")
            study()
            return True
        elif choice == 2:
            os.system('cls')
            print(f"{comparison[choice]}:\n")
            quiz_single()
            return True
        elif choice == 3:
            os.system('cls')
            print(f"{comparison[choice]}:\n")
            quiz_all()
            return True
        else:
            break


def quit(selection: str):
    try:
        selection = int(selection)
        if selection == 0:
            sys.exit()
            return True
    except Exception as e:
        print(f"{e}")
        return False


def study():
    for k, v in serial.items():
        print(f"{k}) {v}")
    selection = input("\nWhich port do you want to review? Enter 0 to return: ")

    try:
        selection = int(selection)
        if selection in serial.keys():
            print(f"\n{serial[selection]}:")
            print(f"Speed: {speed[serial[selection]]}")
        elif selection == "0":
            quit(selection)
        else:
            os.system('cls')
            print("***Must be an option in the menu, try again.***".upper())
    except:
        os.system('cls')
        selection = print("***Invalid input, try again.***".upper())


def quiz_single():
    for k, v in serial.items():
        print(f"{k}) {v}")
    print("\nWhich interface do you want to quiz? Enter 0 to return: ")
    
    numeric_selection = validate_choice(serial)
    which = serial[numeric_selection]

    # Build the multiple choice options here that'll be presented
    # start with a list of options. We'll shuffle this later
    options = [speed[which]]
    # init the dict for shufflin', where we'll add enumerates as the keys
    shuffle = {}
    while len(options) != 4:
        rando = random.randint(1, len(serial))
        if rando == numeric_selection:
            rando = random.randint(1, len(serial))
        rando = serial[rando]
        if speed[rando] in options:
            pass
        else:
            options.append(speed[rando])

    # Shuffle shuffle
    random.shuffle(options)
    # Add to shuffle dict with new enumeration
    for k, v in enumerate(options, 1):
        shuffle[k] = v


    print(f"What is the speed of {which}?")
    for k, v in shuffle.items():
        print(f"{k}) {v}")
     
    answer = print(f"Enter selection: {validate_choice(range(4))}")
    if shuffle[answer] == speed[which]:
        print("\nCorrect!")
    else:
        print(f"\nIncorrect. {which}'s speed is {speed[which]}.")


def quiz_all():
    # Thinking of making a dictionary of dictionaries
    correct = 0
    total = 0
    randomizer = list(range(1, len(serial) + 1))

    while len(randomizer) > 0:
        i = random.choice(randomizer)
        which = serial[i]

        options = [speed[which]]
    # init the dict for shufflin', where we'll add enumerates as the keys
        shuffle = {}
        while len(options) != 4:
            rando = random.randint(1, len(serial))
            rando = serial[rando]
            if speed[rando] in options:
                pass
            else:
                options.append(speed[rando])

        # Shuffle shuffle
        random.shuffle(options)
        # Add to shuffle dict with new enumeration
        for k, v in enumerate(options, 1):
            shuffle[k] = v


        print(f"What is the speed of {which}?")
        for k, v in shuffle.items():
            print(f"{k}) {v}")
        print(f"Enter selection: ", end="")
        answer = validate_choice(range(4))
        if shuffle[answer] == speed[which]:
            print("\nCorrect!\n")
            correct += 1
            total += 1
        else:
            print(f"\nIncorrect. {which}'s speed is {speed[which]}.")
            total +=1 
    
        print(f"{'*' * 3} {which} Quiz Results: {'*' * 3}")
        
        percentage_correct = correct/total
        print(f"\n\nTotal Correct: {correct}/{total}")    
        print(f"Total Incorrect: {total - correct}/{total}")
        print(f"Overall Grade = {percentage_correct:.0%}\n\n")
        
        randomizer.remove(i)
        input("Press enter to continue.")
        os.system("cls")
    return correct
    

def main():
    while True:
        # options, either pull up info about individual ports or do quiz for all
        print("\n\nMain Menu:")
        menu = {1: "Learn about one", 2: "Quiz on one", 3: "Quiz on all"}
        for k, v in menu.items():
            print(f"{k}) {v}", end=" "*10)
        print("")

        choice = validate_choice(menu)
        menu_action(choice, menu)

if __name__ == "__main__":
    main()


"""
###Code to later im/export the above dictionaries as txt or json.###

dict_consolidate = {"serial": serial,
                    "abbreviations": abbreviations,
                    "port_type": port_type,
                    "port_number_in": port_number_in,
                    "port_number_out": port_number_out}

with open("port_info.json", 'w') as fp:
    json.dump(serial, fp, indent=4)
    json.dump(abbreviations, fp, indent=4)
    json.dump(port_type, fp, indent=4)
    json.dump(port_number_in, fp, indent=4)
    json.dump(port_number_out, fp, indent=4)

    for i in range(len(dict_consolidate)):
        json_string = json.dumps(dict_consolidate, indent=4)
        # print(json_string)
        # print(type(json_string[i]))
        json.dump(json_string, fp)

    does_it_work = json.load(fp)
    print(does_it_work)

"""