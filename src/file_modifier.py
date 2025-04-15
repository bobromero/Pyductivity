import pickle
import os


def file_writer(filename, data):
    try:
        print("saving...")
        with open(filename, "wb") as file:
            pickle.dump(data, file)

        print("saving succeded")
        return
    except:
        print("an error occured while saving")


def file_reader(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


def create_weekly_category(weekly_category):
    weekly_path = "../data/weekly"
    weekly_file = "weekly.pk"
    try:
        os.mkdir(weekly_path + "/" + weekly_category)
        weekly_file = f"{weekly_path}/{weekly_category}/weekly.pk"
        with open(weekly_file, "wb") as file:
            pickle.dump([], file)
        return weekly_file
    except:
        print(f"Error: could not create {weekly_category}")
    return weekly_category


def create_todo_category(todo_category):
    todo_path = "../data/todo"
    todo_file = "todo.pk"
    try:
        os.mkdir(todo_path + "/" + todo_category)
        todo_file = f"{todo_path}/{todo_category}/todo.pk"
        with open(todo_file, "wb") as file:
            pickle.dump([], file)
        return todo_file
    except:
        print(f"Error: could not create {todo_category}")
    return todo_category
