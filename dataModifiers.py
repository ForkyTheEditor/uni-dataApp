from district import District
from copy import copy

class DataModifiers:
    """ Object containing functions for data modification and analysis """

    def average(list):
        """ Computes the average of a given list
            In: lis
            Out: float """

        return sum(list) / len(list)

    def mostPopulousDistrict(list):
        """ Returns the district with the most population from the given list
            In: List of District objects
            Out: District object """

        localList = list.copy()

        #Remove the districts with no population data
        filteredDistrictList = [elem for elem in localList if elem.population != None]
        
        #Find the most populous district
        mostPopulousDistrict = max(filteredDistrictList, key = lambda d: d.population)

        return mostPopulousDistrict


    def leastPopulousDistrict(list):
        """ Returns the district with the least population from the given list
            In: List of District objects
            Out: District object"""
        
        localList = list.copy()

        #Remove the districts with no population data
        filteredDistrictList = [elem for elem in localList if elem.population != None]

        #Find the least populous district
        leastPopulousDistrict = min(filteredDistrictList, key = lambda d: d.population )

        return leastPopulousDistrict


    def mostPeoplePerBedroom(list):
        """ Returns the district with the most population per bedroom from the given list
            In: List of District objects
            Out: District object"""

        localList = list.copy()

        #Remove the districts with no population or bedroom data
        filteredDistrictList = [elem for elem in localList if elem.population != None and elem.totalBedrooms != None]

        
        #Find the district with the most people per bedroom
        mostPeoplePerBedroomDistrict = max(filteredDistrictList, key = lambda d: d.population / d.totalBedrooms)

        return mostPeoplePerBedroomDistrict

    def leastPeoplePerBedroom(list):
        """ Returns the district with the least population per bedroom from the given list
            In: List of District objects
            Out: District object"""

        localList = list.copy()

        #Remove the districts with no population or bedroom data
        filteredDistrictList = [elem for elem in localList if elem.population != None and elem.totalBedrooms != None]

        
        #Find the district with the most people per bedroom
        leastPeoplePerBedroomDistrict = min(filteredDistrictList, key = lambda d: d.population / d.totalBedrooms)


        return leastPeoplePerBedroomDistrict

    def avgPeoplePerBedroom(list):
        """ Returns the average people per bedroom across all districts
            In: List of District objects
            Out: float """

        localList = list.copy()

        #Remove the districts with no population or bedroom data and form the list of population to bedroom ratios
        filteredListOfRatios = [elem.population/elem.totalBedrooms for elem in localList if elem.population != None and elem.totalBedrooms != None]

        #Return the total average of the list
        return DataModifiers.average(filteredListOfRatios)

    def avgAge(list):
        """ Returns the average median age across all districts
            In: List of District objects
            Out: float """
        
        localList = list.copy()

        #Remove the districts with no age data and form the age list
        filteredListOfAges = [elem.medianAge for elem in localList if elem.medianAge != None]

        #Return the average age
        return DataModifiers.average(filteredListOfAges)


    def avgIncome(list):
        """ Returns the average median income across all districts
            In: List of District objects
            Out: float """

        localList = list.copy()

        #Remove the districts with no income data and form the income list
        filteredListOfIncomes = [elem.medianIncome for elem in localList if elem.medianIncome != None]

        #Return the average income
        return DataModifiers.average(filteredListOfIncomes)

    def raisePrice(district):
        """ Raises the median house value if the district is near the ocean 
            In: District type object
            Out: District type object """
        
        localDistrict = copy(district)
       
        #Check for the appropriate proximities
        if localDistrict.proximity in ['NEAR OCEAN']:
            
            if localDistrict.medianHouseValue != None:
            
                localDistrict.medianHouseValue = localDistrict.medianHouseValue + (localDistrict.medianHouseValue * 0.1)

        return localDistrict

    

    def filterDistrictsByCriteria(list):
        """ Filters the list by longitude, latitude and medianHouseValue 
            In: List of districts
            Out: List of districts """

        localList = list.copy()
        
        while True:
            try:
                minLong = float(input("Longitude lower bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break
        while True:
            try:
                maxLong = float(input("Longitude upper bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break
        while True:
            try:
                minLat = float(input("Latitude lower bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break
        while True:
            try:
                maxLat = float(input("Latitude upper bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break
        while True:
            try:
                minValue = float(input("Median House Value lower bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break
        while True:
            try:
                maxValue = float(input("Median House Value upper bound: "))
            except ValueError:
                print("Input is not float!")
            else:
                break

        #First, remove the None types in the list
        filteredList = [elem for elem in localList if elem.longitude != None and elem.latitude != None and elem.medianHouseValue != None]

        #Then, progressively filter the list by one criteria at a time
        filteredList = [elem for elem in filteredList if elem.longitude <= maxLong and minLong <= elem.longitude ]
        filteredList = [elem for elem in filteredList if elem.latitude <= maxLat and minLat <= elem.latitude ]
        filteredList = [elem for elem in filteredList if elem.medianHouseValue <= maxValue and minValue <= elem.medianHouseValue]

        if len(filteredList) == 0:
            
            print("No district meets the criteria!")

        return filteredList

    def sortByMedianHouseValue(list, descending):
        """ Sorts the district list by the median house value 
            Descending = True for descending order, False otherwise
            In: List of districts
            Out: List of districts """

        localList = list.copy()

        localList = [elem for elem in localList if elem.medianHouseValue != None]

        sortedList = sorted(localList, key = lambda x: x.medianHouseValue, reverse = descending)

        return sortedList

    def sortByOceanProximity(list, descending):
        """ Sorts the district list by the ocean proximity
            Descending = True for descending order, False otherwise
            In: List of districts
            Out: List of districts """

        localList = list.copy()

        localList = [elem for elem in localList if elem.proximity not in [None, '', 'ocean_proximity'] ]

        sortedList = sorted(localList, key = lambda x: x.proximity, reverse = descending)

        return sortedList

    def continentalShift(list):
        """ Increases all the longitudes by 5 
            In: List of districts
            Out: Nothing"""

        

        for elem in list:

            if elem.longitude not in [None, '', 'longitude']:

                elem.longitude += 5
        
           

    def userFilterList(column):
        """ Filters the list by the user given column
            In: int
            Out: List of districts """

        if column == 0:
            #Longitude
            pass
        elif column == 1:
            #Latitude
            pass
        elif column == 2:
            #Median Age
            pass
        elif column == 3:
            #Total Rooms
            pass
        elif column == 4:
            #Total Bedrooms
            pass
        elif column == 5:
            #Population
            pass
        elif column == 6:
            #Households
            pass
        elif column == 7:
            #Median Income
            pass
        elif column == 8:
            #Median House Value
            pass
        elif column == 9:
            #Proximity
            pass
        else:
            return []


