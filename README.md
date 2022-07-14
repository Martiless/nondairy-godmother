# Non-dairy Godmother: 

This website is designed for a fictional vegan restaurant based in Cork, Ireland. 

This website has been created as the Fourth Milestone project for Code Institute's Full Stack Software Development Diploma. It was built using a Full-Stack Toolkit. GitPod was used for writing the code for this website, as well as committing and pushing to GitHub. GitHub was then used to store the project after it had been pushed from GitPod. Once all the code had been written, Heroku was then used to deploy the website. 

![Am I Responsive]()

### View the live website [here]()
***
## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [UX](#UX)
      1. [User Stories](#User-Stories)
      1. [Development Planes](#Development-Planes)
            * [Strategy](#Strategy)
            * [Scope](#Scope)
            * [Structure](#Structure)
            * [Skeleton](#Skeleton)
            * [Surface](#Surface)
      1. [Color](#Color)
      1. [Font](#Font)
      1. [Images](#Images)
 1. [Features](#Features)
 1. [Testing](#Testing)
 1. [User Stories Met](#User-Stories-Met)
 1. [Bugs](#Bugs)
 1. [Technologies Used](#Technologies-Used)
 1. [Validation](#Validation)
 1. [Accessibility](#Accessibility)
 1. [Deployment](#Deployment)
 1. [Credits](#Credits)
 1. [Acknowledgments](#Acknowledgements)
***
  

## Site Goals:

The goals for this site are as follows:
* 

## UX:

### User stories:
#### New User:  
*  

#### Returning User:
* 

## Development Planes:
To create a website that is comprehensive and informative for a user, as a developer you need to look at all aspects of the website and how someone who visits your website will use it. You have to consider all the user stories that have been outlined in the above sections.  

## Strategy
The strategy principal looks at user needs, as well product/service objectives. This websites target audience was broken down into three categories:
### Roles: 
* New User
* Existing User  

### Demographic:
* 

### Psychographic:
#### Lifestyle:
*  
#### Values:
*  

#### The website needs to allow users to:  
*   


#### The website needs to allow the restaurant owner to:  
*   

## Scope:  

With the structure in place, it was then time to move onto the scope plane. This was all about developing website requirements based on the goals set out in the strategy plane. These requirements are broken down into two categories. 
### Content Requirements:
1. The user will be looking for:
      * 
### Functionality Requirements:
1. The user will be able to:
      * 


## Structure:

The information above was then used to create a structure for the website. Below is a site map showing how users can navigate the website intuitively 
<details>
<summary>Sitemap</summary>

![Sitemap](/static/images/site_map.png)
</details>


## Skeleton:
[Wireframes](/static/documents/wireframes/WIREFRAMES.MD) were created to set out the initial appearance of the website while also making sure to keep the end-user in mind at all times. Wireframes were created using [Balsamiq](https://balsamiq.com/).  

## Surface:
[Please see the live site here]()  


### Color: 
For this website I wanted to make it visually appealing, easy for people to read but also that it instantly came across as a 'Plant Power' website. As it is for a vegan restaurnat I wanted the look to be clean and fresh. For this I picked green as my main color, using white as the contrasting color to make everything appear modern and clean.
I wanted to make sure the color scheme was not only eye-catching but also that it passed the LightHouse Accessibility test. 

To make sure text could be seen without issue on my chosen colors I used [Coolors](https://coolors.co/) color contrast checker.

<details>
<summary>Color Checker 1</summary>

![Color Checker 1](/static/images/colour_checker1.png)
</details>

<details>
<summary>Color Checker 2</summary>

![Color Checker 2](/static/images/colour_checker2.png)
</details>



### Font:

 

### Images:

A lot of the imagery on this site was sourced from [Pexel](https://www.pexels.com/) with some real-life images too.  


***
[Back to top](#Non-dairy-Godmother)  
  

## Features:
There are several features on this site to help users get the most out of their visit to the site.  

### General:
#### Header and Navigation:  

![Header and Nav bar]()  
#### Footer:  

![Social Media Icons]()
### Home page:


## Future Features:
* 

***
[Back to top](##Non-dairy-Godmother)  

## User Stories Met:
This section is to look back at the User stories we established during the strategy phase of the project. 
We are looking to see if we have met all the goals we set out. 
#### New User:  
* 

***

## Testing:
Testing information can be viewed [here]( "Link to testing information")

***

## Bugs:
1. Styling of the base page was not consistant across all pages on the site.
      * I had not included "{% load static %}" at the beginning of my base.html page. Once this was edited, all pages loaded correctly. 
1. Font Awesome icons not appearing on site.
      * 
1. Booking page was not loading, the following error message was coming up:
      * After debugging should elements of the the booking model didn't exist, I realised that I had changed elements of the model without making any migrations.
<details>
<summary>Booking Page Error</summary>

![Booking Page Error](/static/documents/errors/booking_page_error.png)
</details>

1. Bookings appeared to be completed on the site but nothing was happening in the backend. 
      * One reason this wasn't working was because I had manually entered the booking form into the bookings.html file as apose to entering it using django's built in features.
      * Once this was fixed I then had to add the POST function to the bookings view. 

1. When trying to add specific users the booking form loaded but throw up a ProgrammingError when the user clicked on "Book Now"
      * I had to do a bit of troubleshooting to solve this one. After spending a bit of time researching and chatting with other students on Slack it was discovered that my view for the booking form was written for the older version of the booking model and had to be updated to include the user request.
      * After making these changes a user was now able to complete the booking and were redirected to the "Thank you" page.
<details>
<summary>ID Error</summary>

![ID Error](/static/documents/errors/id_error.png)
</details>

1. After correcting the above ID error it caused another ProgrammingError when I logged into the django admin page and clicked on the bookings tab.
      * After countless attempts to solve this error but debugging, troubleshooting and reaching out to various programming communities (including Slack) I had to eventually contact the CI tutors. 
      * There were serveral attempts to find the issue in the code, looking at the 'list_display' in the admin.py file, correcting errors in the models.py file neither of which solved the problem.
      * We cleared the previous migrations in order to create the admin page again but the tutor noticed that the Heroku postgres database was still connected. 
      * I reset the database from inside Heroku and performed the migrations, this corrected the issue 
<details>
<summary>Admin Page Error</summary>

![Admin Page Error](/static/documents/errors/admin_page_error.png)
</details>


***
[Back to top](#Non-dairy-Godmother) 

## Technologies Used:
For the purpose of this project, the following technologies were used.  

### Languages:
* HTML
* CSS
* Python
* Javascript
 


### Frameworks, Libraries, Programs & Applications Used:
* Django
* PostgreSQL
* Bootstrap

#### Google Font

#### Font Awesome
* Font Awesome was used on each page of the website to provide icons for UX purposes.  

#### GitPod
* GitPod was used for writing all the code for this project. It was also used to commit and push to GitHub.  

#### GitHub 
* GitHub was used to store this project.

#### Heroku
* Heroku was used to deploy the project.

#### Balsamiq 
* Balsamiq was used to draw initial Wireframes for this project.

#### Figma
* Figma was used during the structure phase of this project. It was used to create a sitemap of the website. 

#### Am I Responsive
* Am I Responsive was used to check that each page of the site was responsive. It was also used to create the mock-up image seen at the beginning of this document. 

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness before making the changes permanent.

*** 
[Back to top](#Non-dairy-Godmother)

## Validation:

See screenshot to W3C validator and Jigsaw CSS validator [here]( "Link to validation screenshots")

### **Index.html:**
No errors found. 

### **Style.css:**
No errors found

***
[Back to top](#Non-dairy-Godmother)

## Accessibility:
![LightHouse Report]()
***
## Deployment:

***
## Credits:
* Initial setup of the Django project was done following Code Institutes walkthrough project.  


## Acknowledgements:
* I would like to thank Brian O’Hare for being my mentor for this project.

*** 
[Back to top](#Non-dairy-Godmother) 