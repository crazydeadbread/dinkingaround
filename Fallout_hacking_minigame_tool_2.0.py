import os

"""
V1 would work linearly. Enter word, next ask to remove word, next ask update match counts, next ask to sort.
So much asking! New idea: always display the words and matches, and give the user the option to take their action
without needing to go in a linear sequence.
"""

print("\n\n*** Fallout Terminal Hacking ***\n\nInstructions:")
print("- Input your first word you guessed in Fallout, and how many matches it had.")
print("- Each new word you enter must be the same length as the original. This is a requirement of the mini-game and mitigates check for too few/many characters.")
print("- Each new word you enter will automatically be assigned matches against the first word in the list. (You can change these counts if you wish.)")
print("- You can test words before you guess them in Fallout. See which letters match with your best word here before you use an attempt in the game.")
print("- You can remove words if it was a bad guess, misspelled, etc. ")
print("- You can sort the list to prioritize which word has the most matches and compare against that instead of your first guess.\n")


# Start with the first word guessed in Fallout, and what the match count said it was.
# For anyone else taking a peek - if True means the user will be prompted to input. This will be the defaul tin the live environment.
# if False means we're going to use the hardcoded sample word/match in the else statement. Only used for testing.
while True:
    if True:
        start = input("First word: ").upper()
        count = input("How many matched: ")
        while type(count) != int:
            try:
                count = int(count)
            except:
                print("Must be a number. Try again:")
        print("")
    else:
        start = "patio".upper()
        count = 2
        
   
def menu_action(choice: int, existing: dict, pointer_lines: dict, menu: dict):
    # When the user enters their menu choice (choice: int), this is what is going to guide the program to which functions to execute.
    # The menu options are in the menu variable in the main() function. But so it's easily referenced here:
    # menu = {1: "Enter new word", 2: "Remove a word", 3: "Update match counts", 4: "Sort", 5: "Restart", 6: "Exit"}
    for k in range(choice + 1):
        k = choice
        if k == 1:
            # Enter a new word:
            word = validate_compare()
            # This is the "back" option. If they selected "enter new word" by mistake, they can return to the menu.
            if word == "0":
                break
            # Confirm if it's already in the dict - without this, it'd just replace the existing key/value pair.
            word = already_used(existing, word)
            # Automatically apply matches to the most matched word in the dict.
            new_match = auto_match(existing, word)
            # Add it to the dict.
            existing[word] = new_match
            return True
        elif k == 2:
            # Remove a word
            removal(existing)
            return existing
        elif k == 3:
            # Update match counts
            update_match(existing)
            return existing
        elif k == 4:
            # Sort
            existing = sort(existing)
            return existing
        elif k == 5:
            # Discard everything and start from the beginning. Great if you leave the program up and running and come to a 2nd 
            # terminal in the game.
            restart()
            return False
        elif k == 6:
            # Kill the program.
            # 
            exit_check()


def validate_choice(choice: str):
    # We must ensure that the menu option is simply an int between 1-6. Any other entry will break the program.
    while type(choice) != int:
        try:
            choice = int(choice)
            if choice not in range(1, 7):
                print(f"Invalid selection, please enter an option between 1 and 6")
                choice = input()
        except:
            print(f"Invalid selection, please enter an option between 1 and 6")
            choice = input()
    return choice


def validate_compare():
    # THis is called within menu_action() function. 
    # while True: run until the entry is valid and we hit a return.
    while True:
        compare = input("Enter word (or press 0 to return to menu): ")
        # "0" will cancel this and return them to the main menu.
        # This will pass str("0") back to menu_function() to break and return to the main() function.
        # No need to convert to int. No one's going to enter a word where the single character is "0". Doesn't exist in Fallout.
        if compare == "0":
            return compare
        # Check to ensure length is correct. No point in coninuing if it's to be 7 and someone typed 6 or 8 chars.
        elif len(compare) != len(start):
            print(f"\n{compare.upper()} is {len(compare)} characters long, {start} is {len(start)}. Word length must match - try again.")
        # Return upper for consistency, and matches game format.
        else:
            return compare.upper()


def already_used(existing: dict, word: str, count=int):
    # My pisspoor excuse for exception handling. Writing my own function to check if a word's already in the dict.
    # Start with used = True because we consider it used until proven otherwise. Then used == False, and we continue on.
    used = True
    while used == True:
        # Compare with existing words:
        if str(word) in existing.keys():
            # Re-enter if it's already present.
            print(f"{word} already used. Try again.")
            word = validate_compare()
        else:
            used = False
    # Return the word that triggered False.
    return word


