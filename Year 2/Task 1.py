import os
import csv


# Simple hash function that uses Python's built-in hash and handles negative values
def simple_hash(key, table_size):
    return hash(key) % table_size


# Hash table implementation using separate chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = simple_hash(key, self.size)
        # Check if the key exists and update the value if it does
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i] = [key, value]
                return
        # If the key does not exist, append a new list
        self.table[index].append([key, value])

    def search(self, key):
        index = simple_hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None


# Function to normalize a postcode
def normalize_postcode(postcode):
    # Placeholder normalize_postcode function
    # Replace this with your actual normalization logic if you have one
    postcode = postcode.upper().replace(' ', '')
    if len(postcode) >= 6:
        return postcode[:len(postcode) - 3] + ' ' + postcode[len(postcode) - 3:]
    else:
        return None


# Function to create a hash table from a CSV file
def create_store_table(csv_file_path, hash_table):
    try:
        # Opens the file and reads it line by line and creates a key
        with open(csv_file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['retailer'], row['postcode'])
                value = {
                    'store_name': row['store_name'],
                    'address': row['add_one'],
                    'town': row['town'],
                    'postcode': row['postcode'],
                    'size_band': row['size_band']
                }
                hash_table.insert(key, value)
    # If it can't find a file gives an error message and ends the program
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
        exit()
    # If it gets a csv error then it gives a relevant error message and ends the program
    except csv.Error as error:
        print(f"CSV error: {error}")
        exit()


# Function to print store details
def print_store_details(store_details):
    # Prints the store details unless it can't find them in the hash table
    if store_details:
        print("--------------------------------------------------")
        print(f"Retailer Name: {store_details['store_name']}")

        print(f"Address: {store_details['address']}")
        print(f"Town: {store_details['town']}")
        print(f"Postcode: {store_details['postcode']}")
        print(f"Size Band: {store_details['size_band']}")
        print("--------------------------------------------------")
    else:
        print("Retailer with the provided name and postcode not found.")


# Main function
def main():
    # Set the path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'geolytix_retailpoints_v25_202209.csv')

    # Set the size of the hash table
    hash_table_size = 10000
    hash_table = HashTable(hash_table_size)

    # Populate the hash table with data from the CSV file
    create_store_table(csv_file_path, hash_table)

    # Main loop for user input
    while True:
        retailer = input("Enter the store name (capital first letter) or 'exit' to quit: ")
        if retailer.lower() == 'exit':
            break
        postcode = input("Enter a postcode: ")

        # Normalize the postcode
        normalized_postcode = normalize_postcode(postcode)

        if normalized_postcode:
            # Creates a search key using the retailer name and the postcode
            search_key = (retailer, normalized_postcode)
            store_details = hash_table.search(search_key)
            print_store_details(store_details)
        else:
            print("Invalid postcode, please enter a new one in the format 'XX1 1XX'.")


# Run the main function
main()
