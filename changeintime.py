import csv  

def calculate_change():
    with open('chess_grandmaster_list.csv', 'r') as file:  
        reader = csv.reader(file)  #
        next(reader)  

        # Initialize counters for male and female Grandmasters before and after 2000
        male_count_before_2000 = female_count_before_2000 = 0
        male_count_2000_and_after = female_count_2000_and_after = 0

        for row in reader:  # Loop through each row in the CSV
            year = int(row[4])  # Get the year from the row
            if year < 2000:  # If the year is before 2000
                if row[7] == 'M':  # If the Grandmaster is male
                    male_count_before_2000 += 1
                elif row[7] == 'F':  # If the Grandmaster is female
                    female_count_before_2000 += 1
            else:  # If the year is 2000 or after
                if row[7] == 'M':  # If the Grandmaster is male
                    male_count_2000_and_after += 1
                elif row[7] == 'F':  # If the Grandmaster is female
                    female_count_2000_and_after += 1

        # Calculate the total number of Grandmasters before and after 2000
        total_before_2000 = male_count_before_2000 + female_count_before_2000
        total_2000_and_after = male_count_2000_and_after + female_count_2000_and_after

        # Calculate the percentage of male and female Grandmasters before and after 2000
        male_percent_before_2000 = (male_count_before_2000 / total_before_2000) * 100 if total_before_2000 else 0
        female_percent_before_2000 = (female_count_before_2000 / total_before_2000) * 100 if total_before_2000 else 0

        # Calculate the rate of change in the percentage of Grandmasters
        male_percent_2000_and_after = (male_count_2000_and_after / total_2000_and_after) * 100 if total_2000_and_after else 0
        female_percent_2000_and_after = (female_count_2000_and_after / total_2000_and_after) * 100 if total_2000_and_after else 0

        male_rate_of_change = male_percent_2000_and_after - male_percent_before_2000
        female_rate_of_change = female_percent_2000_and_after - female_percent_before_2000

        print(f"Before year 2000: Male GMs: {male_count_before_2000}   Female GMs: {female_count_before_2000}       Male %: {male_percent_before_2000}%     Female %: {female_percent_before_2000}%")
        print(f"Year 2000 and beyond: Male GMs: {male_count_2000_and_after}   Female GMs: {female_count_2000_and_after}      Male %: {male_percent_2000_and_after}%     Female %: {female_percent_2000_and_after}%")
        print('\033[38;5;27m' + f"Rate of change for male Grandmasters: {male_rate_of_change}")
        print('\033[95m' + f"Rate of change for female Grandmasters: {female_rate_of_change}")

calculate_change()