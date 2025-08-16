# Crowdfunding Back End
Joyce Gonzaga

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- Home page
    - Featured fundraiser
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL              | HTTP Method                            | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| ---------------- | -------------------------------------- | ------- | ------------ | --------------------- | ---------------------------- |
| /fundaraisers/   | Fetch all the fundraiser               | GET     | N/A          | 200                   | None                         |
| /fundaraisers/   | Create a new fundraiser                | POST    | JSON Payload | 201                   | Any logged in user           |
| /fundaraisers/1/ |                                        |         |              |                       |                              |
| /pledges/        | Fetch all the pledges                  | GET     | N/A          | 200                   | None                         |
| /pledges/        | Fetch all the pledges for a fundraiser | POST    | JSON payload | 201                   | Any logged in user           |

### DB Schema
![](./database.drawio.svg)