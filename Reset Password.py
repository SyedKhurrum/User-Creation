import requests
from simple_salesforce import Salesforce
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Connect to Salesforce
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token='o5Lnq85FAlchomgJD0hB3ZQWa', domain='test')

# Query for the user ID
query = "SELECT Id FROM User WHERE Username = 'khurrum.syed@brighthousefinancial.com.test'"
result = sf.query(query)
user_id = result['records'][0]['Id']
logging.debug(f'User ID: {user_id}')

# Reset the user's password
headers = {
    'Content-type': 'application/json',
    'Authorization': f'Bearer {sf.session_id}'
}
response = requests.delete(sf.base_url + f'sobjects/User/{user_id}/password', headers=headers)
if response.status_code == 204:
    logging.info('Password reset for user.')
else:
    logging.error(f'Error resetting password: {response.content}')
