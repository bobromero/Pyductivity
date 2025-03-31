import weekly
import daily


# motivationa_quote =
def get_weekly_reminder():
    try:
        weekly_focus = weekly.display_weekly()
    except:
        weekly_focus = "weekly reminder not set"
    return weekly_focus


main_prompt = f"""
    Welcome to Pyductivity!
    motivational_quote
    This week, remember to focus on
    {get_weekly_reminder()}
    A. Today's notes
    B. Todo Lists
    C. Weekly Reminders    
    Enter to exit
    """


def main_path():
    try:
        choice = input(main_prompt)
        if choice == "A" or choice == "a":
            daily.daily_path()

        elif choice == "B" or choice == "b":
            pass

        elif choice == "C" or choice == "c":
            weekly.weekly_path()
        elif choice == "":
            exit()
        else:
            print("invalid input: try again")
    except KeyboardInterrupt:
        print("\n")
        exit()
    except Exception as e:
        print("exiting", e)
        exit()


while True:
    main_path()
