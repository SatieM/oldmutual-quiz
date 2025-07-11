import sys

clients = {}  


def add_client():
    client_id = input("Enter client ID: ").strip()
    if client_id in clients:
        print(" Client ID already exists.")
        return

    name = input("Enter client name: ").strip()
    fund = input("Enter Fund: ").strip()

    if not name or not fund:
        print(" Name and Fund cannot be empty.")
        return

    clients[client_id] = {"Name": name, "Fund": fund}
    print("Client added successfully!")


def view_clients():
    if not clients:
        print(" No clients found.")
        return

    print("===== CLIENT LIST =====")
    for cid, info in clients.items():
        print(f"ID: {cid} | Name: {info['Name']} | Fund: {info['Fund']}")
    print(f"Total clients: {len(clients)}")


def search_clients():
    keyword = input("Enter search term: ").strip().lower()
    results = {
        cid: info
        for cid, info in clients.items()
        if keyword in cid.lower()
        or keyword in info["Name"].lower()
        or keyword in info["Fund"].lower()
    }

    if results:
        print(f"Found {len(results)} client(s):")
        for cid, info in results.items():
            print(f"ID: {cid} | Name: {info['Name']} | Fund: {info['Fund']}")
    else:
        print(" No matching clients found.")


def edit_client():
    client_id = input("Enter client ID to edit: ").strip()
    if client_id not in clients:
        print(" Client not found.")
        return

    current = clients[client_id]
    print(f"Current details - ID: {client_id} | Name: {current['Name']} | Fund: {current['Fund']}")

    new_name = input("Enter new name (press Enter to keep current): ").strip()
    new_fund = input("Enter new Fund (press Enter to keep current): ").strip()

    if new_name:
        current["Name"] = new_name
    if new_fund:
        current["Fund"] = new_fund

    print("Client updated successfully!")


def delete_client():
    client_id = input("Enter client ID to delete: ").strip()
    if client_id not in clients:
        print(" Client not found.")
        return

    confirm = input(f"Are you sure you want to delete {clients[client_id]['Name']}? (y/n): ").strip().lower()
    if confirm == 'y':
        del clients[client_id]
        print("Client deleted Successfully!.")
    else:
        print("Deletion canceled.")


def main():
    while True:
        print("\n===== CLIENT MANAGEMENT SYSTEM =====")
        print("1. Add Client")
        print("2. View All Clients")
        print("3. Search Client")
        print("4. Edit Client")
        print("5. Delete Client")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_client()
        elif choice == '2':
            view_clients()
        elif choice == '3':
            search_clients()
        elif choice == '4':
            edit_client()
        elif choice == '5':
            delete_client()
        elif choice == '6':
            print(" Exiting")
            sys.exit()
        else:
            print(" Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

