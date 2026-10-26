import requests
import json
import csv
import os 


def fetch(url, params = None):
    try:
        response = requests.get(url, params = params, timeout = 5)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"en error had occured : {e}")
        return None


def save_data(data, fields_to_keep, csv_path, json_path):
    if not data:
        print("No Data...!")
        return 
    
    os.makedirs(os.path.dirname(csv_path), exist_ok = True)
    os.makedirs(os.path.dirname(json_path), exist_ok = True)

    records = data if isinstance(data, list) else [data]

    filtered_records = []
    for record in records:
        filtered = {field: record.get(field) for field in fields_to_keep}
        filtered_records.append(filtered)

    if filtered_records:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_records, f, indent = 4)
        print("file saved as json successfully")

        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames = fields_to_keep)
            writer.writeheader()
            writer.writerows(filtered_records)

        print("file saved as csv successfuly")



if __name__ == "__main__":
    test_url = "https://jsonplaceholder.typicode.com/posts"
    fields = ["id", "title", "body"]

    print("--- Running successful fetch test ---")
    data = fetch(test_url, params={"_limit": 3})
    save_data(data, fields, "data/output.json", "data/output.csv")
    
    print("\n--- Running intentional failure test (Step 6) ---")
    bad_url = "https://jsonplaceholder.typicode.com/invalid-endpoint-xyz"
    failed_data = fetch(bad_url)
    save_data(failed_data, fields, "data/output.json", "data/output.csv")
