import pandas as pd
import json
import logging
from geocodio import GeocodioClient, GeocodioError

# Configure logging
logging.basicConfig(
    filename='geocoding_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to batch geocode with error handling and logging
def batch_geocode(input_csv, output_json, api_key):
    try:
        # Initialize the Geocodio client
        client = GeocodioClient(api_key)

        # Log start of process
        logging.info(f"Starting geocoding for file: {input_csv}")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_csv)

        # Ensure the CSV contains the required columns
        required_columns = ['FID', 'ID', 'address', 'city', 'state', 'zip']
        for col in required_columns:
            if col not in df.columns:
                logging.error(f"Missing column: {col}")
                raise ValueError(f"Input CSV must contain the '{col}' column")

        # Combine address, city, state, and zip into a full address string
        df['full_address'] = df['address'] + ', ' + df['city'] + ', ' + df['state'] + ' ' + df['zip'].astype(str)

        # Extract the full addresses
        addresses = df['full_address'].tolist()

        # Geocode the addresses in batches of up to 10,000
        geocode_results = []
        batch_size = 10000
        for i in range(0, len(addresses), batch_size):  # Geocodio batches in groups of 10,000
            batch = addresses[i:i + batch_size]
            batch_number = i // batch_size + 1
            try:
                logging.info(f"Processing batch {batch_number} (records {i + 1} to {i + len(batch)})")
                
                # Call Geocodio API for geocoding with optional fields (census data)
                geocode_batch_results = client.geocode(batch, fields=["census2000", "census2010", "census2020"])

                # Create a custom result structure that includes original fields and geocoded data
                for j, result in enumerate(geocode_batch_results['results']):
                    record = {
                        'FID': df.iloc[i + j]['FID'],
                        'ID': df.iloc[i + j]['ID'],
                        'address': df.iloc[i + j]['address'],
                        'city': df.iloc[i + j]['city'],
                        'state': df.iloc[i + j]['state'],
                        'zip': df.iloc[i + j]['zip'],
                        'geocoded_address': result['formatted_address'],
                        'latitude': result['location']['lat'],
                        'longitude': result['location']['lng'],
                        'accuracy': result.get('accuracy'),
                        'census2000': result.get('fields', {}).get('census2000', {}),
                        'census2010': result.get('fields', {}).get('census2010', {}),
                        'census2020': result.get('fields', {}).get('census2020', {})
                    }
                    geocode_results.append(record)
                
                logging.info(f"Successfully geocoded batch {batch_number} (records {i + 1} to {i + len(batch)})")

            except GeocodioError as e:
                logging.error(f"Error during geocoding batch {batch_number} (records {i + 1} to {i + len(batch)}): {str(e)}")
                raise

        # Write the results to a JSON file
        with open(output_json, 'w') as json_file:
            json.dump(geocode_results, json_file, indent=4)

        # Log completion
        logging.info(f"Geocoding complete. Results saved to {output_json}")

    except Exception as e:
        logging.error(f"Failed to process geocoding: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    input_csv = "input_addresses.csv"  # Your CSV input file
    output_json = "output_geocoded_results.json"  # Output JSON file
    api_key = "your_geocodio_api_key"  # Replace with your actual Geocodio API key

    try:
        batch_geocode(input_csv, output_json, api_key)
    except Exception as e:
        print(f"An error occurred: {str(e)}. Check the log file for more details.")
