import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_contacts(self):
        response = requests.get(f'{self.base_url}/contacts/')
        return response.json()

if __name__ == '__main__':
    client = APIClient('http://127.0.0.1:8000/api')
    contacts = client.get_contacts()
    for contact in contacts:
        print(contact)
