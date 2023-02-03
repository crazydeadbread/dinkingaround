import random, os, json, sys

serial = {
    1: "FTP", 
    2: "SSH",
    3: "Telnet",
    4: "SMTP",
    5: "DNS",
    6: "DHCP",
    7: "HTTP",
    8: "HTTPS",
    9: "POP3",
    10: "IMAP",
    11: "SMB",
    12: "SNMP",
    13: "LDAP",
    14: "RDP"
}

abbreviations = {
    "FTP": "File Transfer Protocol", 
    "SSH": "Secure Shell", 
    "Telnet": "Telecommunication Network",
    "SMTP": "Simple Mail Transfer Protocol",
    "DNS": "Domain Name Service", 
    "DHCP": "Dynamic Host Configuration Protocol", 
    "HTTP": "Hypertext Transfer Protocol", 
    "HTTPS": "Hypertext Transfer Protocol Secure", 
    "POP3": "Post Office Protocol 3", 
    "IMAP": "Internet Message Access Protocol", 
    "SMB": "Server Message Block",
    "SNMP": "Simple Network Management Protocol", 
    "LDAP": "Lightweight Directory Access Protocol", 
    "RDP": "Remote Desktop Protocol"
}

port_type = {
    "FTP": "TCP", 
    "SSH": "TCP", 
    "Telnet": "TCP",
    "SMTP": "TCP", 
    "DNS": "UDP", 
    "DHCP": "UDP", 
    "HTTP": "TCP", 
    "HTTPS": "TCP", 
    "POP3": "TCP", 
    "IMAP": "TCP", 
    "SMB": "UDP/TCP",
    "SNMP": "UDP", 
    "LDAP": "TCP", 
    "RDP": "TCP"
}

port_number_out = {
    "FTP": "20", 
    "SSH": "22", 
    "Telnet": "23",
    "SMTP": "25", 
    "DNS": "53", 
    "DHCP": "67", 
    "HTTP": "80", 
    "HTTPS": "443", 
    "POP3": "110", 
    "IMAP": "143", 
    "SMB": "137",
    "SNMP": "161", 
    "LDAP": "389", 
    "RDP": "3389"
}

port_number_in = {
    "FTP": "21",
    "SSH": "22",
    "Telnet": "23",
    "SMTP": "25",
    "DNS": "53",
    "DHCP": "68",
    "HTTP": "80",
    "HTTPS": "443",
    "POP3": "110",
    "IMAP": "143",
    "SMB": "139",
    "SNMP": "162",
    "LDAP": "389",
    "RDP": "3389"
}

# This is going to be additional information, such as the "what is the ephemeral port range (1024-65535)?"
other_port_info = {}

def validate_choice(comparison: dict or int):
    choice = input()
    while choice != type(int):
        try:
            choice = int(choice)
            if choice not in range(len(comparison) + 1):
                print(f"Invalid selection, please enter an option between 1 and {len(comparison)}.")
                choice = input()
            else:
                return choice
        except:
            print(f"Invalid. Please enter an option between 1 and {len(comparison)}.")
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
            print(f"Full Name: {abbreviations[serial[selection]]}")
            print(f"Port Type: {port_type[serial[selection]]}")
            print(f"Port Number Out (Send): {port_number_out[serial[selection]]}")
            print(f"Port Number In (Recieve): {port_number_in[serial[selection]]}")
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
    print("\nWhich port do you want to quiz? Enter 0 to return: ")
    
    which = validate_choice(serial)
    which = serial[which]
    correct = 0


    record = {
        "Short code": which,
        "Full name": "", 
        "Port Type (or both)": "", 
        "Port Number Out": "",
        "Port Number In": ""
    }
    compare = {
        "Short code": which,
        "Full name": abbreviations[which], 
        "Port Type (or both)": port_type[which], 
        "Port Number Out": port_number_out[which],
        "Port Number In": port_number_in[which]
}
    q1 = input(f"What is the full name for {which}? ")
    q2 = input(f"What is the port type for {which}? (if both, enter TCP/UDP or UDP/TCP for OUT/IN (out first))")
    q3 = input(f"What is the outbound port number for {which}? ")
    q4 = input(f"What is the inbound port number for {which}? ")

    record["Full name"] = q1.title()
    record["Port Type (or both)"] = q2.upper()
    record["Port Number Out"] = q3
    record["Port Number In"] = q4

    print(f"\n\n\n{which} Quiz Results:")


    # Running results/stats. 

    for k, v in compare.items():
        if k == "Short code":
            pass
        else:
            if record[k] == compare[k]:
                print(f"{k}: {record[k]} - correct!")
                correct += 1
            else:
                print(f"{k} - incorrect. You entered {record[k]}, the correct answer is {compare[k]}")

    print(f"\nCorrect: {correct}/4")    
    print(f"Incorrect: {4-correct}/4")
    print(f"Grade = {correct/4:.0%}")


def quiz_all():
    # Thinking of making a dictionary of dictionaries
    correct = 0
    total = 0
    randomizer = list(range(1, len(serial) + 1))

    while len(randomizer) > 0:
        i = random.choice(randomizer)
        which = serial[i]
        print(f"{which}")

        record = {
            "Short code": which,
            "Full name": "", 
            "Port Type (or both)": "".upper(), 
            "Port Number Out": "",
            "Port Number In": ""
        }
        
        compare = {
            "Short code": which,
            "Full name": abbreviations[which], 
            "Port Type (or both)": port_type[which], 
            "Port Number Out": port_number_out[which],
            "Port Number In": port_number_in[which]
        }
        q1 = input(f"what is the full name for {which}? ")
        q2 = input(f"what is the port type for {which}? (if both TCP and UDP, regardless of order, enter \"both\") ")
        q3 = input(f"what is the outbound port number for {which}? ")
        q4 = input(f"what is the inbound port number for {which}? ")
    
        record["Full name"] = q1.title()
        record["Port Type (or both)"] = q2.upper()
        record["Port Number Out"] = q3
        record["Port Number In"] = q4

        print(f"\n\n\n{which} Quiz Results:")

        for k, v in compare.items():
            if k == "Short code":
                pass
            else:
                if record[k] == compare[k]:
                    print(f"{k}: {record[k]} - correct!")
                    correct += 1
                    total += 1
                else:
                    print(f"{k}: \"{record[k]}\" is incorrect. The correct answer is {compare[k]}")
                    total += 1
        
        percentage_correct = correct/total
        print(f"\n\nTotal Correct: {correct}/{total}")    
        print(f"Total Incorrect: {total - correct}/{total}")
        print(f"Overall Grade = {percentage_correct:.0%}\n\n")
        
        randomizer.remove(i)
        input("Press enter to continue.")
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

    # quiz_single(1)




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