import datetime
import requests

def get_covid_data():
    from canvas import label, label2

    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    population = str(json_data['population'])
    recovered = str(json_data['recovered'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
    label.config(text="Total Cases: " + total_cases
                 +"\nTotal Deaths: " + total_deaths
                 + "\nToday Cases: " + today_cases
                 + "\nToday Deaths: " + today_deaths
                 + "\nPopulation: " + population
                 + "\nRecovered: " + recovered)
    label2.config(text=formatted_date)



