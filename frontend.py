import requests
import json

BASE_URL = "http://localhost:5000"


def menu():
    print("Blockchain Menu:")
    print("1. Mine a new block")
    print("2. Create a new transaction")
    print("3. View the full blockchain")
    print("4. Register new nodes")
    print("5. Resolve conflicts")
    print("6. Check wallet balance")
    print("7. Exit")


def mine_block():
    response = requests.get(f"{BASE_URL}/mine")
    print(json.dumps(response.json(), indent=4))


def create_transaction():
    sender = input("Enter sender address: ")
    recipient = input("Enter recipient address: ")
    amount = int(input("Enter amount: "))
    transaction_data = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    response = requests.post(f"{BASE_URL}/transactions/new", json=transaction_data)
    print(json.dumps(response.json(), indent=4))


def view_blockchain():
    response = requests.get(f"{BASE_URL}/chain")
    print(json.dumps(response.json(), indent=4))


def register_nodes():
    nodes = input("Enter nodes to register (comma-separated): ").split(',')
    nodes = [node.strip() for node in nodes]
    data = {
        "nodes": nodes
    }
    response = requests.post(f"{BASE_URL}/nodes/register", json=data)
    print(json.dumps(response.json(), indent=4))


def resolve_conflicts():
    response = requests.get(f"{BASE_URL}/nodes/resolve")
    print(json.dumps(response.json(), indent=4))


def check_balance():
    address = input("Enter wallet address: ")
    response = requests.get(f"{BASE_URL}/wallet/balance", params={'address': address})
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            mine_block()
        elif choice == '2':
            create_transaction()
        elif choice == '3':
            view_blockchain()
        elif choice == '4':
            register_nodes()
        elif choice == '5':
            resolve_conflicts()
        elif choice == '6':
            check_balance()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")