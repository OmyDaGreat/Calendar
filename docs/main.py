from festivals import IndianFestivals
import json

fest = IndianFestivals(2024)

# Parse the JSON string into a Python dictionary
festivals_dict = json.loads(fest.get_festivals_in_a_year())

# Open the output file
with open('docs/output.txt', 'w') as f:
    f.write("Festivals in 2024:\n")
    
    # Iterate over each month
    for month, festivals in festivals_dict.items():
        if month != "S.No.": # Skip the "S.No." entry
            f.write(f"\n{month}:\n")
            # Iterate over each festival in the month
            for festival in festivals:
                f.write(f"- {festival['name']} on {festival['day']}, {month} {festival['date']}\n")
