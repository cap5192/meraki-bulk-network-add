import backend

def main():
    orgs = backend.get_orgs()

    # Counters
    x = 1
    y = 1
    z = 1

    # Get Orgs
    for i in orgs:
        print(f"{x}. {i['name']}")
        x = x + 1
    print("This script is used to claim devices under CSV file into a network.")
    org_num = int(input("Select an organization by its number: "))
    org = orgs[org_num - 1]
    org_id = org['id']

    # Get Networks
    network = backend.get_networks(org_id)
    for i in network:
        print(f"{y}. {i['name']}")
        y = y + 1
    net_num = int(input("Select a destination network to claim devices by its number: "))
    net = network[net_num - 1]
    net_id = net['id']

    backend.claim_network_devices(net_id, org_id)

if __name__ == '__main__':
    main()
