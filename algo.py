import requests

api_key = open('api_key.txt', 'r').read()

while True:
    location = input('Enter the city: ')

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
    if result.json()['cod'] == '404':
        print('City not found')
        continue
    break

description = result.json()['weather'][0]['description']
temp = round(result.json()['main']['temp'])
min_temp = round(result.json()['main']['temp_min'])
max_temp = round(result.json()['main']['temp_max'])

print(f'Current weather in {location[0].upper() + location[1:]}: {description}')
print(f'Temperature: {temp}°C')
print(f'Min temperature: {min_temp}°C')
print(f'Max temperature: {max_temp}°C')