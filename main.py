# Dalton  House - Student ID 009453254 - WGU C950

import csv
import hash_table
import package
import truck
import nearest_neighbor

# Create Hash Table instance to hold packages in main
package_table = hash_table.HashTable()

# Import csv containing package data
with open('package_file.csv') as package_file:
    package_reader = csv.reader(package_file, delimiter=',')
    next(package_reader)

    # Each row in csv represents a new package - iterate over each row to gain attributes
    for row in package_reader:
        package_id = int(row[0])
        package_address = row[1]
        package_city = row[2]
        package_zipcode = row[3]
        package_weight = row[4]
        package_deadline = row[5]

        # Store each package in a package object - each attribute is assigned to one of the rows
        pack = package.Package(package_id, package_address, package_city, package_zipcode, package_weight, package_deadline)
        package_table.insert(package_id, pack)

# Initialize empty list to hold distance matrix
distance_matrix = []

# Initialize empty dictionary to map locations to indexes for fast indexing
address_lookup = []

with open('distance_table.csv', newline = '') as distance_table:
    distance_reader = csv.reader(distance_table, delimiter = ',')
    address_lookup = next(distance_reader)
    for row in distance_reader:
        distance_matrix.append(row)