def removal(existing: dict):
    # while True: we must keep running in case they make an invalid selection. If there's 2 entries in the dict, and they enter "3",
    # The except in the else at the bottom of the function will print, and it'll loop back to try again or back out.
    while True:
        # We're using selection variable to serialize the keys (which are strings) and display them.
        selection = {}
        for number in range(len(existing)):
            # We begin serializing. We start at 0 because we'll need to start at the index from list(existing) 
            # This will add the number from range(len(existing)) as the key, then the word from existing as the index position.
            # Index in dict starts at 0, but we need the new menu to start at 1. So selection[number + 1]. Then add first word in dict (index 0)
            # list(existing) will only return the keys, which is what we want.
            selection[number + 1] = list(existing)[number]
        print("Enter number next to the word you wish to remove. Press 0 to return.\n")
        for k, v in selection.items():
            # Display selection: dict
            print(f"{k}) {v}")
            print(end="")
        # The validate variable below will ensure the user's entering a number and nothing else.
        validate = 0
        while validate == 0:
            decision = input("Number: ")
            try:
                decision = int(decision)
                validate = 1
            except:
                print(f"Must be a number. Try again.")
        # 0 is the universal code in this program to cancel, so it just returns the dict untouched and menu_action returns back to main()
        if decision == 0:
            return existing
        else:
            # See if the decision they entered is in the list. If they type in 3 but there's only 2 options, this forces them to select
            # a valid one.
            try: 
                existing.pop(selection[decision])
                return existing
            except:
                print(f"{decision} is not in the list. Try again")


def auto_match(existing: dict, word: str):
    # automatically counts which letters match with the first entry in existing parameter.
    ### I may add option to manually input matches. I started that way, but automated it. Will later build an option for manual entry every time.
    new_match = 0
    for k, v in existing.items():
        best_match = k
        for index in range(len(word)):
            if word[index] == best_match[index]:
                new_match += 1
        # This return returns it after only comparing with the first word in existing: dict. The idea is that the first one is the best match,
        # and the dict has been sorted using sort(). They can always update the counts manually after entry, and I may add manual_match() later.
        return new_match


"""
# If I decide to integrate manual matching instead of auto, this is a base.
def manual_match(existing: dict, word: str):
    new_match = input("New number: ")
    while True:
        try:
            new_match = int(new_match)
        except:
            new_match = input(f"Must be a number. Try again: ")
        if type(new_match) == int:
            existing[word] = new_match
        return existing
"""


def update_match(existing: dict):
    # while True: we must keep running in case they make an invalid selection and need to try again.
    while True:
        # Same as removal. We're using this selection variable to serialize the keys (which are strings) and display them.
        selection = {}
        # We begin serializing. We start at 0 because we'll need to start at the index from list(existing) 
        # This will add the number from range(len(existing)) as the key, then the word from existing as the index position.
        # Index in dict starts at 0, but we need the new menu to start at 1. So selection[number + 1]. Then add first word in dict (index 0)
        # list(existing) will only return the keys, which is what we want.
        for number in range(len(existing)):
            selection[number + 1] = list(existing)[number]
        print("Enter the number of which word to update. Press 0 to return.\n")
        for k, v in selection.items():
            # Display the items.
            print(f"{k}) {v} - {existing[v]}")
        validate = 0
        # The validate variable below will ensure the user's entering a number and nothing else.
        while validate == 0:
            decision = input("Number: ")
            try:
                decision = int(decision)
                validate = 1
            except:
                print(f"Must be a number. Try again.")
        if decision == 0:
            # 0 is the universal code in this program to cancel, so it just returns the dict untouched and menu_action returns back to main()
            return existing
        else:
            # This function is almost identical with removal() up to this point. Really the only difference is what happens in this else statement.
            # Which is to update the value for existing(selection[decision]) key.
            update = int(input(f"New value for {selection[decision]}: "))
            existing[selection[decision]] = update
            return existing

"""
def sort(existing: dict):
    # Motherfucking sort isn't modifiing the motherfucking dictionary directly. 
    # With dict {'AGREE': 1, 'PATIO': 2, 'RADIO': 3}, debugger/breakpoint shows 
    # "(return) <dictcomp:> {'RADIO': 3, 'PATIO': 2, 'AGREE': 1}" after the sort code below runs.
    # But even though I say "existing = " with the sort code, the "existing" var doesn't change.
    # 
    # existing = {k: v for k, v in sorted(existing.items(), key=lambda item: item[-1], reverse=True)}
    # existing = {}
    # for k, v in new_order.items():
    #     existing[k] = v
    return existing
"""

