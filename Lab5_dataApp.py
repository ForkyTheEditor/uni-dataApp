from csvImporter import CSVImporter
from district import District
from dataModifiers import DataModifiers
from testModule import TestUnits

class MainClass:
    """ The main class of the application """

    def main():
        """ The main function of the application """

        #The main district list of the application
        districtList = []

        #Import the CSV file to the main district list
        districtList = CSVImporter.ImportCSVAsDistrict('housing.csv')

        #Update the ocean proximity dictionary
        [District.UpdateProximities(elem.proximity) for elem in districtList if elem.proximity != None]         
        

        #Return the most populous district
        print("Most populous district: ", DataModifiers.mostPopulousDistrict(districtList))

        #Return the least populous district
        print("Least populous district: ", DataModifiers.leastPopulousDistrict(districtList))

        #Return the district with the most people per bedroom
        largestRatioDistrict = DataModifiers.mostPeoplePerBedroom(districtList)
        print("District with the most people per bedroom: ", largestRatioDistrict)
        print("Most people per bedroom: ", largestRatioDistrict.population / largestRatioDistrict.totalBedrooms)

        #Return the district with the least people per bedroom
        smallestRatioDistrict = DataModifiers.leastPeoplePerBedroom(districtList)
        print("District with the least people per bedroom: ", smallestRatioDistrict)
        print("Least people per bedroom: ", smallestRatioDistrict.population / smallestRatioDistrict.totalBedrooms)
       
        #Return the average people per bedroom of the districts
        print("Average people per bedroom: ", DataModifiers.avgPeoplePerBedroom(districtList))

        #Return the average median age across all districts
        print("Average age across all districts", DataModifiers.avgAge(districtList))

        #Return the average median income across all districts
        print("Average income across all districts", DataModifiers.avgIncome(districtList))

        #Return the districts by category
        print("District by location: ", District.nrOceanProximities)


        #Filter the list by the given criterium
        while True:
            try:
                userColumn = int(input("""Choose column to filter by: 0 - longitude 
                                                                      1 - latitude 
                                                                      2 - medianAge
                                                                      3 - totalRoom
                                                                      4 - totalBedroom 
                                                                      5 - population 
                                                                      6 - households
                                                                     7 - medianIncome
                                                                      8 - medianHouseValue
                                                                      9 - proximity """))
                
                    
            except ValueError:
                print("Not an integer!")
            else:
                break
        #userFilteredList = DataModifiers.userFilterList(userColumn)

        #Raise the price for all properties at the ocean
        raisedPricesList = [DataModifiers.raisePrice(elem) for elem in districtList]

        with open('raisedPrices.txt', 'w') as f:
            for item in raisedPricesList:
                f.write(str(item))
        
        #Sort the list by median house value
        sortedByMedianHouseValue = DataModifiers.sortByMedianHouseValue(districtList, False)


        with open('sortedByHouseValue.txt', 'w') as f:
            for item in sortedByMedianHouseValue:
                f.write(str(item))

        #Sort the list by ocean proximity
        sortedByOceanProximity = DataModifiers.sortByOceanProximity(districtList, False)

        with open('sortedByOceanProximity.txt', 'w') as f:
            for item in sortedByOceanProximity:
                f.write(str(item))

        #Let the user filter the list by the given criteria
        filteredList = DataModifiers.filterDistrictsByCriteria(districtList)

        with open('report.txt', 'w') as f:
            for item in filteredList:
                f.write(str(item))
        
        with open('preShiftList.txt', 'w') as f:
            for item in districtList:
                f.write(str(item))

        #Shift the whole continent
        DataModifiers.continentalShift(districtList)

        with open('postShiftList.txt', 'w') as f:
            for item in districtList:
                f.write(str(item))
        



if __name__ == "__main__":

    #RUN THE UNIT TESTS BEFORE RUNNING THE MAIN FUNCTION
    TestUnits.RunTests()

    #RUN THE MAIN FUNCTION
    MainClass.main()
    