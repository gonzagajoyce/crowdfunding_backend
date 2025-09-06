# Crowdfunding Back End
Joyce Gonzaga

## Planning:
### Concept/Name
ENGLISH FOR HOPE is more than just a fundraiser, it’s a movement to spark dreams and transform futures!
Through campaigns, we give children from underprivileged communities in Brazil the chance to learn English, a skill that opens doors to brighter opportunities, global connections, and the confidence to dream bigger. 
Every donation is a step toward change, and donors can directly see the impact of their contributions, becoming part of an inspiring journey of growth and hope.

### Intended Audience/User Stories
Target Audience: Adults who care about education, social causes, and making a positive impact in children’s lives.

User Stories:
As a donor, I want to explore fundraisers and donate easily.
As a donor, I want to choose a custom amount so I can contribute in a way that feels personal.
As a donor, I want to receive a confirmation so I know my contribution was successful.
As a donor, I want to feel inspired by the impact of my donation.
As an admin, I want to track total donations collected across campaigns.

### Front End Pages/Functionality
Displays fundraiser name, inspiring description, goal amount, and total raised.
"Donate" button leading to the donation page.

Donation Page
Simple form to enter a donation amount (customizable).
Confirmation message after donation.
Thank you message showing the positive impact of the contribution.

Admin Dashboard
View total donations collected per fundraiser.
Manage campaigns and track progress.

### API Spec

| URL                   | HTTP Method | Purpose                        | Request Body                                                                 | Success Response Code | Authentication/Authorisation        |
| ---------------------- | ----------- | ------------------------------ | ---------------------------------------------------------------------------- | --------------------- | ----------------------------------- |
| /fundraisers/          | GET         | Get all fundraisers            | N/A                                                                          | 200                   | Public                              |
| /fundraisers/          | POST        | Create a new fundraiser        | {"title": "", "description": "", "goal": 1000, "image": "", "is_open": true} | 201                   | Authenticated user only             |
| /fundraisers/<id>/     | GET         | Get fundraiser details         | N/A                                                                          | 200                   | Public                              |
| /fundraisers/<id>/     | PUT         | Update fundraiser              | {"title": "", "description": "", "goal": 1200, "is_open": false}             | 200                   | Owner only                          |
| /pledges/              | GET         | Get all pledges                | N/A                                                                          | 200                   | Public                              |
| /pledges/              | POST        | Create pledge                  | {"amount": 50, "comment": "", "anonymous": false, "fundraiser": 1}           | 201                   | Authenticated user only             |
| /pledges/<id>/         | PUT         | Update pledge                  | {"amount": 75, "comment": "updated comment"}                                 | 200                   | Supporter only                      |
| /users/                | GET         | Get all users                  | N/A                                                                          | 200                   | Public                              |
| /users/auth/           | POST        | Create user account (signup)   | {"username": "", "password": ""}                                             | 201                   | Public                              |
| /users/<id>/           | PUT         | Update user details            | {"username": "new_name", "password": "new_pass"}                             | 200                   | Owner only                          |
| /api-token-auth/       | POST        | Get Auth Token (login)         | {"username": "", "password": ""}                                             | 200                   | Public                              |


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )