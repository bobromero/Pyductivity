from file_modifier import file_reader, file_writer
import subprocess
import datetime


format = {
    "date": ["Info1", "Info2"],
}

daily_file = "../data/daily.pk"

daily_prompt = f"""
    Welcome to the your daily messages!

    A. Add a daily message for tomorrow
    B. Remove a daily message
    Enter to go back
    """


def load_daily():
    return file_reader(daily_file)


def save_daily(data):
    file_writer(daily_file, data)


def daily_setup():
    data = []
    try:
        data = load_daily()
    except:
        print(f"Error: could not load data from {daily_file}")
        print("Creating a new file")
        data = format
        add_to_daily(data, "Do more work")
        data.pop("date")
        save_daily(data)
    print(datetime.date.today())
    print(data)


def clean_daily(data):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    today = datetime.date.today()
    save = False
    to_remove = []
    for key in data:
        if key != str(today) and key != str(tomorrow):
            to_remove.append(key)
            save = True
    for x in to_remove:
        data.pop(x)
    if save:
        save_daily(data)


def add_to_daily(data, info):
    # date
    # data
    # info
    # check to see if the date is already in the list and append to it
    # if not add a new date to the list

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = str(tomorrow)
    if tomorrow in data:
        data[tomorrow].append(info)
        print("appended to ", tomorrow)
    else:
        data[tomorrow] = [info]
        print("added new date ", tomorrow)

    save_daily(data)


def check_date(data):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = str(tomorrow)
    if tomorrow not in data:
        value = input("Add a new message for tomorrow\n")
        add_to_daily(data, value)


def print_daily(data):
    subprocess.run(["clear"])
    for key in data:
        print("Date:", key)
        for i in range(len(data[key])):
            print(i, "\t", data[key][i], end=",\n")


def remove_from_daily(data, index):
    data.pop(index)


def daily_path():
    subprocess.run(["clear"])
    daily_choice = " "
    daily_data = load_daily()

    check_date(daily_data)
    clean_daily(daily_data)
    print_daily(daily_data)

    while daily_choice != "":
        daily_choice = input(daily_prompt)
        if daily_choice == "A" or daily_choice == "a":
            value = " "
            while value != "":
                value = input("Enter what you want to do tomorrow:\n")
                if len(value) <= 0:
                    print("nothing added")
                else:
                    add_to_daily(daily_data, value)
                    print("added", value)

        if daily_choice == "B" or daily_choice == "b":
            print_daily(daily_data)
            try:
                change_date = input("today or tomorrow\n")
                if change_date == "today":
                    if str(datetime.date.today()) in daily_data:
                        change_date = str(datetime.date.today())
                    else:
                        print("no data for today")
                        continue
                elif change_date == "tomorrow":
                    change_date = str(
                        datetime.date.today() + datetime.timedelta(days=1)
                    )
                else:
                    print("invalid date")
                    continue
                value = int(input("Enter the index of the value you want to remove\n"))
                daily_data[change_date].pop(value)
                print("removed ", value, " from the list\n")
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)


if __name__ == "__main__":
    print("Ran weekly script as main")
    daily_setup()
