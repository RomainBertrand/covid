import data_by_country, data_analysis

if __name__=='__main__':
    possible_countries = data_by_country.list_possible_country_names()
    COUNTRY = ""
    attempts = 0
    while COUNTRY not in possible_countries:
        COUNTRY = input("De quel pays souhaitez-vous observer l'évolution?\n")
        attempts += 1
        if attempts > 2:
            print(possible_countries)
    data_analysis.analysis(data_by_country.data_by_country(COUNTRY))
