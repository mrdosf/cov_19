from covid import Covid

try:
    covid = Covid()
    covid.get_data()

    countries = covid.list_countries() #global var
    def banner():
        print("#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
        print("#                                   #")
        print("%       Covid-19 info grabber       %") 
        print("$                 - Md. Emam        $")
        print("#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
    banner()

    print("\n| You will get all the informations about Corona from this script for instance: \n # country list (list)\n # to know specific country info type (country) \n # to know about world info type (world) \n # type nothing to exit |")

    def corona_info():
        active = covid.get_total_active_cases()
        print("Total active case are:", active)
        
        confirmed = covid.get_total_confirmed_cases()
        print("Total confrimed cases:", confirmed)
        
        recovered = covid.get_total_recovered()
        print("Total recovered cases:",recovered)

        death = covid.get_total_deaths()
        print("Total deaths in the world:", death)


    def country_info():
        cntr_input = str(input("Which country you want to know about: \n "))
        case = covid.get_status_by_country_name(cntr_input)
        print('Here is the info of', cntr_input  + ':\n', case)

    def choice():
        #inputs from user
        opt_input = str(input("\n What do you want to know: "))
        
        if opt_input == "list":
            print("These are the countries with id to navigate later on this script \n you can use them to know more about them") 
            print(countries)
            print("\n Copy the country name to know the covid status of certain country")
        else:
            if opt_input == "world":
                corona_info()
            else:
                if opt_input == "country":
                    country_info()
                else:
                    if opt_input in ["nothing", "exit", "no"]:
                        print("okh bruh!!!!")
                        exit()
                    
    while True:
        choice()

except(ValueError):
    print(" something went wrong \n or you have just mistypen something \n **Check Again**")
