from file_modifier import file_reader, file_writer, create_weekly_category
from os import listdir
import shutil
import subprocess
import datetime

weekly_dir = "../data/weekly/"

weekly_prompt = f"""
    Enter a choice:

    A. Add an item to the weekly list 
    B. Remove an item from the weekly list
    C. Edit categories
    Enter to go back
    """

category_prompt = f"""
    Enter a choice:

    A. Add a category
    B. Remove a category
    C. Edit a categories name
    Enter to go back

    """


def get_weekly_categories():
    categories = []
    try:
        categories = listdir(weekly_dir)
    except:
        print(f"Error: could not load data from {weekly_dir}")
        return categories
    return categories


def get_weekly_files(weekly_category):
    weekly_file = weekly_category + "/weekly.pk"
    return listdir(weekly_dir)


def load_weekly(category):
    file = weekly_dir + category + "/weekly.pk"
    return file_reader(file)


def save_weekly(weekly_category, data):
    try:
        weekly_file = weekly_dir + weekly_category + "/weekly.pk"
    except:
        print(f"Error: could not write data to {weekly_category}")

        return
    file_writer(weekly_file, data)


def weekly_setup(weekly_category="weekly"):
    isocalendar = datetime.date.today().isocalendar()
    data = [0, isocalendar.week, ["Do more work"]]
    try:
        data = load_weekly(weekly_category)
    except:
        print(f"Error: could not load data from {weekly_category}")
        print("Creating a new list")
    print(data)
    clean_weekly_index(data)
    create_weekly_category(weekly_category)
    save_weekly(weekly_category, data)


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


def log(obj):
    with open("logs.txt", "a") as f:
        f.write(f"{obj}\n")


def display_weekly():
    data = []
    try:
        categories = get_weekly_files(weekly_dir)
        for c in categories:
            data.append(load_weekly(c))

    except:
        log(f"Error: could not load data from {weekly_dir}")
        return data

    log(f"data: {data}")
    subjects = []
    for d in data:
        weekly_index(d)
        subjects.append(d[2][d[0]])
        subjects.append("\n   ")
    return subjects


def print_weekly_categories():
    categories = get_weekly_categories()
    for c in categories:
        data = load_weekly(c)
        print(f"    {c}")
        for i in range(len(data[2])):
            print("\t", i + 1, ":", data[2][i], end="\n")


def print_weekly(category, data):
    print(f"{category}")
    for i in range(len(data[2])):
        print("\t", i + 1, ":", data[2][i], end="\n")


def clean_weekly_index(data):
    if data[0] >= len(data[2]):
        data[0] = len(data[2]) - 1


def add_to_weekly(data, info):
    data[2].append(info)
    clean_weekly_index(data)


def remove_from_weekly(data, index):
    data[2].pop(index - 1)
    clean_weekly_index(data)


def remove_weekly_category(category):
    try:
        shutil.rmtree(weekly_dir + category)
    except:
        print(f"Error: could not remove {category}")
        return
    print(f"Removed {category} from weekly categories")


def change_weekly_category(old, new):
    try:
        shutil.move(weekly_dir + old, weekly_dir + new)
    except:
        print(f"Error: could not move {old} to {new}")
        return
    print(f"Moved {old} to {new}")


def weekly_path():
    subprocess.run(["clear"])

    weekly_categories = get_weekly_files(weekly_dir)

    print(
        f"""
    Welcome to the your weekly focuses!
"""
    )
    weekly_choice = " "
    weekly_data = load_weekly(weekly_categories[0])

    clean_weekly_index(weekly_data)
    while weekly_choice != "":
        print_weekly_categories()
        value = ""
        weekly_choice = input(weekly_prompt)
        if weekly_choice == "A" or weekly_choice == "a":
            subprocess.run(["clear"])
            print_weekly_categories()
            category_choice = input("\n    Enter a category: ")
            weekly_data = load_weekly(category_choice)
            value = input("    Enter an item to add on the list\n")
            if len(value) <= 0:
                print("nothing added")
            else:
                add_to_weekly(weekly_data, value)
                print("added", value)
                save_weekly(category_choice, weekly_data)
            subprocess.run(["clear"])
        if weekly_choice == "B" or weekly_choice == "b":
            subprocess.run(["clear"])
            print_weekly_categories()
            try:
                category_choice = input("\n    Enter a category: ")
                weekly_data = load_weekly(category_choice)
                value = int(
                    input("    Enter the index of the item you want to remove\n")
                )
                if type(value) == type(0):
                    remove_from_weekly(weekly_data, value)
                    print("removed ", value, " from the list\n")
                    save_weekly(category_choice, weekly_data)
                subprocess.run(["clear"])
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)
        if weekly_choice == "C" or weekly_choice == "c":
            category_choice = " "
            while category_choice != "":
                print_weekly_categories()
                category_choice = input(category_prompt)
                if category_choice == "A" or category_choice == "a":
                    cat = input("\n    Enter a category name: ")
                    weekly_setup(cat)
                if category_choice == "B" or category_choice == "b":
                    cat = input("    Enter a category name: ")
                    remove_weekly_category(cat)
                if category_choice == "C" or category_choice == "c":
                    cat1 = input("    Enter the existing categories name: ")
                    cat2 = input("    Enter the new category name: ")
                    change_weekly_category(cat1, cat2)


if __name__ == "__main__":
    print("Ran weekly script as main")
    weekly_setup("weekly")
