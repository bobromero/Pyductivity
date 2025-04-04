from file_modifier import file_reader, file_writer
import subprocess
import datetime

weekly_file = "../data/weekly.pk"

weekly_prompt = f"""
    Enter a choice:

    A. Add an item to the weekly list 
    B. Remove an item from the weekly list
    Enter to go back
    """


def load_weekly():
    return file_reader(weekly_file)


def save_weekly(data):
    file_writer(weekly_file, data)


def weekly_setup():
    isocalendar = datetime.date.today().isocalendar()
    data = [0, isocalendar.week, ["Do more work"]]
    try:
        data = load_weekly()
    except:
        print(f"Error: could not load data from {weekly_file}")
        print("Creating a new list")
    print(data)
    clean_weekly_index(data)
    save_weekly(data)


def weekly_index(data):
    isocalendar = datetime.date.today().isocalendar()

    def change_week_data():
        data[1] = isocalendar.week
        data[0] += 1
        if data[0] >= len(data[2]):
            data[0] %= len(data[2]) - 1

    if data[1] != isocalendar.week:
        # the week has changed
        change_week_data()


def display_weekly():
    data = []
    try:
        data = load_weekly()
    except:
        print(f"couldn't load weekly")

    weekly_index(data)
    return data[2][data[0]]


def print_weekly(data):
    for i in range(len(data[2])):
        print("\t", i + 1, ":", data[2][i], end="\n")


def clean_weekly_index(data):
    if data[0] >= len(data[2]):
        data[0] = len(data[2]) - 1


def add_to_weekly(data, info):
    data[2].append(info)
    clean_weekly_index(data)


def remove_from_weekly(data, index):
    data[2].pop(index)
    clean_weekly_index(data)


def weekly_path():
    subprocess.run(["clear"])

    print(
        """
    Welcome to the your weekly focuses!
        """
    )
    value = ""
    weekly_choice = " "
    weekly_data = load_weekly()
    clean_weekly_index(weekly_data)
    print_weekly(weekly_data)
    while weekly_choice != "":
        weekly_choice = input(weekly_prompt)
        if weekly_choice == "A" or weekly_choice == "a":
            value = input("Enter an item to add on the list\n")
            if len(value) <= 0:
                print("nothing added")
            else:
                add_to_weekly(weekly_data, value)
                print("added", value)
                save_weekly(weekly_data)
        if weekly_choice == "B" or weekly_choice == "b":
            print_weekly(weekly_data)
            try:
                value = int(input("Enter the index of the item you want to remove\n"))
                if type(value) == type(0):
                    remove_from_weekly(weekly_data, value)
                    print("removed ", value, " from the list\n")
                    save_weekly(weekly_data)
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)


if __name__ == "__main__":
    print("Ran weekly script as main")
    weekly_setup()
