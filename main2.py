import json

organizations=[]
file=open('organizations.json', 'r')
data=json.load(file)
file.close()
organizations=data['organizations']
print('Dati loaded')

while (True):
    response=input('(1) Add organization (2) Print organization (3) Exit')
    if response=='1':
        organization_name=input('Organization name: ')
        organization_adress=input('Organization adress: ')
        organization_id=input('Organization id: ')

        organization={
            'name':organization_name,
            'adress':organization_adress,
            'id': organization_id,
             'contacts': []
         }  
        while (True):
             response=input('Do you want to add contact (y/n)')
             if response=='y':
                contact_name=input('Contact name: ')
                contact_position=input('Contact position: ')
                contact_id=input('Contact id: ')

                contact={
                    'name': 'contact_name',
                    'position': contact_position,
                    'id':contact_id
                }
                organization['contacts'].append(contact)
             elif response=='n':
                break
        organizations.append(organization)
    elif response=='2':
        for organization in organizations:
              print('---ORGANIZATION---')
              print(f"{organization['name']}({organization['id']})")
              print(f"Adrese:{organization['adress']}")
              print(f"Kontaktu skaits:{len(organization['contacts'])}")
    elif response=='3':
         
         data={
             'organizations':organizations
         }
         print('Saving data...')
         file=open('organizations.json', 'w')
         json.dump(data,file, indent=4)
         print('Bye bye!')
         exit()
    else:
        print('Choose a number between 1-3')
        continue