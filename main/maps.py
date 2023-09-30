import googlemaps

# Підставте свій ключ API
gmaps = googlemaps.Client(key='AIzaSyDbCzGsAHX87x7ZALEZRuU95oQ9LYAqIDw')

# Використання API
# Наприклад, отримання координат за адресою
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
