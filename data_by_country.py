import csv, os
import data_analysis

def data_by_country(country_name="France"):
    output_file_name = country_name+"_data.csv"
    if os.path.isfile('./'+output_file_name):
        return output_file_name
    country_data= []
    with open("data.csv", 'r') as csv_file:
        csv_lines = csv.reader(csv_file, delimiter=',')
        country_data.append(next(csv_lines))
        for line in csv_lines:
            if line[6]==country_name:
                country_data.append(line)
    with open(output_file_name, 'w') as csv_file:
        spamwriter = csv.writer(csv_file, delimiter=',')
        for data in country_data:
            spamwriter.writerow(data)
    print("Country data generated!")
    return output_file_name

def list_possible_country_names(csv_file='./data.csv'):
    possible_countries = []
    with open("data.csv", 'r') as csv_file:
        csv_lines = csv.reader(csv_file, delimiter=',')
        for line in csv_lines:
            if line[6] not in possible_countries:
                possible_countries.append(line[6])
    return possible_countries


