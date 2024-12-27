import meraki
import csv

# Replace with your API key
API_KEY = ''

# Replace with the path to your CSV file (r for raw string)
CSV_FILE_PATH = r""

# Initialize the Meraki Dashboard API client
dashboard = meraki.DashboardAPI(API_KEY)

# Get the organizations the API key can access
organizations = dashboard.organizations.getOrganizations()

# Print the available organizations and ask the user to select one
print("Available organizations:")

for i, org in enumerate(organizations, start=1):
    print(f"{i}. {org['name']} (ID: {org['id']}")
selected_org_num = int(input("Enter the number of the organization to use: "))

if selected_org_num < 1 or selected_org_num > len(organizations):
    print("Invalid selection. Exiting.")
    exit()

selected_org = organizations[selected_org_num - 1]
org_id = selected_org['id']

# Get the network names and IDs from the selected organization
networks = dashboard.organizations.getOrganizationNetworks(org_id)

# Print the available networks and ask the user to select one
print("Available networks:")

for i, network in enumerate(networks, start=1):
    print(f"{i}. {network['name']} (ID: {network['id']}")
selected_network_num = int(input("Enter the number of the network to use for device import: "))

if selected_network_num < 1 or selected_network_num > len(networks):
    print("Invalid selection. Exiting.")
    exit()

selected_network = networks[selected_network_num - 1]
network_id = selected_network['id']

# Read the CSV file
with open(CSV_FILE_PATH, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    # Iterate over each row in the CSV file
    for row in reader:
        serial = row[3]  # Assuming the serial number is in the 4th column
        # Add the device to the selected network
        try:
            dashboard.networks.claimNetworkDevices(
                networkId=network_id,
                serials=[serial]
            )
            print(f"Device {serial} added to the network {selected_network['name']}.")
        except meraki.APIError as e:
            print(f"Error adding device {serial}: {e}")