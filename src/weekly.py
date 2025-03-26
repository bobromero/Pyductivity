from file_modifier import file_reader, file_writer 

weekly_file = "../data/weekly.pk"

weekly_prompt = f'''
    A. Add an item to the weekly list 
    B. Remove an item from the weekly list
    C. List the items in the weekly list
    D. Save
    Enter to go back
    '''



def load_weekly():
    return file_reader(weekly_file)

def save_weekly(data):
    file_writer(weekly_file, data)

def display_weekly(index):
    data = []
    try:
        data = load_weekly()[index]
    except:
        print(f"couldn't load weekly at {index}")

    string = data[1]
    if len(data) < 1:
        return ""
    if len(data) <= index:
        return string 
    return string 

def add_to_weekly(data, info):
    data.append([len(data), info])
    
def remove_from_weekly(data,index):
    data.pop(index)

def weekly_path():
    value = ""
    weekly_choice = " "
    weekly_data = load_weekly()
    while weekly_choice != "":
        weekly_choice = input(weekly_prompt)
        if weekly_choice == "A" or weekly_choice == "a":
            value = input("Enter an item to add on the list\n")
            if len(value) <= 0:
                print("nothing added")
            else:
                add_to_weekly(weekly_data, value)
                print("added", value)
        if weekly_choice == "B" or weekly_choice == "b":
            print(*weekly_data)
            try:
                value = int(input("Enter the index of the item you want to remove\n"))
                if type(value) == type(0):
                    remove_from_weekly(weekly_data,value)
                    print("removed ",value, " from the list\n")
            except TypeError:
                print("couldn't process index, not deleting")
            except:
                print("Error, could not delete at, ", value)

        if weekly_choice == "C" or weekly_choice == "c":
            print(*weekly_data)

        if weekly_choice == "D" or weekly_choice == "d":
            try:
                print("saving...")
                save_weekly(weekly_data)
                print("saving succeded")
                return
            except:
                print("an error occured while saving")



if __name__ == '__main__':
    print("Ran weekly script as main")
    data = [[0,"value"]]   
    try:
        data = load_weekly()
    except:
        print(f"Error: could not load data from {weekly_file}")
        print("Creating a new list")
    print(data)
    # info = input("enter a weekly reminder\n")
    # data.append([len(data),info])
    # print(data)
    # save_weekly(data)
    

    
