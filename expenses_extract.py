import csv

def process_amount(amount_str):
    """Process the amount string and convert it to a float."""
    inflow = False
    amount_str = amount_str.replace(',', '.')
    
    if "-" in amount_str:
        amount_str = amount_str.lstrip('-')
    else:
        inflow = True
    
    try:
        amount = float(amount_str)
        if inflow:
            amount = amount * -1
    except ValueError:
        return None
    
    return amount

def process_csv(csv_filename):
    """Process the CSV file and return category totals."""
    category_totals = {}
    
    with open(csv_filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            amount_str = row[7]
            amount = process_amount(amount_str)
            
            if amount is None:
                continue

            category_name = row[-1]
            provider = row[2]
            if "DYNAMIC" in provider:
                category_name = "Office bar"
            elif "FITNESS" in provider:
                category_name = "Gym"
            elif "SPOTIFY" in provider:
                category_name = "Spotify"
            elif "KATARZYNA" in provider:
                category_name = "Netflix"

            if category_name not in category_totals:
                category_totals[category_name] = 0.0
                
            category_totals[category_name] += amount

    return category_totals
