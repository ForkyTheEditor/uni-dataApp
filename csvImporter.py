import csv
from district import District

class CSVImporter:
    """ Object used for importing CSV files and converting them to District type objects """

    def ImportCSVAsDistrict(filename):
        """ Imports an CSV file and returns it as a list of Districty type objects 
            In: filename : str
            Out: List of District objects """

        
        try:
            filename = str(filename)
        except ValueError:
            print("Filename is not of type string!")
            return []

        with open(filename, 'r') as f:

            readerObj = csv.reader(f)
            #Create the district list
            districtList = [District.OrderedListToDistrict(elem) for elem in readerObj]


        
        return districtList
            

