# Batch Geocoding with Geocodio API

This project is designed to process a batch of addresses from a CSV file and geocode them using the Geocodio API. The script reads the CSV file, sends the addresses to the Geocodio API in batches of up to 10,000 addresses, retrieves geocoding data (including census fields from 2000, 2010, and 2020), and outputs the results into a JSON file.

## Features
- Batch geocoding for large datasets using the Geocodio API.
- Logs each batch processing step and errors in `geocoding_log.log`.

## Project Structure

- **`main.py`**: The main script that performs batch geocoding using the Geocodio API.
- **`output_geocoded_results.json`**: Output JSON file containing the geocoded addresses along with census data.
- **`geocoding_log.log`**: Log file for tracking batch processing and any errors encountered.
- **`.gitignore`**: Ensures that sensitive and unnecessary files like virtual environment files are ignored by Git.
- **`requirements.txt`**: Lists all the dependencies required for running the project.

## Prerequisites

- Python 3.7 or above
- A Geocodio API key (You can obtain this from [Geocodio](https://www.geocod.io/))
