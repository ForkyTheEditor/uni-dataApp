from district import District
from dataModifiers import DataModifiers

class TestUnits:
    """ Object containing all of the test functions """


    #UNIT TESTS FOR THE RESPECTIVE FUNCTIONS
    def test_mostPopulousDistrict():

        distr1 = District()
        distr1.population = 150

        distr2 = District()
        distr2.population = 15

        distrList = [distr1, distr2]

        assert distr1 == DataModifiers.mostPopulousDistrict(distrList)


    def test_leastPopulousDistrict():

        distr1 = District()
        distr1.population = 12331

        distr2 = District()
        distr2.population = 15

        distrList = [distr1, distr2]

        assert distr2 == DataModifiers.leastPopulousDistrict(distrList)


    def test_mostPeoplePerBedroom():

        distr1 = District()
        distr1.population = 12
        distr1.totalBedrooms = 3

        distr2 = District()
        distr2.population = 18
        distr2.totalBedrooms = 3

        distrList = [distr1, distr2]

        assert distr2 == DataModifiers.mostPeoplePerBedroom(distrList)


    def test_leastPeoplePerBedroom():

        distr1 = District()
        distr1.population = 12
        distr1.totalBedrooms = 3

        distr2 = District()
        distr2.population = 18
        distr2.totalBedrooms = 3

        distrList = [distr1, distr2]

        assert distr1 == DataModifiers.leastPeoplePerBedroom(distrList)

    def test_avgIncome():

        distr1 = District()
        distr1.medianIncome = 10

        distr2 = District()
        distr2.medianIncome = 20

        distrList = [distr1, distr2]

        assert 15 == DataModifiers.avgIncome(distrList)

    def RunTests():
        """ Call this function to run all the unit tests """

        TestUnits.test_mostPopulousDistrict()
        TestUnits.test_leastPopulousDistrict()
        TestUnits.test_mostPeoplePerBedroom()
        TestUnits.test_leastPeoplePerBedroom()
        TestUnits.test_avgIncome()



