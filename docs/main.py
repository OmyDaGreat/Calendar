# main.py
from festivals import IndianFestivals

fest = IndianFestivals(2024)

# Write output to a file instead of printing
with open('output.txt', 'w') as f:
    f.write("Festivals in 2024:\n")
    f.write(fest.get_festivals_in_a_year())
    f.write("\n================================================")
'''
    f.write("\nFestivals in February 2024:\n")
    f.write(fest.get_festivals_in_a_month(2))
    f.write("\n================================================")
    f.write("\nReligious Festivals in 2024:\n")
    f.write(fest.get_religious_festivals_in_a_year())
    f.write("\n================================================")
    f.write("\nReligious Festivals in February 2024:\n")
    f.write(fest.get_religious_festivals_in_a_month(2))
'''