def sort(existing: dict):
    # Sort using existing and lambda, saving the new dict into new_order
    new_order = {k: v for k, v in sorted(existing.items(), key=lambda item: item[-1], reverse=True)}
    # clear existing
    existing.clear()
    # add key/value pairs from new_order into existing.
    for key, value in new_order.items():
        existing[key] = value


def drawing(existing: dict, current_drawing: dict):
    # This is waht's going to draw the space " " and pipe "|" between the matching letters.
    # We'll need a dict to contain the words, and the matches.
    draw = {}
    counter = 0
    start = ""
    for k, v in existing.items():
        # empty string to put the " " and "|" into. This will empty each time this starts over - with each new word.
        drawing = ""
        if counter == 0:
            # The first word in the dictionary goes into start variable. This is what all the others will compare against.
            start = k
            # Counter only used this once. Everything that happens from here will be int he else statement.
            counter += 1
        else:
            for i in range(len(k)):
                # If it matches, draw a pipe "|"
                if k[i] == start[i]:
                    drawing = drawing + "|"
                # otherwise, draw a space space " "
                elif k[i] != start[i]:
                    drawing = drawing + " "
            # Add to drawing dict
            current_drawing[k] = drawing
    return current_drawing


def printer(data: dict, draw: dict, word: str):
    # printer() gives the display the nice =-=-=- border and is what prints the words, then the pipes
    start = ""
    counter = 0
    print("=-" * (11 + (len(word) // 2)), end="\n")
    for k, v in data.items():
        # We have to print the first word before any pipes. So we tell it explicitly to do so here, and counter += 1.
        if counter == 0:
            start = k
            print(f"Word: {k} - Matches: {v}/{len(k)}")
            counter += 1
        # After that's done everything else are the pipes and rest of the words.
        else:
            # draw spaces+pipes
            print((" " * 6) + draw[k])
            # Print next word, just as we did in the if statement above.
            print(f"Word: {k} - Matches: {v}/{len(k)}")
    print("=-" * (11 + (len(word) // 2)))


def restart():
    # Restart option in case someone leaves the program up and running while playing Fallout and comes to another minigame instance.
    # Great so they don't have to quit this and restart it each time.
    # First, give them an opportunity to back out.
    confirm = input("Are you sure you want to restart? All current information will be discarded.\n Y or 1 to confirm, enter anything else to return.\n").upper()
    if confirm == "Y" or confirm == "1":
        # We are basically doing everything we have already done. Just reinitialize all the things.
        # Had to learn how to call the GLOBAL variable to do this. 
        global start
        start = input("First word: ").upper()
        global count
        count = int(input("How many matched: "))
        # So really re-prompt for new start/count variables, and rerun main again.
        return main(start, count)
    else:
        return True


def exit_check():
    # Same as restart - give them an option to back out.
    confirm = input("Are you sure you want to exit?\nY or 1 to confirm, enter anything else to return.\n").upper()
    if confirm == "Y" or confirm == "1":
        import sys
        print("*** Exiting ***")
        sys.exit()
    # Return something, though it doesn't matter. sys.exit() already exited.
    return False
            

def main(word: str, match: int):
    attempts = {word: match}
    # attempts = {'PATIO': 2, 'RADIO': 3, 'AGREE': 1} ### HARDCODED EXAMPLES FOR TESTING - NO TOUCHY.
    pointer_lines = {}
    menu = {1: "Enter new word", 2: "Remove a word", 3: "Update match counts", 4: "Sort matches (highest to lowest)", 5: "Restart", 6: "Exit"}
    while True:
        print("")
        # Display what we have thus far before presenting the menu
        # Generate the drawing. On first iteration, there's nothing yet.
        drawing(attempts, pointer_lines)
        # Print the words and drawings (if any)
        printer(attempts, pointer_lines, start)
        # display the menu options 
        print("\nSelect a number:")
        for k, v in menu.items():
            print(f"{k}) {v}", end=" " * 10)
        print("")
        
        # Have them enter the menu selection/number, validate will ensure it's between 1-6.
        choice = input()
        choice = validate_choice(choice)

        # menu_action() is the powerhouse, more than main(). It's what calls the other functions whereas this just calls printer and menu.
        menu_action(choice, attempts, pointer_lines, menu)
        # Much cleaner to clear the screen after every menu selection rather than have it just cascade down and clutter the terminal window.
        os.system('cls')
    return True

if __name__ == "__main__":
    main(start, count)
