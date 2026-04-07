
# Documentation - SCANNER_API.py (EN)

## Description
This script connects to an Aruba Wi-Fi controller via its REST API. It retrieves access point information and exports the results to a CSV file.

## Main Features
- Secure HTTPS connection to Aruba controller
- API authentication (login + session)
- Retrieves list of access points with details
- Exports to a CSV file

## Libraries Used
- `requests`, `getpass`, `csv`, `re`, `time`
- `urllib3` to suppress SSL warnings

## Output
A CSV file is generated containing extracted access point information.
