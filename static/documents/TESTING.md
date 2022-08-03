## Manual Testing of Non-Dairy Godmother website: 

## Table of content: 
 1. [General](#General)
 1. [Home Page](#home-page)
 1. [Menus Page](#menus-page)
 1. [Newsletter](#newsletter)
 1. [Register](#register)
 1. [Login](#log-in)
 1. [Book A Table](#book-a-table)
 1. [My Bookings](#my-bookings)
 1. [Edit Bookings](#edit-bookings)
 1. [Thank You](#thank-you-page)
 1. [User Feedback](#user-feedback)


### General:
Using Google devtools I tested each page of the site to insure that it was responsive to different devices.
One the website was deployed it was also tested on different browsers, i.e Google Chrome, Microsoft Edge, Mozilla Firefox and Safari. Testing was also performed on differnt operating systems, in particular Andriod and iOS.


### Home page: 
On the homepage there wasn't alot that needed to be tested, the following checks were made: 
* By clicking on the resturant logo the home page was reloaded
* All social media links worked correctly, opening the social network on a new tab


### Menus page:
On the menus page the user has the option to view the restaurant menus or download them. The checks for the menu page are as follows:
* All the menu options, once clicked on, open up correctly and on a new tab
* All "Download menu" options are working correctly 


### Newsletter: 
During the testing of the Newsletter page it was discovered that the form could be submitted without any information on it. This needed to be addresssed before deploying of the project. 
*(Please refer to the Bugs section of the [README] (/README.md) for more information)*
Once this issue was sorted testing of the Newsletter form was able to continue. The checks were as follows:
* Click on the 'Submit' button without entering any details, this will cause an error message to appear staing "Please fill out this field". This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* Once the user has filled out all the fields in the form and clicked on the submit button they will be directed back to the home page where a message will pop up "Thank you for signing up to our newsletter"


### Register:
Like the Newsletter page, the Register page has a form for the user to fill out however, in this form not all fields are required. 
* The first test on the Register page was to check if the link to the "Log In" page at the top of the form works. Clicking on this link will bring the user straight to the Login Page. 
* Click on the 'Submit' button without entering any details, this will cause an error message to appear staing "Please fill out this field". This message will appear each time the user tries to submit the form without filling in the required fields. 
* If the user tried to create a password that is too easy or too common they will not be able to proceed and will get all or some of the following messages: 
    * This password is too short. 
    * It must contain at least 8 characters.
    * This password is too common.
    * This password is entirely numeric.
* Once the user has filled out all the required fields and created a strong enough password, they can then click the submit button. This will redirected them back to the home page where a message will pop up "Successfully signed in as 'Username"
During testing of the Register page, it was noted that when the password messages appeared the submit button was moved outside the container box, this was a quick css fix, changing the height of the box from a certain number of pixels to auto. 


### Log In:
The Log in page 

### Book A Table:

### My Bookings

### Edit Bookings:

### Thank you Page:

### User Feedback: