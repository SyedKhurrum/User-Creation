import requests
from simple_salesforce import Salesforce

sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token='o5Lnq85FAlchomgJD0hB3ZQWa', domain='test')

user_info = {
    'LastName': 'Syed',
    'FirstName': 'Khurrum',
    'Email': 'khurrum.syed@brighthousefinancial.com',
    'Username': 'khurrum.syed@brighthousefinancial.com.test5',
    'Alias': 'KS',
    'CommunityNickname': 'johndoe5',
    'TimeZoneSidKey': 'America/Los_Angeles',
    'LocaleSidKey': 'en_US',
    'EmailEncodingKey': 'UTF-8',
    'LanguageLocaleKey': 'en_US',
    'ProfileId': '00e46000001EdI7AAK',
    'UserRoleId': '00E46000000HnsEEAS',
    'IsActive': True,
    'TimeZoneSidKey': 'America/Los_Angeles',
    'LocaleSidKey': 'en_US',
    'EmailEncodingKey': 'UTF-8',
    'LanguageLocaleKey': 'en_US'
}

# Create the new user
new_user = sf.User.create(user_info)

