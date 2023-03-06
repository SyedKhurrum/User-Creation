from simple_salesforce import Salesforce

sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token='O2vpuER1zpuC2gRuiT8oiat1', domain='test')

# List of usernames to delete
usernames = ['khurrum.syed@brighthousefinancial.com.test4', 'khurrum.syed@brighthousefinancial.com.test3', 'khurrum.syed@brighthousefinancial.com.test2', 'khurrum.syed@brighthousefinancial.com.test']

# Get the user IDs for the specified usernames
user_ids = []
for username in usernames:
    result = sf.query(f"SELECT Id FROM User WHERE Username = '{username}'")
    if result['records']:
        user_ids.append(result['records'][0]['Id'])

# Delete the users
if user_ids:
    sf.bulk.User.delete(user_ids)
    print(f"Deleted {len(user_ids)} users.")
else:
    print("No users found to delete.")
