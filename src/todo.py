from file_modifier import file_reader, file_writer, create_todo_category
from os import listdir
import shutil
import subprocess
import datetime

todo_dir = "../data/todo/"

todo_prompt = f"""
    Enter a choice:

    A. Add an item to the todo list 
    B. Remove an item from the todo list
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


def get_todo_categories():
    categories = []
    try:
        categories = listdir(todo_dir)
    except:
        print(f"Error: could not load data from {todo_dir}")
        return categories
    return categories


def get_todo_files(todo_category):
    todo_file = todo_category + "/todo.pk"
    return listdir(todo_dir)


def load_todo(category):
    file = todo_dir + category + "/todo.pk"
    return file_reader(file)


def save_todo(todo_category, data):
    try:
        todo_file = todo_dir + todo_category + "/todo.pk"
    except:
        print(f"Error: could not write data to {todo_category}")

        return
    file_writer(todo_file, data)


def todo_setup(todo_category="todo"):
    isocalendar = datetime.date.today().isocalendar()
    data = [0, isocalendar.week, ["Do more work"]]
    try:
        data = load_todo(todo_category)
    except:
        print(f"Error: could not load data from {todo_category}")
        print("Creating a new list")
    print(data)
    clean_todo_index(data)
    create_todo_category(todo_category)
    save_todo(todo_category, data)


def todo_index(data):
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


def display_todo():
    data = []
    try:
        categories = get_todo_files(todo_dir)
        for c in categories:
            data.append(load_todo(c))

    except:
        log(f"Error: could not load data from {todo_dir}")
        return data

    log(f"data: {data}")
    subjects = []
    for d in data:
        todo_index(d)
        subjects.append(d[2][d[0]])
        subjects.append("\n   ")
    return subjects


def print_todo_categories():
    categories = get_todo_categories()
    for c in categories:
        data = load_todo(c)
        print(f"    {c}")
        for i in range(len(data[2])):
            print("\t", i + 1, ":", data[2][i], end="\n")


def print_todo(category, data):
    print(f"{category}")
    for i in range(len(data[2])):
        print("\t", i + 1, ":", data[2][i], end="\n")


def clean_todo_index(data):
    if data[0] >= len(data[2]):
        data[0] = len(data[2]) - 1


def add_to_todo(data, info):
    data[2].append(info)
    clean_todo_index(data)


def remove_from_todo(data, index):
    data[2].pop(index - 1)
    clean_todo_index(data)


def remove_todo_category(category):
    try:
        shutil.rmtree(todo_dir + category)
    except:
        print(f"Error: could not remove {category}")
        return
    print(f"Removed {category} from todo categories")


def change_todo_category(old, new):
    try:
        shutil.move(todo_dir + old, todo_dir + new)
    except:
        print(f"Error: could not move {old} to {new}")
        return
    print(f"Moved {old} to {new}")


def todo_path():
    subprocess.run(["clear"])

    todo_categories = get_todo_files(todo_dir)

    print(
        f"""
    Welcome to the your todo focuses!

    {' '.join(map(str, todo_categories))}
        """
    )

    todo_choice = " "
    todo_data = load_todo(todo_categories[0])

    clean_todo_index(todo_data)
    while todo_choice != "":
        subprocess.run(["clear"])
        print_todo_categories()
        value = ""
        todo_choice = input(todo_prompt)
        if todo_choice == "A" or todo_choice == "a":
            subprocess.run(["clear"])
            print_todo_categories()
            category_choice = input("    Enter a category: ")
            todo_data = load_todo(category_choice)
            value = input("    Enter an item to add on the list\n")
            if len(value) <= 0:
                print("nothing added")
            else:
                add_to_todo(todo_data, value)
                print("added", value)
                save_todo(category_choice, todo_data)
            subprocess.run(["clear"])
        if todo_choice == "B" or todo_choice == "b":
            subprocess.run(["clear"])
            print_todo_categories()
            try:
                category_choice = input("    Enter a category: ")
                todo_data = load_todo(category_choice)
                value = int(
                    input("    Enter the index of the item you want to remove\n")
                )
                if type(value) == type(0):
                    remove_from_todo(todo_data, value)
                    print("removed ", value, " from the list\n")
                    save_todo(category_choice, todo_data)
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)
            subprocess.run(["clear"])
        if todo_choice == "C" or todo_choice == "c":
            category_choice = " "
            while category_choice != "":
                subprocess.run(["clear"])
                print_todo_categories()
                category_choice = input(category_prompt)
                if category_choice == "A" or category_choice == "a":
                    cat = input("    Enter a category name: ")
                    todo_setup(cat)
                if category_choice == "B" or category_choice == "b":
                    cat = input("    Enter a category name: ")
                    remove_todo_category(cat)
                if category_choice == "C" or category_choice == "c":
                    cat1 = input("    Enter the existing categories name: ")
                    cat2 = input("    Enter the new category name: ")
                    change_todo_category(cat1, cat2)
                subprocess.run(["clear"])


if __name__ == "__main__":
    print("Ran todo script as main")
    todo_setup("todo")
