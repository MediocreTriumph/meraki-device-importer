# Meraki Device Importer

A Python script for bulk importing devices into Meraki networks using CSV files. This tool streamlines the process of claiming multiple devices into a Meraki network.

## Features

- Interactive organization and network selection
- Bulk device importing from CSV
- Error handling for API operations
- Progress feedback for each device import

## Prerequisites

- Python 3.6+
- Meraki Python SDK
- Meraki API key with write access
- CSV file containing device serial numbers

## Installation

1. Install required packages:
   ```bash
   pip install meraki
   ```

2. Update the script with your credentials:
   - Set `API_KEY` to your Meraki Dashboard API key
   - Set `CSV_FILE_PATH` to the path of your CSV file

## Usage

1. Prepare a CSV file with device serial numbers in the 4th column (index 3)
2. Run the script:
   ```bash
   python device_importer.py
   ```
3. Select your organization from the list
4. Select the target network
5. The script will process each device and show progress

## CSV Format

The script expects a CSV file with serial numbers in the 4th column (index 3). The CSV should have a header row which will be skipped during processing.

Example format:
```csv
Name,Model,MAC,Serial
Device1,MR46,00:11:22:33:44:55,Q2XX-YYYY-ZZZZ
```

## Error Handling

The script includes error handling for common scenarios:
- Missing or invalid CSV file
- API authentication failures
- Device claiming errors
- Invalid organization/network selection

All errors are displayed in the console with relevant details.