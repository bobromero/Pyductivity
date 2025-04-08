import weekly
import subprocess
import daily


# motivationa_quote =
def get_weekly_reminder():
    try:
        weekly_focus = weekly.display_weekly()
    except:
        weekly_focus = "Set your weekly focuses!"
    return weekly_focus


main_prompt = f"""
    Welcome to Pyductivity!

    This week, remember to focus on

    {' '.join(map(str, get_weekly_reminder()))}

    A. Today's notes
    B. Todo Lists
    C. Weekly Reminders    
    Enter to exit
    """


def main_path():
    try:
        subprocess.run(["clear"])
        choice = input(main_prompt)
        if choice == "A" or choice == "a":
            try:
                daily.daily_path()
            except FileNotFoundError:
                print("daily file not found, setting up file")
                daily.daily_setup()
                daily.daily_path()

        elif choice == "B" or choice == "b":
            try:
                pass
            except FileNotFoundError:
                print("todo file not found, setting up file")

        elif choice == "C" or choice == "c":
            try:
                weekly.weekly_path()
            except FileNotFoundError:
                print("weekly file not found, setting up file")
                weekly.weekly_setup("weekly")
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
