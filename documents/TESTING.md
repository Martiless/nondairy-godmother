## Testing of Non-Dairy Godmother website: 

## Table of content: 
 1. [Manual Testing](#manual-test)
    1. [General](#General)
    1. [Navbar and Footer Links](#navbar-and-footer-links)
    1. [Menus Page](#menus-page)
    1. [Newsletter](#newsletter)
    1. [Register](#register)
    1. [Login](#log-in)
    1. [Book A Table](#book-a-table)
    1. [My Bookings](#my-bookings)
    1. [Edit Bookings](#edit-bookings)
    1. [Thank You](#thank-you-page)
 1. [Automated Testing](#automated-test)
 1. [User Feedback](#user-feedback)
    1. [Home Page Image](#home-page-image)
    1. [Spacing](#spacing-on-the-pages)
    1. [Message Time Out](#time-out-of-message)


## Manual Test:

### General:
Using Google devtools I tested each page of the site to insure that it was responsive to different devices.
One the website was deployed it was also tested on different browsers, i.e Google Chrome, Microsoft Edge, Mozilla Firefox and Safari. Testing was also performed on differnt operating systems, in particular Andriod and iOS.

### Navbar and Footer Links: 
On each page there is a navigation bar and a footer that needs to be tested, the following checks were made: 
* By clicking on the resturant logo the home page was reloaded
* By clicking on each of the tabs in the navbar you are redirected to the right page
* All social media links worked correctly, opening the social network on a new tab

***

### Menus page:
On the menus page the user has the option to view the restaurant menus or download them. The checks for the menu page are as follows:
* All the menu options, once clicked on, open up correctly and on a new tab
* All "Download menu" options are working correctly 


### Newsletter: 
During the testing of the Newsletter page it was discovered that the form could be submitted without any information on it. This needed to be addresssed before deploying of the project.

*(Please refer to the Bugs section of the [README](/README.md) for more information)*

Once this issue was sorted testing of the Newsletter form was able to continue. The checks were as follows:
* Click on the 'Submit' button without entering any details, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* Once the user has filled out all the fields in the form and clicked on the submit button they will be directed back to the home page where a message will pop up "Thank you for signing up to our newsletter"


### Register:
Like the Newsletter page, the Register page has a form for the user to fill out however, in this form not all fields are required. 
* The first test on the Register page was to check if the link to the "Log In" page at the top of the form works. Clicking on this link will bring the user straight to the Login Page. 
* Click on the 'Submit' button without entering any details, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling in the required fields. 
* If the user tried to create a password that is too easy or too common they will not be able to proceed and will get all or some of the following messages: 
    * This password is too short. 
    * It must contain at least 8 characters.
    * This password is too common.
    * This password is entirely numeric.
* Once the user has filled out all the required fields and created a strong enough password, they can then click the submit button. This will redirected them back to the home page where a message will pop up "Successfully signed in as 'Username"
During testing of the Register page, it was noted that when the password messages appeared the submit button was moved outside the container box, this was a quick css fix, changing the height of the box from a certain number of pixels to auto. 


### Log In:
The Log in page is a simple test, there was just two elements on the page that needs to be tested. These checks are as follows:
* Try clicking on the 'Submit' button without entering any details in the log in form, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* If the user attempts to log in with an incorrect username or password they will get the following message ***"The username and/or password you specified are not correct."***
* Once the user has enter the correct username and password they now have the option to tick the 'remember me' box which will keep them logged in on their browser. 
* Clicking on the 'Log In' button redirects the user back to the home page.


### Book A Table:
When a user moves to the Book A Table page they will be met with a form with 8 elements on it
1. Booking Name
1. Email Address
1. Contact Number
1. Number of People
1. Date
1. Time
1. Table
1. Occasion 

These elements need to be filled out before the user can make a booking, the checks for this page are as follows:
* Try clicking on the 'Submit' button without entering any details in the log in form, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* Selecting a date is done using the calender widget. Click on the calendar icon on the right and select a date.
* Number of People, Time, Table and Occasion are all selected using the dropdown menu, this is done but clicking on the arrow and choosing the option that best suits the booking. If the user attempts to make a booking without making one of these choices they will recieved the following message ***"Please select an item in the list"***


### My Bookings:
The My Bookings page is a page where all the bookings from the user will appear in the order of most recent bookings. From there the user has the option to Edit a booking or to cancel a booking.   
*Checks for Edit bookings can be found [here](#edit-bookings)*   
The checks for My Bookings are as follows:
* When a user clicks on the 'edit' button they are redirected to the Edit Bookings page, where they can make adjustments to their booking.
* When a user clicks on the 'cancel' button they are redirected to the Home page, where they get a message pop up stating ***"Your booking has been cancelled"***


### Edit Bookings:
The Edit Bookings page gives the user the opportunity to make changes to any aspects of their bookings. To test this page the following checks were made.
* If a user removes any of the forms fields without giving it a new value they will not be able to submit the changes. They will receive a message that tells them either ***"Please fill out this field"*** or  ***"Please select an item in the list"***. Once all fields of the form have been filled out the user can them submit the form.
* Once the changes have been submitted the user will be redirected to the home page where they will receive a message stating ***"Your booking has been updated"***


### Thank you Page:
The user is redirected to a Thank you for Booking page once they have successfully made a booking. This is just a simple page with some text and two links.   
Checks for this page: 
* When a user clicks on the link to view, change or cancel their booking they are redirected to the 'My Bookings' page
* When a user clicks on the link to view the menus they are redirected to the 'Menus' page

***

## Automated Test:
Automated testing was done on the views.py file. This file was pick as it allowed testing of the views but also the CRUD functionality of the site.   
To view the automated testing please go to [testing_views.py](/bookingsystem/test_views.py)
For testing the view I created 10 automated tests. One to test each view and then to test the CRUD functionality. Each test passed when I ran the command in the terminal   
![Testing](/static/images/testing_validation.png)

***

## User Feedback:  
### Home page image:
Original image on the home page did not give users the impression that they had landed on a restaurants website but more a cooking blog. After this feedback the homepage image was changed to make the site look like a restaurant website from the minute you land on it.  

<details>
<summary>Here is the original Home page image</summary>

![Original Home Page Image](/static/images/bowl_of_fruit.jpg)
</details><br>


### Spacing on the pages:
There was originally a white gap between the navigation bar and the main image on each page. After receiving user feedback that this looked like it wasn't meant to be there, it was removed from each page. The navigation bar and the main image now sit perfectly next to each other on each page. The white space still appears but only when a message is popping up.

### Time out of message:
When a user does just about anything on the site a message will appear to confirm their action. The time out on this was origianlly 2.5seconds. After receiving user feedback it was noted that these messages dissapear too quickly and were hard to read. The time out was increased to 4seconds to combat this. 

[Back to Top of Testing](#manual-testing-of-non-dairy-godmother-website)     
[Back to README](/README.md)