import meraki
import os
from dotenv import load_dotenv
import json
import pandas as pd
import csv

file_name = 'meraki-serials.csv'

# load all environment variables
load_dotenv()


def get_orgs():
    """Gets the list of all orgs (name and id) that admin has access to"""
    orgs = []
    dict = {"id": "", "name": ""}
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.getOrganizations()

    for i in response:
        dict["id"] = i["id"]
        dict["name"] = i["name"]
        orgs.append(dict)
        dict = {"id": "", "name": ""}

    return orgs


def get_networks(org_id):
    """Get a list of networks and returns dict with net IDs and names"""
    nets = []
    dict = {"id": "", "name": ""}
    # collect network names
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.getOrganizationNetworks(
        org_id, total_pages='all'
    )
    for i in response:
        dict["id"] = i["id"]
        dict["name"] = i["name"]
        nets.append(dict)
        dict = {"id": "", "name": ""}

    return nets

def check_serials_claimed(serials_check, org_id):
    """Checks if serial numbers are already in the org or not. If they are not in the org, returns false"""
    serial_claimed = []
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.getOrganizationInventoryDevices(org_id, total_pages='all')
    for i in response:
        serial_claimed.append(i['serial'])
    # print(serial_claimed)
    # print(serials_check)
    # matches = set(serials_check) & set(serial_claimed)
    for z in serials_check:
        if z not in serial_claimed:
            print(f"{z} is not in the inventory")
            return False
    return True


def claim_network_devices(net_id, org_id):
    """Checks if the devices are claimed or not in the org, and then claims them into a network"""
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    serials = []
    with open(file_name, newline='') as file:

        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            serials.append(row[0])
    if serials:
        if check_serials_claimed(serials, org_id) == True:
            print("Claiming devices...")
            for i in serials:
                print(i)
            print("Please wait...")
            response = dashboard.networks.claimNetworkDevices(net_id, serials)
            print("Devices claimed successfully")

    else:
        print("no data in csv file")