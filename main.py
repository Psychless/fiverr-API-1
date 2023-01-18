import requests
import json

search_API_url = "https://api.tech.ec.europa.eu/search-api/prod/rest/search?apiKey=SEDIA&text=***"
facet_API_url = "https://api.tech.ec.europa.eu/search-api/prod/rest/facet?apiKey=SEDIA&text=***"

try:

    print("Search API data fetching...")
    # Make the search API request
    response = requests.post(search_API_url)

    # Check if the request was successful
    response.raise_for_status()

    print("Search API data fetched succesfully!")

    # Parse the JSON data
    data = json.loads(response.text)

    # Write the JSON data to a text file
    with open('Search_API_JSON_output.txt', 'w') as outfile:
        json.dump(data, outfile)
    
    print("Search API data successfully exported!")

    print("------------------------------")
    # ------------------------------------------------------
    print("Facet API data fetching...")
    # Make the facet API request
    response = requests.post(facet_API_url)

    # Check if the request was successful
    response.raise_for_status()

    print("Facet API data fetched succesfully!")

    # Parse the JSON data
    data = json.loads(response.text)

    # Write the JSON data to a text file
    with open('Facet_API_JSON_output.txt', 'w') as outfile:
        json.dump(data, outfile)
    
    print("Facet API data successfully exported!")

except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except requests.exceptions.ConnectionError as err:
    print(f'Error Connecting: {err}') 
except requests.exceptions.Timeout as err:
    print(f'Timeout Error: {err}') 
except requests.exceptions.RequestException as err:
    # catastrophic error. bail.
    print (f'Other Error : {err}')

input("\nPress Enter to exit...")