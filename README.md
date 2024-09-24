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

## Jupyter Notebook

In addition to the Python script, this project includes a Jupyter Notebook (`geocoding_batch_notebook.ipynb`) for interactive execution and debugging of the batch geocoding process. The notebook breaks the process into multiple cells, allowing for step-by-step execution and easier debugging.

### Usage Instructions:
1. **Install Dependencies**: The first cell in the notebook includes commands to install the required libraries (`pandas`, `pygeocodio`). Make sure to uncomment and run the installation cell if the packages are not already installed.
   
2. **Load and Inspect Data**: The notebook allows you to load the CSV data, inspect the first few rows, and validate that the required columns are present before proceeding.

3. **Configure Geocodio API**: Enter your Geocodio API key in the designated cell to initialize the API client.

4. **Step-by-Step Execution**: You can run the notebook cells sequentially to:
   - Prepare the full address for geocoding.
   - Perform batch geocoding in steps.
   - Inspect and process the results before saving them to a JSON file.

5. **Interactive Debugging**: The notebook is designed to make it easier to debug individual steps without rerunning the entire script, making it ideal for testing and troubleshooting.

This notebook is useful for those who prefer to interact with the data and the geocoding process in a more granular, cell-by-cell manner.