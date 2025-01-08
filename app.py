from flask import Flask, render_template, request, redirect, url_for
import weather_api
import database
import json
import os
from dotenv import load_dotenv
load_dotenv()
YANDEX_API_KEY = os.getenv('YANDEX_MAPS_API_KEY')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    units = request.args.get("units", "celcius")
    if request.method == "POST":
        city = request.form["city"]
        weather_data = weather_api.get_weather(city, units)
        if weather_data:
            database.add_history(city)
            dates, temps = weather_api.get_forecast_data(city, units)
            lat, lon = weather_api.get_city_coordinates(city)
            if dates and temps:
                return render_template("index.html", weather_data=weather_data, city=city, chart_data=json.dumps({"labels": dates, "temps": temps}), lat=lat, lon=lon, units=units)
            else:
                return render_template("index.html", error="Не удалось получить данные для графика.", units=units)
        else:
            return render_template("index.html", error="Город не найден.", units=units)
    return render_template("index.html", units=units)


@app.route("/history")
def history():
    history = database.get_history()
    return render_template("history.html", history=history)


if __name__ == "__main__":
    database.init_db()
    app.run(debug=True)
