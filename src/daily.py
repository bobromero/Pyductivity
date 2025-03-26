from file_modifier import file_reader, file_writer 
import datetime


format = [[1, datetime.date.today(),["value1","value2"]]]

daily_file = "../data/daily.pk"

daily_prompt = f'''
    A. Add a daily message for tomorrow
    B. Remove a daily message
    C. List the daily messages
    Enter to go back
    '''

def load_daily():
    return file_reader(daily_file)

def save_daily(data):
    file_writer(daily_file, data)   

def add_to_daily(data, info):
    today = datetime.date.today()
    if data[1][0] != today:
        data[0] = data[1]
        data[1] = [datetime.date.today(), info]
    else:
        data[1][1].extend(info)

def remove_from_daily(data,index):
    data.pop(index)

def daily_path():
    value = " "
    daily_choice = " "
    daily_data = load_daily()
    # if daily_data[1][0] != datetime.date.today():
    #     add_to_daily(daily_data, [])

    while daily_choice != "":
 
        print("hello")
        if daily_choice == "A" or daily_choice == "a":
            while value != "":
                value = input("Enter what you want to do tomorrow\nPress enter to finish\n")
                if len(value) <= 0:
                    print("nothing added")
                else:
                    add_to_daily(daily_data, value)
                    print("added", value)
        if daily_choice == "B" or daily_choice == "b":
            print(*daily_data)
            try:
                value = int(input("Enter the index of the item you want to remove\n"))
                if type(value) == type(0):
                    remove_from_daily(daily_data,value)
                    print("removed ",value, " from the list\n")
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)
            if daily_choice == "C" or daily_choice == "c":
                print(*daily_data)
            if daily_choice == "D" or daily_choice == "d":
                save_daily(daily_data)


if __name__ == "__main__":
    print("Ran weekly script as main")
    data = [] 
    try:
        data = load_daily()
    except:
        print(f"Error: could not load data from {daily_file}")
        print("Creating a new file")
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        data.append([yesterday, ["value"]])
        data.append([datetime.date.today(), ["value"]])
        save_daily(data)
    print(datetime.date.today())
    print(data)


