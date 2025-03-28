from file_modifier import file_reader, file_writer
import datetime


format = {
    "date": ["Info1", "Info2"],
}

daily_file = "../data/daily.pk"

daily_prompt = f"""
    A. Add a daily message for tomorrow
    B. Remove a daily message
    C. List the daily messages
    Enter to go back
    """


def load_daily():
    return file_reader(daily_file)


def save_daily(data):
    file_writer(daily_file, data)


def clean_daily(data):
    data = {}
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    for key in data:
        if key != str(today) or key != str(yesterday):
            data.pop(key)
    save_daily(data)


def add_to_daily(data, info):
    # date
    # data
    # info
    # check to see if the date is already in the list and append to it
    # if not add a new date to the list

    today = datetime.date.today()
    today = str(today)
    if today in data:
        data[today].append(info)
        print("appended to ", today)
    else:
        data[today] = [info]
        print("added new date ", today)

    save_daily(data)


def check_date(data):
    today = datetime.date.today()
    today = str(today)
    if today not in data:
        value = input("Add a new message for today")
        add_to_daily(data, value)
        clean_daily(data)
        save_daily(data)


def print_daily(data):
    for key in data:
        print("Date:", key)
        for item in data[key]:
            print("\t", item, end=",\n")


def remove_from_daily(data, index):
    data.pop(index)


def daily_path():
    daily_choice = " "
    daily_data = load_daily()

    check_date(daily_data)
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
                print(daily_data)
                change_date = input("today or yesterday\n")
                if change_date == "today":
                    change_date = str(datetime.date.today())
                elif change_date == "yesterday":
                    change_date = str(
                        datetime.date.today() - datetime.timedelta(days=1)
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
        if daily_choice == "C" or daily_choice == "c":
            print_daily(daily_data)


if __name__ == "__main__":
    print("Ran weekly script as main")
    data = []
    try:
        data = load_daily()
    except:
        print(f"Error: could not load data from {daily_file}")
        print("Creating a new file")
        data = format
        add_to_daily(data, "value")
        data.pop("date")
        save_daily(data)
    print(datetime.date.today())
    print(data)
