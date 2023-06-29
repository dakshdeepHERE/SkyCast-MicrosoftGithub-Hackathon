import requests
import typer

app = typer.Typer()


@app.command()
def weather(city: str):
    api_key = "Your open weather api"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        typer.echo(f"Weather in {city}:")
        typer.echo(f"Description: {weather_description}")
        typer.echo(f"Temperature: {temperature}K")
        typer.echo(f"Humidity: {humidity}%")
        typer.echo(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError as e:
        typer.echo(f"Error: {e.response.status_code} - {e.response.reason}")
    except KeyError:
        typer.echo(f"Error: Invalid response format from OpenWeatherMap API")
    except Exception as e:
        typer.echo(f"An error occurred: {e}")


if __name__ == "__main__":
    app()
