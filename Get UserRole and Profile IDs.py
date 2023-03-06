from simple_salesforce import Salesforce

sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token='o5Lnq85FAlchomgJD0hB3ZQWa', domain='test')

# Query for the Other UserRole
other_role = sf.query("SELECT Id FROM UserRole WHERE Name = 'Other'")

# Query for the Annuity Internal Wholesaler Profile
aiw_profile = sf.query("SELECT Id FROM Profile WHERE Name = 'Annuity Internal Wholesaler'")

# Print the results to the console
print("Other UserRole Id: ", other_role['records'][0]['Id'])
print("Annuity Internal Wholesaler Profile Id: ", aiw_profile['records'][0]['Id'])
