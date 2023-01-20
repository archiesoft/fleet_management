# total_ss= total suitablility score
#this file calculates total SS and based on that assign shipment to drivers on basis of street names

import json

def calculate_base_suitability_score(street_name, driver_name):
    ss_score = 0
    # condition 1 when shipment street name length is even
    if len(street_name) % 2 == 0:
        ss_score = vowels_count(driver_name)*1.5
    # condition 2 when shipment street name length is odd
    else:
        ss_score = consonants_count(driver_name)*1
    # find common factors
    common_substring = find_common_string(driver_name, street_name)
    if common_substring:
        #increase the base score by 50%
        ss_score += ss_score*0.5
    return ss_score

def find_common_string(string1, string2):
    # Initialize variables to store the length of common patterns
    common_substrings = []

    # Find the length of common substrings
    for i in range(len(string1)):
        for j in range(i+1, len(string1)+1):
            if string1[i:j] in string2:
                if(len(string1[i:j]) > 1):
                    common_substrings.append(len(string1[i:j]))
    return common_substrings

def consonants_count(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count

def vowels_count(string):
    vowels = 'aeiouAEIOU'
    # or return sum(1 for char in string if char in vowels)
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def assign_shipment():
    assignments = {}
    # getting peron name list from file person_names
    with open("person_names.json", "r") as names_file:
        person_data = json.load(names_file)
        driver_names = person_data["person_names"]

    # getting street name list from file shipment_destinations    
    with open("shipment_destinations.json", "r") as street_file:
        street_data = json.load(street_file)
        streets = street_data["shipment_destinations"] 

        for driver_name in driver_names:
            best_driver = None
            # total_ss is the total calculated Suitability score
            total_ss = 0
            for street_name in streets:
                score_count = calculate_base_suitability_score(street_name, driver_name)
                if score_count > total_ss:
                    best_driver = driver_name
                    total_ss = score_count
                if best_driver not in assignments.values() and street_name not in assignments.keys():
                    assignments[street_name] = best_driver
                    
    # print all the shipments(street name) with best driver assigned
    for street, best_driver in assignments.items():
        print(f' shipment destination- {street}  has been assigned to: {best_driver}')
    print(f'Total suitability score SS: {total_ss}')



#run the main function
assign_shipment()



        