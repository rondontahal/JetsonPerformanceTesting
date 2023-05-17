from jtop import jtop
import csv
with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        # Read tegra stats
        print(jetson.stats)
        filename = 'JetsonStats.csv'
        with open(filename, 'w', newline="") as file:
            csvwriter = csv.writer(file) # create CSV
            csvwriter.writerow(header)
            


        