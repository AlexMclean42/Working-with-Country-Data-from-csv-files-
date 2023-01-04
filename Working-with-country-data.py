
#ALEXANDER MCLEAN, DOMINICO MENDES, F21
import numpy as np
import matplotlib.pyplot as plt

class CountryData:
    '''
    A class used to create a countrydata object.
    Attributes:
        name (str): String that represents the country's name
        stat (str): String that represents the selected user statistic
    '''
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat
    
    def print_all_stats(self):
        '''
        A function that prints the name and stat of the country and statistic selected.
        Parameters: None
        Returns: None
        '''
        print("Country Name: {0}, Statistic: {1}".format(self.name, self.stat))
    
def main():
    
    # Intro print statement
    print("Working with Country Data\n")
    
    # Lists of countries, statistics, years, country independant statistics
    list_of_countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium', 'Belize','Benin','Bhutan','Bolivia', 'Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombia','Comoros','Costa Rica','Cote d\'Ivoire','Croatia','Cuba','Cyprus','Czech Republic','Dem. Rep. of Congo','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea', 'Estonia', 'Eswatini','Ethiopia','Fed. Sts. Micronesia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyz Republic','Lao','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panama','P\'apua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Rep. of Congo','Romania','Russia','Rwanda','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovak Republic','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','St. Kitts and Nevis','St. Lucia','St. Vincent and the Grenadines','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
    list_of_statistics = ['Population Change', 'Certain Year Population', 'Location', 'Total Threatened Animals', 'The min number of threatened plants', 'The max number of threatened plants', 'The min number of threatened fish', 'The max number of threatened fish', 'The min number of threatened birds', 'The max number of threatened birds', 'The min number of threatened mammals', 'The max number of threatened mammals']
    list_of_years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    list_of_nocountry_statistics =  ['The min number of threatened plants' , 'The mix number of threatened plants' , 'The min number of threatened fish' , 'The max number of threatened fish' , 'The min number of threatened birds' , 'The max number of threatened birds' , 'The min number of threatened mammals','The max number of threatened mammals']
    
    # Importing csv files
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True, encoding= 'utf-8', dtype= None)    # Array 1
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter = ',', skip_header = True)    # Array 2
    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, encoding= 'utf-8', dtype= None)    # Array 3
    
    # User input for countries
    print(list_of_countries)
    input_country = input('Please enter a country from the list above: ')
    
    # While loop to check if inputted country is valid
    search = True
    while search:
        if input_country in list_of_countries:    # If input country in list of countries
            name = input_country
            break
        else:    # If input country not in list of countries
            # Prompts user for a valid input
            print('You must enter a valid country.')
            input_country = input('Please enter a country from the list above: ')
    print()
    
    # Prompts user for statistic input
    print(list_of_statistics)
    input_statistic = input('Please enter a statistic from the list above: ')
    
    # While loop to check if inputted statistic is valid
    while search:
        if input_statistic in list_of_statistics:    # If statistic is valid
            stat = input_statistic # Valid statistic = input statistic
            break
        else:    # If statistic is invalid
            # Prompts user for a valid statistic input
            print('You must enter a valid statistic choice.')
            input_statistic = input('Please enter a statistic from the list above: ')
    
    print()
    
    country = CountryData(name, stat) # Creates an instance of the class 'CountryData' with parameters 'name' (country name input) and 'stat' (statistic input)
    country_index = list_of_countries.index(str(name)) # Assigns index value of input country in list of countries to country_index variable
    
    # If input statistic not in country independant statistics, print
    if input_statistic not in list_of_nocountry_statistics:
        country.print_all_stats()
    
    # If statistic choice is 'Population Change'
    if input_statistic == 'Population Change':
        population_change = float(population_data[country_index][21] - population_data[country_index][1])    # Finding change in population from 2000-2020
        yes_no_input = input('Would you like to create a graph, yes or no: ')    # Prompting user if they would like to create a graph or not
        
        if yes_no_input == 'yes':    # If user inputs 'yes' to create a graph
            
            # Checking to see if population increased or decreased
            if population_change >= 0:
                pop_change = 'increased'
            else:
                pop_change = 'decreased'
            
            # Printing statement of population change and how much the population changeed by
            print('The population change of', input_country,'from 2000 - 2020', pop_change, 'at a rate of: {:.0f} people'.format(population_change))
            
            # Creates a list of population data from 2000-2020
            years_2000_2020 = population_data[country_index][1], population_data[country_index][2], population_data[country_index][3], population_data[country_index][4], population_data[country_index][5], population_data[country_index][6], population_data[country_index][7], population_data[country_index][8], population_data[country_index][9], population_data[country_index][10], population_data[country_index][11], population_data[country_index][12], population_data[country_index][13], population_data[country_index][14], population_data[country_index][15], population_data[country_index][16], population_data[country_index][17], population_data[country_index][18], population_data[country_index][19], population_data[country_index][20],  population_data[country_index][21]
            
            # Plotting population data graph
            plt.subplot(1,1,1)
            plt.plot(list_of_years, years_2000_2020, 'y--', label = "Population data")
            
            # Labeling and formatting graph
            plt.legend(shadow=True, loc="upper left")
            plt.xticks(list_of_years)
            plt.ylabel("Number of People")
            plt.xlabel("Year number")
            plt.title(f'Population of {input_country} from 2000-2020')
            
            # Outputting graph
            plt.show()
    
    # If statistic choice is 'Certain Year Population'
    if input_statistic == 'Certain Year Population':
        input_year = int(input('Please choose a year from 2000 - 2020: '))   # Prompts user for specific year input
        while input_year not in list_of_years:
            print('Please enter a valid year.')
            input_year = int(input('Please choose a year from 2000 - 2020: '))
        if input_year in list_of_years:
            year_index = list_of_years.index(int(input_year) + 1)    # Finding index value of input year in list of years
            year_pop = population_data[country_index][year_index]    # Finding population based on input country and year
            print('The population of', input_country, 'in', input_year, 'is', int(year_pop))

    # If statistic choice is 'Location'
    if input_statistic == 'Location':
        
        # Finding UN Region, UN Sub Region, and Country Distance based on user's input country from Country_Data.csv and assigning them to variables
        un_region = country_data[country_index][1]
        un_sub_region = country_data[country_index][2]
        country_distance = country_data[country_index][3]
        
        # Output statement with input country, UN Region, UN Sub Region, and Country Distance
        print(input_country, 'is located in,', un_region, 'which is located in,', un_sub_region, 'which has a square kilometer distance of,', int(country_distance))
    
    # If statistic choice is 'Total Threatened Animals'
    if input_statistic == 'Total Threatened Animals':
            yes_no_input = input('Would you like to create a graph, yes or no: ')    # Prompts user if they want to create a graph or not
            country_animals = int(threatened_species[country_index][1] + threatened_species[country_index][2] + threatened_species[country_index][3] + threatened_species[country_index][4])    # Total threatened species according to user's input country
            print('The total number of threatened animals of', input_country, 'is', country_animals)
            print()
    
            # If user wants to create a graph
            if yes_no_input == 'yes':
                animals = ('Plants','Fish','Birds','Mammals')
                
                # Assigning variables with each amount of threatened species based off the corresponding index of the user's input country
                country_plants = [threatened_species[country_index][1]]
                country_fish =  [threatened_species[country_index][2]]
                country_birds = [threatened_species[country_index][3]]
                country_mammals = [threatened_species[country_index][4]]
                
                # Plotting a graph of 'Total Threatened Animals'
                plt.subplot(1,1,1)
                plt.plot('Plants', country_plants, 'o', color = 'seagreen', label = "Threatened Plants")
                plt.plot('Fish', country_fish, 'o', color = 'mediumblue', label = "Threatened Fish")
                plt.plot('Birds', country_birds, 'o', color = 'darkgoldenrod', label = "Threatened Birds")
                plt.plot('Mammals', country_mammals, 'o', color = 'saddlebrown', label = "Threatened Mammals")
                
                # Labeling and formatiing graph
                plt.legend(shadow=True, loc="upper right")
                plt.xticks(animals)
                plt.xlabel("Different types of species")
                plt.ylabel("Number of threatened species")
                plt.title(f'Number of threatened species in {input_country}')
                
                # Outputting graph
                plt.show()
    
    # If statistic choice is in the list of country independant statistics
    if input_statistic in list_of_nocountry_statistics:
        
        # Prompts user to decide if a graph of all min and max data of all threatened species should be created and outputted
        print_max_min_graph = input('Would you like to print a graph containing all max and min data? \nPlease choose yes or no: ')
        
        # Finding min and max number of threatened plants
        min_plants = threatened_species[:,1].min()
        max_plants = threatened_species[:,1].max()
        
        # Finding min and max number of threatened fish
        min_fish = threatened_species[:,2].min()
        max_fish = threatened_species[:,2].max()
        
        # Finding min and max number of threatened birds
        min_birds = threatened_species[:,3].min()
        max_birds = threatened_species[:,3].max()
        
        # Finding min and max number of threatened mammals
        min_mammals = threatened_species[:,3].min()
        max_mammals = threatened_species[:,3].max()
    
        # If statistic choice is 'The min number of threatened plants'
        if input_statistic == 'The min number of threatened plants':
            print('The min number of plants is', int(min_plants))
        
        # If statistic choice is 'The max number of threatened plants'
        if input_statistic == 'The max number of threatened plants':
            print('The max number of plants is', int(max_plants))
        
        # If statistic choice is 'The min number of threatened Fish'
        if input_statistic == 'The min number of threatened fish':
            print('The min number of fish is', int(min_fish))
        
        # If statistic choice is 'The max number of threatened Fish'
        if input_statistic == 'The max number of threatened fish':
            print('The max number of fish is', int(max_fish))
        
        # If statistic choice is 'The min number of threatened birds'
        if input_statistic == 'The min number of threatened birds':
            print('The min number of threatened birds is', int(min_birds))
        
        # If statistic choice is 'The max number of threatened birds'
        if input_statistic == 'The max number of threatened birds':
            print('The max number of threatened birds is', int(max_birds))
        
        # If statistic choice is 'The min number of threatened mammals'
        if input_statistic == 'The min number of threatened mammals':
            print('The min number of threatened mammals is', int(min_mammals))
        
        # If statistic choice is 'The max number of threatened mammals'
        if input_statistic == 'The max number of threatened mammals':
            print('The max number of threatened mammals is', int(max_mammals))
        
        # If user wants to create a graph
        if print_max_min_graph == 'yes':
            
            # Plotting Min and Max Plants
            plt.bar('Min Plants', min_plants, color = 'mediumseagreen', label = 'Min Plants')
            plt.bar('Max Plants', max_plants, color = 'seagreen', label = 'Max Plants')
            
            # Plotting Min and Max Fish
            plt.bar('Min Fish', min_fish, color = 'cornflowerblue', label = 'Min Fish')
            plt.bar('Max Fish', max_fish, color = 'mediumblue', label = 'Max Fish')
            
            # Plotting Min and Max Birds
            plt.bar('Min Birds', min_birds, color = 'gold', label = 'Min Birds')
            plt.bar('Max Birds', max_birds, color = 'darkgoldenrod', label = 'Max Birds')
            
            # Plotting Min and Max Mammals
            plt.bar('Min Mammals', min_mammals, color = 'sandybrown', label = 'Min Mammals')
            plt.bar('Max Mammals', max_mammals, color = 'saddlebrown', label = 'Max Mammals')
            
            # Labeling and formatting graph
            plt.xlabel('Type of Animal')
            plt.ylabel('Number of Threatened Species')
            plt.legend(shadow = True, loc = "upper right")
            plt.title('Total Min Max Data')
            plt.grid(True)
            
            # Outputting graph
            plt.show()
    
    # Do not modify the code below
if __name__ == '__main__':
    main()
