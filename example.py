from WeatherQualityCSB import WeatherQuality

locations = {
    "ankara": []
}

dates = ("04.07.2023 09:00", "05.07.2023 09:00")

test = WeatherQuality(locations, dates, headless=False, logs=True)
test.run()
