# Crowdfunding Back End
Joyce Gonzaga

## Planning:
### Concept/Name
SEEDS OF ENGLISH is more than just a fundraiser, it’s a chance to PLANT THE SEEDS OF KNOWLEDGE AND OPPORTUNITY in the lives of children from underprivileged communities in Brazil. Every donation helps a child take their first steps toward learning English, opening doors to new possibilities, brighter futures, and the power to dream bigger. Donors can see the impact of their contributions and be part of this exciting journey of growth and hope.

### Intended Audience/User Stories
Target audience: adults who want to support children’s education and social causes.
User Stories:
As a donor, I want to see the fundraiser and donate easily.
As a donor, I want to donate a custom amount to make a difference.
As an admin, I want to see the total donations collected.
As a user, I want to receive confirmation when my donation is processed.

### Front End Pages/Functionality
Home Page / Fundraiser
Displays fundraiser name, inspiring description, goal amount, and total raised.
Button to donate.

Donation Page
Form to enter donation amount.
Confirmation message after donation.
Thank you message highlighting the impact of the contribution.

Admin Dashboard (Optional)
View total donations collected.

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL              | HTTP Method | Purpose                | Request Body   | Success Response Code | Authentication/Authorisation |
| ---------------- | ----------- | ---------------------- | -------------- | --------------------- | ---------------------------- |
| /fundraiser/     | GET         | Get fundraiser details | N/A            | 200                   | Public                       |
| /donations/      | POST        | Create a donation      | {"amount": 50} | 201                   | Optional                     |
| /donations/<id>/ | GET         | View donation details  | N/A            | 200                   | Admin only                   |


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )