import csv

def process_amount(amount_str):
    # Remove the minus sign from the amount string
    inflow = False
    amount_str = amount_str.replace(',', '.')
    
    if "-" in amount_str:
        amount_str = amount_str.lstrip('-')
    else:
        inflow = True
    # Convert the string to a float
    try:
        amount = float(amount_str)
        
        if inflow == True:
            
            amount = amount * -1
    
    except ValueError:
        # Return None if the conversion fails
        return None
    
    return amount

def process_csv(csv_filename):
    # Initialize variables
    category_totals = {}

    # Open the CSV file with UTF-8 encoding and semicolon as the delimiter
    with open(csv_filename, 'r', encoding='utf-8') as file:
        # Create a CSV reader object with semicolon as the delimiter
        csv_reader = csv.reader(file, delimiter=';')

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Extract the value from the 7th column (assuming 0-based indexing)
            
            amount_str = row[7]
            amount = process_amount(amount_str)
            
            if amount is None:
                # Skip rows with missing or invalid amounts
                continue

            # Extract category name (assuming it's the last element)
            category_name = row[-1]
            provider = row[2]
            if "DYNAMIC" in provider:
                category_name = "Office bar"
            
            if "FITNESS" in provider:
                category_name = "Gym"
            
            if "SPOTIFY" in provider:
                category_name = "Spotify"
            
            if "KATARZYNA" in provider:
                category_name = "Netflix"
            
            # Add amount to category total
            if category_name not in category_totals:
                category_totals[category_name] = 0.0
                
            category_totals[category_name] += amount

    
    return category_totals

# Example usage:
csv_filename = 'Lista_operacji_20240421_211135.csv'
category_totals = process_csv(csv_filename)
print("Category totals:")
amount_total = 0.00

for category, total in category_totals.items():
    
    #print(f"{category}: {total}")
   
    if total < 0:
        continue
    
    amount_total = amount_total + total
    
print(amount_total)
print("let's examine what % you wasted:")

for category, total in category_totals.items():
    
    if total < 0:
        continue
    print(f"{category}: {round(total)} #Percentage: {round((total/amount_total)*100)} %")
    print()
    
    
    