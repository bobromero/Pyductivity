import weekly
import daily

# motivationa_quote =
weekly_reminder_list = weekly.display_weekly()
main_prompt = f"""
    Welcome to Pyductivity!
    motivational_quote
    This week, remember to focus on
    {weekly_reminder_list}
    A. Today's notes
    B. Todo Lists
    C. Weekly Reminders    
    Enter to exit
    """


def main_path():
    choice = input(main_prompt)

    if choice == "A" or choice == "a":
        daily.daily_path()

    elif choice == "B" or choice == "b":
        pass

    elif choice == "C" or choice == "c":
        weekly.weekly_path()
    elif choice == "":
        return -1
    else:
        print("invalid input: try again")
    return 0


val = 0
while val >= 0:
    val = main_path()
