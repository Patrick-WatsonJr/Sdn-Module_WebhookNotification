"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


#email address

addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#asks users to for email address to enter
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
#prints email addresses    

{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZWQ1MGQxZTAtMTUxNy0xMWViLWFlNmUtMjM0MmY0N2FmMDdk",
      "title": "SDN Postman Room",
      "type": "group",
      "isLocked": false,
      "lastActivity": "2020-10-23T12:38:19.643Z",
      "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jZTY4MDM2Mi02NGM1LTRhNmYtYWFmOS1hZTM4YmY2MWYwYWM",
      "created": "2020-10-23T10:10:07.486Z",
      "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi83ZmUxNWZlZC1jNjdiLTRkZGMtYjI5Yy0zOTMzOGI0ZDMwOWU"
    }
  ]
}

print(addresses)
