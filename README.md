# Weather-Forecasting-Tool
A command-line tool that accepts a city's name and returns the current weather forecast.

# Programming language used to develop this project
Python

# Set up a development environment
  * Libraries used under this project
     argparse
     simple_chalk
     requests
  * Code Editor used
     VS Code
     
# Select a weather API
  * Here I have used OpenWeatherMap
  * Sign up for an API key
 
# Design the CLI Interface
  * Define the commands and options that users will interact with to retrive weather information
 
# Implement Argument Parsing
  * Used a command line argument parsing library "argparse"
  * This handles user input and command-line arguments
  * This allows users to pass arguments to CLI tool.

# Connect to weather API
  * Make http requests to the weather API using your api key
  * handle the API response using the requests library 

# At the place of 'my api key' you will be using your own api key which you can get by signing up in the OpenWeatherMap
  import argparse
  API_KEY='my api key'
  BASE_URL="https://api.openweathermap.org/data/2.5/weather"
