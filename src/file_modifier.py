import pickle

'''
weekly = [int,[strings]]
daily = [date,[strings]]
todo = [tasks] #not done, done
'''


def file_writer(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def file_reader(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

