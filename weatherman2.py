__author__ = 'root'

import os
import sys

def read_files(path):
    '''reading all input data files from directory'''

    data = {}

    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            with open(dir_entry_path, 'r') as my_file:
                data[dir_entry] = my_file.read()

    return data

def formatting(data):
    '''Formatting the raw data into ordered key value pairs so that
    values can easily be read'''

    temp_dict_1  = {}
    monthly_data = {}
    keys_index = []
    
    #first loop for data formatting
    for entry_key, entry_value in data.items():

        year = entry_key.split("_")[2]
        month = entry_key.split("_")[3]
        month = month.split(".")[0]

        temp_dict_1 = entry_value.splitlines()
        monthly_data[year+month] = temp_dict_1[0:]

        temp_dict_1 = []       #emptying temporary list for next iteration

    #print(monthly_data)

    #removing file header and footer for each file
    for key, value in monthly_data.items():

        monthly_data[key] = value[1:-1]

    #print(monthly_data)

    #splitting measurements string for each day into seperate values
    for key, value in monthly_data.items():

        for k in range(len(value)):

            value[k] = value[k].split(",")

            if k == 0:

                for j in value[k]:
                    keys_index.append(j)

        monthly_data[key] = value[1:]

    #print(keys_index)
    return (monthly_data, keys_index)

def calculation(monthly_data, keys_index):
    '''Findin MIN and MAX values for Temp and Humidity from data for
    each year'''

    report1_yearly_values = {}
    report2_yearly_values = {}
    report1_final = ""
    report2_final = ""

    # To iterate over all months for each year separately
    for i in range(1996, 2012):

        # initializing using default values ('null' values cause problems in comparison)
        report1_yearly_values['Year'] = i
        report1_yearly_values['MaxTemp'] = 0
        report1_yearly_values['MinTemp'] = 100
        report1_yearly_values['MaxHumidity'] = 0
        report1_yearly_values['MinHumidity'] = 100

        report2_yearly_values["Year"] = i

        # iterating over months
        for key, value in monthly_data.items():

            if str(i) in key:
                # iterating over each day in a month
                for j in value:

                    if j[1] == '':
                        continue

                    # checks to find max and min values for temp and humidity
                    if int(j[1]) > report1_yearly_values['MaxTemp']:

                        report1_yearly_values['MaxTemp'] = int(j[keys_index.index('Max TemperatureC')])

                        report2_yearly_values['Temp'] = int(j[keys_index.index('Max TemperatureC')])
                        report2_yearly_values['Day'] = j[keys_index.index('PKT')]

                    if int(j[3]) < report1_yearly_values['MinTemp']:

                        report1_yearly_values['MinTemp'] = int(j[keys_index.index('Min TemperatureC')])

                    if int(j[7]) > report1_yearly_values['MaxHumidity']:

                        report1_yearly_values['MaxHumidity'] = int(j[keys_index.index('Max Humidity')])

                    if int(j[9]) < report1_yearly_values['MinHumidity']:

                        report1_yearly_values['MinHumidity'] = int(j[keys_index.index('Max Humidity')])
                        
        report1_final += str(report1_yearly_values['Year']) + " \t\t\t" + str(report1_yearly_values['MaxTemp']) + " \t\t\t\t" + str(report1_yearly_values['MinTemp']) + \
                        " \t\t\t\t" + str(report1_yearly_values['MaxHumidity']) + "  \t\t\t\t" + str(report1_yearly_values['MinHumidity']) + " \n"

        report2_final += str(report2_yearly_values['Year']) + " \t\t" + str(report2_yearly_values['Day']) + " \t\t" + str(report2_yearly_values['Temp']) + " \n"

    return report1_final, report2_final

def display(report1_result, report2_result, choice):
    '''Final formatting and printing of output'''

    output_report_1 = "Year \t\t MAX Temp \t\t MIN Temp \t\t MAX Humidity \t\t MIN Humidity \n"
    output_report_1 += "-------------------------------------------------------------------------------\n"

    output_report_2 = "Year \t\t Date \t\t Temp \n"
    output_report_2 += "------------------------------- \n"

    if choice == 1:

        output_report_1 += report1_result
        print(output_report_1)

    elif choice == 2:

        output_report_2 += report2_result
        print(output_report_2)

    else:

        print("Pass argument \n\t 1 to see Temperature and Humidity stats of "
              "each year \n\t 2 to see Hottest days of each year\n\nfollowed "
              "by the path of the data directory")

def main():
    '''Main function'''

    # reading command line arguments
    req_num = str(sys.argv[1])
    path = str(sys.argv[2])

    # path = os.getcwd() + '/weatherdata'
    # req_num = 2

    raw_data = {}
    monthly_data = {}
    report_results = ()
    keys_index = []

    raw_data = read_files(path)

    monthly_data, keys_index = formatting(raw_data)

    report_results = calculation(monthly_data, keys_index)

    display(report_results[0], report_results[1], int(req_num))

main()

