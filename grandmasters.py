import csv  


def count_gender(): 
    print('\033[91m' + '~Gender Ratio of Chess Grandmasters~\n     ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ' + '\033[0m')  # Print the message in red
    with open('chess_grandmaster_list.csv', 'r') as file:  # Open the CSV file
        reader = csv.reader(file)  # Create a CSV reader
        next(reader)  # Skip the header row
        male_count = 0  # Initialize the male count
        female_count = 0  # Initailize the female count
        for row in reader:  # Loop through each row in the CSV
            if row[7] == 'M':  # If the gender is male
                male_count += 1  # Increment the male count
            elif row[7] == 'F':  # If the gender is female
                female_count += 1  # Increment the female count
        total_count = male_count + female_count  # Calculate the total count
        male_percent = (male_count / total_count) * 100 if total_count else 0  # Calculate the male percentage, or 0 if there are no rows
        female_percent = (female_count / total_count) * 100 if total_count else 0  # Calculate the female percentage, or 0 if there are no rows
        print('\033[38;5;27m' + f"Number of Male Grandmasters ♂ : {male_count}")  # Print the male count in blue
        print('\033[95m' + f"Number of Female Grandmasters ♀ : {female_count}")  # Print the female count in pink
        print('\033[38;5;27m' + f"Percentage of Male Grandmasters ♂ : {male_percent}%")  # Print the male percentage in blue
        print('\033[95m' + f"Percentage of Female Grandmasters ♀ : {female_percent}%")  # Print the female percentage in pink
        print('\033[0m')  # Reset the color
        return male_count, female_count, male_percent, female_percent  # Return the counts and percentages

count_gender()







    
