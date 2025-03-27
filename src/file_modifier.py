import pickle


def file_writer(filename, data):
    try:
        print("saving...")
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

        print("saving succeded")
        return
    except:
        print("an error occured while saving")



def file_reader(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

