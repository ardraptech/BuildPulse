import requests
from datetime import datetime

today = datetime.now()

try:
    weather = requests.get("https://wttr.in/?format=3").text
except:
    weather = "Weather information unavailable"

try:
    quote = requests.get(
        "https://zenquotes.io/api/random"
    ).json()[0]["q"]
except:
    quote = "Quote unavailable"

summary = f"""
Daily Report

Date:
{today}

Weather:
{weather}

Quote:
{quote}
"""

print(summary)

# Create unique file name using date and time
date_string = today.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{date_string}.txt"

# Save report
with open(filename, "w", encoding="utf-8") as file:
    file.write(summary)

print(f"\nReport saved as: {filename}")
