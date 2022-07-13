import os 
import json

def load_credentials():
    """Loads account credentials into a dictionary.

    Returns: 
        dict: Dictionary with the names of the supermarket brands as keys each key has a dict associated
        with username, password and site of the supermarket. For example:
        
        {'Supermarket_1': {
                'username': 'User1@example.com',
                'password': 'pass1',
                'site': 'https://www.supermarket_1.com/shop'
            },
        'Supermarket_2': {
                'username': 'User2@example.com',
                'password': 'pass2',
                'site': 'https://www.supermarket_2.com/shop'
            }
        }
        
    Raises:
        JSONDecodeError: An error ocurred with the JSON format.
        FileNotFoundError: File containing the credentials not found.
    """
    credentials_path = os.path.join(os.getcwd(), 'keys\keys.json')
    credentials = {}
    try:
        with open(credentials_path) as json_file:
            credentials = json.load(json_file)
    except json.JSONDecodeError:
        print("JSON format error")
        exit()
    except FileNotFoundError:
        print('keys.json not found')
        exit()
    else:
        return credentials

