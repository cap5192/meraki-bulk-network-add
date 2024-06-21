# meraki-bulk-network-add

This script allows you to bulk-claim Meraki devices which are already present under a dashboard organization into a network of your choice. This script can help admins bulk-add Meraki devices if they already have a network created. This can work across different types of Meraki devices, except MXs. 

To run this script, add your Meraki API key with appropriate priviledges under .env file, download dependencies using requirements.txt file.
Add a list of serial numbers of Meraki devices you would like to claim inside a network in the 'serial' row of the CSV file. 
Run the script, select the organization and network that you would like to claim all of the listed devices into.

This script does not have error checks, so ensure you have correct type of devices, they are already claimed within an organization and are not claimed inside a network.
