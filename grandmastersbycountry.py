import csv  
import re

def country_with_grandmasters():  # Define a function to count the genders
    with open('chess_grandmaster_list.csv', 'r', encoding='utf-8') as file:  # Open the CSV file with 'utf-8' encoding
        reader = csv.reader(file)  # Create a CSV reader
        next(reader)  # Skip the header row
        maleDictCountry = dict()  #Initialize the male country dictionary
        femaleDictCountry = dict()  # Initailize the female country dictionary
        for row in reader:  # Loop through each row in the CSV
            country = re.sub(r'[^\x00-\x7F]+', '', row[5])  # Remove non-ASCII characters from the country name
            if row[7] == 'M':  # If the gender is male
                maleDictCountry[country] = maleDictCountry.get(country, 0) + 1  # Increment the male count for the country
            elif row[7] == 'F':  # If the gender is female
                femaleDictCountry[country] = femaleDictCountry.get(country, 0) + 1  # Increment the female count for the country

        print('\033[38;5;27m' + f"Male Grandmasters per country: ", maleDictCountry)  # Print the male count per country
        print('\033[95m' + f"Female Grandmasters per country: ", femaleDictCountry, "\n")  # Print the female count per country

        # Find and print the country with the most male grandmasters
        max_male_country = max(maleDictCountry, key=maleDictCountry.get)
        print('\033[38;5;27m' + f"Country that produces the dominating gender Grandmasters: {max_male_country} with {maleDictCountry[max_male_country]} male grandmasters\n")

         # find and print the country with the most female grandmasters
        max_female_country = max(femaleDictCountry, key=femaleDictCountry.get)
        print('\033[95m' + f"Country that produces the most nondominating gender Grandmasters: {max_female_country} with {femaleDictCountry[max_female_country]} female grandmasters\n")

        # Combine the male and female dictionaries into a total dictionary
        totalDictCountry = {k: maleDictCountry.get(k, 0) + femaleDictCountry.get(k, 0) for k in set(maleDictCountry) | set(femaleDictCountry)}

      # Find and print the country with the most grandmasters
        max_country = max(totalDictCountry, key=totalDictCountry.get)
        print('\033[91m' + f"Country that produces the most Grandmasters: {max_country} with {totalDictCountry[max_country]} grandmasters\n")

country_with_grandmasters()  # Call the function
