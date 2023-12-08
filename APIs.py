
import requests

#Two part joke program

def get_programming_joke():
	try:
		url = "https://v2.jokeapi.dev/joke/Programming?type=twopart"
		response = requests.get(url)
		response.raise_for_status()

		joke_data = response.json()

		if joke_data.get("error"):
			return "An error occurred fetching the joke."


		setup = joke_data["setup"]
		delivery = joke_data["delivery"]


		return f"{setup}\n...\n{delivery}"
	except requests.exceptions.RequestException as e:  # matcheing the exception in the requests module
		return f"An error occurred: {e}"


if __name__ == "__main__":
	print(get_programming_joke())


# weather forcast


def get_forecast_for_zip(zip_code):
	#latitude and longitude from the zip code
	zip_url = f"https://api.zippopotam.us/us/{zip_code}"
	try:
		zip_response = requests.get(zip_url)
		zip_response.raise_for_status()  # raise an error if the request fails
		zip_data = zip_response.json()

		#extract latitude and longitude
		latitude = zip_data['places'][0]['latitude']
		longitude = zip_data['places'][0]['longitude']
	except requests.RequestException as e:
		return f"An error occurred while retrieving location data: {e}"

	weather_url = f"https://api.weather.gov/points/{latitude},{longitude}"
	try:
		weather_response = requests.get(weather_url)
		weather_response.raise_for_status()
		weather_data = weather_response.json()
		forecast_url = weather_data['properties']['forecast']
		forecast_response = requests.get(forecast_url)
		forecast_response.raise_for_status()
		forecast_data = forecast_response.json()
		periods = forecast_data['properties']['periods']
		today_forecast = next((period for period in periods if period['isDaytime']), None)
		if today_forecast:
			return today_forecast['detailedForecast']
		else:
			return "No daytime forecast available for today."

	except requests.RequestException as e:
		return f"An error occurred while retrieving weather data: {e}"


zip_code_input = input("Please enter your zip code: ")
forecast = get_forecast_for_zip(zip_code_input)
print(forecast)




#get two APIs

def get_cat_image():
    fact_url = "https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=aZyiLrsCh"
    try:
        response = requests.get(fact_url)
        response.raise_for_status()
        fact = response.json().get('text')
        return fact
    except requests.RequestException as e:
        return f"An error occurred: {e}"


def get_book():
	dog_url = "https://wizard-world-api.herokuapp.com/swagger/index.html"
	try:
		response = requests.get(dog_url)
		response.raise_for_status()
		data = response.json()

		if 'message' in data:
			image_url = data['message']
			parts = image_url.split("/")
			breed = parts[-2] if len(parts) > 2 else "Unknown"
			return image_url, breed
		else:

			return None, "No image URL found"
	except requests.RequestException as e:
		return None, f"An error occurred: {e}"


cat_image, breed = get_cat_image()
if cat_image and breed:
	print(f"Here is a random dog image of a {breed}: {cat_image}")
else:
	print(breed)