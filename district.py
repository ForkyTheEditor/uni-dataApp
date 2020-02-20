class District:
    """ Object representing a district object 
        Attributes:

            districtID : int
            longitude : float
            latitude : float
            medianAge : float
            totalRoom : int
            totalBedroom : int
            population : int
            households : int
            medianIncome : float
            medianHouseValue : float 
            proximity : string """
    

    #Proximities dictionary containing string Keys and integer Values;
    #Represents the number of districts at each category
    nrOceanProximities = {}
    

    def __init__(self):


        self.__districtID = None

        self.__longitude = None
        self.__latitude = None
        self.__medianAge = None

        self.__totalRooms = None
        self.__totalBedrooms = None
        self.__population = None

        self.__households = None
        self.__medianIncome = None
        self.__medianHouseValue = None

        self.__proximity = 'N/A'
    
    def UpdateProximities(value):
        """ Checks whether a given proximity has been seen before 
            If it has, it adds 1 to the number of districts in that category
            If it hasn't, it first adds it to the list """

        

        try:
            value = str(value)
            
            if value in ['ocean_proximity', '']:           
                return

        except ValueError:
            print("Proximity value not a string!")
            return
        try:
            District.nrOceanProximities[value] += 1
        except:
            District.nrOceanProximities.update({value : 0})
            District.nrOceanProximities[value] += 1

        
    
    #DEFINE THE ATTRIBUTES
    #SET THEM EQUAL TO None IF ANY ERRORS COME UP

    @property
    def districtID(self):
        return self.__districtID

    #LONGITUDE
    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        try:
            self.__longitude = float(value)
        except ValueError:
            self.__longitude = None         

    #LATITUDE
    @property 
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        try:
            self.__latitude = float(value)
        except ValueError:
            self.__latitude = None

    #MEDIAN AGE
    @property
    def medianAge(self):
        return self.__medianAge

    @medianAge.setter
    def medianAge(self, value):
        try:
            self.__medianAge = float(value)
        except ValueError:
            self.__medianAge = None
      
    #TOTAL ROOMS
    @property
    def totalRooms(self):
        return self.__totalRooms

    @totalRooms.setter
    def totalRooms(self, value):
        try:
            #The data comes in as a float so the conversion must be first made as a float, then as an int
            self.__totalRooms = int(float(value))
        except ValueError:
            self.__totalRooms = None
    
    #TOTAL BEDROOMS
    @property
    def totalBedrooms(self):
        return self.__totalBedrooms

    @totalBedrooms.setter
    def totalBedrooms(self, value):
        try:
            #The data comes in as a float so the conversion must be first made as a float, then as an int
            self.__totalBedrooms = int(float(value))
        except ValueError:
            self.__totalBedrooms = None

    #POPULATION
    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        try:
            #The data comes in as a float so the conversion must be first made as a float, then as an int
            self.__population = int(float(value))
        except ValueError:
            self.__population = None

    #HOUSEHOLDS
    @property
    def households(self):
        return self.__households

    @households.setter
    def households(self, value):
        try:
            #The data comes in as a float so the conversion must be first made as a float, then as an int
            self.__households = int(float(value))
        except ValueError:
            self.__households = None

    #MEDIAN INCOME
    @property
    def medianIncome(self):
        return self.__medianIncome

    @medianIncome.setter
    def medianIncome(self, value):
        try:
            self.__medianIncome = float(value)
        except ValueError:
            self.__medianIncome = None

    #MEDIAN HOUSE VALUE
    @property
    def medianHouseValue(self):
        return self.__medianHouseValue

    @medianHouseValue.setter
    def medianHouseValue(self, value):
        try:
            self.__medianHouseValue = float(value)
        except ValueError:
            self.__medianHouseValue = None
    
    #PROXIMITY
    @property
    def proximity(self):
        return self.__proximity

    @proximity.setter
    def proximity(self, value):
        try:
            self.__proximity = str(value)
        except ValueError:
            self.__proximity = None

    def OrderedListToDistrict(list):
        """ Interpretes a list as a District type object 
            The corresponding positions get converted to:
            [0] longitude
            [1] latitude
            [2] medianAge
            [3] totalRooms
            [4] totalBedrooms
            [5] population
            [6] households
            [7] medianIncome
            [8] medianHouseValue
            [9] proximity
            In: List
            Out: District object"""

        localList = list.copy()
        districtToReturn = District()

        #Assign the proper values to the District properties
        try:
            districtToReturn.longitude = localList[0]
            districtToReturn.latitude = localList[1]
            districtToReturn.medianAge = localList[2]
            districtToReturn.totalRooms = localList[3]
            districtToReturn.totalBedrooms = localList[4]
            districtToReturn.population = localList[5]
            districtToReturn.households = localList[6]
            districtToReturn.medianIncome = localList[7]
            districtToReturn.medianHouseValue = localList[8]
            districtToReturn.proximity = localList[9]
        except IndexError:
            print("District list out of range!")

        return districtToReturn

    def __str__(self):
        return f'Long:{self.longitude} Lat:{self.latitude} Med_Age:{self.medianAge} Tot_Room:{self.totalRooms} Tot_Bedr:{self.totalBedrooms} Pop:{self.population} H_holds:{self.households} Med_Inc:{self.medianIncome} Med_hou_val:{self.medianHouseValue} Oce_Prox:{self.proximity}'
                                                                                                           
                  
