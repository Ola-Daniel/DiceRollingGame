

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
    

num_dice_input = input("How many dice do you want to roll?")
num_dice = parse_input(num_dice_input)


