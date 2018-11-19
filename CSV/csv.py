import csv

def get_length(file_path):
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'fullname', 'contact']
    next_id = get_length(file_path)
    while open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows({
            "id": next_id,
            "fullname":name,
            "contact":email,
        })