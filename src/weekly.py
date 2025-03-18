from file_modifier import file_reader, file_writer 

weekly_file = "../data/weekly.pk"
# data_type = 


def load_weekly():
    return file_reader(weekly_file)

def save_weekly(data):
    file_writer(weekly_file, data)


if __name__ == '__main__':
    print("Ran weekly script as main")
    data = [[0,"value"]]   
    try:
        data = load_weekly()
    except:
        print(f"Error: could not load data from {weekly_file}")
        print("Creating a new list")
    info = input("enter a weekly reminder\n")
    data.append([len(data),info])
    print(data)

    save_weekly(data)

    
