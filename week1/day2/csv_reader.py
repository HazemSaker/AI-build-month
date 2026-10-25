import csv

def create_dummy_csv(file_path:str) -> None:
    """ creates a dummy csv file with 10 rows of random data."""
    with open(file_path,'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 25, "New York"])
        writer.writerow(["Bob", 30, "Los Angeles"])
        writer.writerow(["Charlie", 35, "Chicago"])
        writer.writerow(["David", 40, "Houston"])  
        writer.writerow(["Eve", 45, "Phoenix"])
        writer.writerow(["Frank", 50, "Philadelphia"])
        writer.writerow(["Grace", 55, "San Antonio"])
        writer.writerow(["Hannah", 60, "San Diego"])
        writer.writerow(["Ian", 65, "Dallas"])
        writer.writerow(["Jack", 70, "San Jose"]) 


def read_csv(file_path: str) -> list:
    """ reads a csv file and returns a list of dictionaries."""
    data = []
    with open(file_path, mode = 'r', encoding = 'utf-8') as f:
        reader = csv.DictReader(f)
        
        data = [row for row in reader]

    return data