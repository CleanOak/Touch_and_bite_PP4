# Touch and Bite Catering Services | Blog

(Developer: Morgan Asare)

[Link to the website](https://touch-and-bite-b5dacde13c2d.herokuapp.com/)

![An image previewing all devices](docs/mockup.png)

## Table of Content

1. [Project Goals](#project-goals)
    1. [About](#about)
    2. [User Goals](#user-goals)
    3. [Site Owner Goals](#site-owner-goals)
    4. [User Stories](#user-stories)
       -[Admin User Stories](#admin-user-stories)
    6. [Design](#design)
      - [Colour Scheme](#colours)
      - [Fonts](#fonts)
      - [Structure](#structure)
        - [Website pages](#website-pages)
        - [Database](#database)
      - [Wireframes](#wireframes)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requrements-and-expectations)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#testing)
7. [Heroku Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

### Touch and Bite catering services is a fictional business set up to complete PP4. In this project, a user can book services from the company by creating an account and reserving a date with food details and the number of guests.
<hr>

### User Goals

- To create a user account
- To pre-book a catering service
- To view menu, a blog, and contact information

### Site Owner Goals

- To create a web application to allow users to book catering service
- To make the web application appealing to attract business
- Implement modern technologies to enhance user experience
- Implement a fully responsive web application

### User Stories

1. As a User I can navigate across the site to move to each feature of the site easily. (Must have)
2. As a User I can use a navbar, footer, and social icons to navigate the site, access menus, and access socials. (Must have)
3. As a Site Owner I can provide a Contact Us page so that users can get in touch with my business (Must have)
4. As a User I can view the opening hours and contact details so that I know when the business is open and how to contact them via email, phone and socials (Must have)
5. As a User I can create a booking by selecting a date and time. (Must have)
6. As a User I can update my booking so that I can choose another available time and date slot. (Must have)
7. As a User I can delete my booking so that I can cancel the reservation (Must have)
8. As a user I can view my booking so that I can remind myself of the date and time I have booked (Must have)
9. As a User I can be notified so that I know my action of creation, edit, or deletion of a booking has been successful (Must have)
10. As a User I can register as prompted so that I can make a booking if I wish to reserve a table. (Must have)
11. As a User I can register to create an account so that my details are stored for faster booking in the future (Must have)
12. As a user I can log in so that I can book a table (Must have)
13. As a user I can see my login status so that I know if I am logged in or not (Must have)
14. As a User I can view the site's blog so that I can learn additional information and read articles (Should have)
15. As a User I can view the food menu so that I can decide whether to eat at the business. (Must have)
16. As a User I can not book a date in the past so that my booking is valid (Must have)
17. As a User, I can view blog posts page by page so that I can browse without seeing an overloaded page (Should have)
18. As a User I can not book a table already booked so that my booking is valid and not double booked (Must have)

### Admin User Stories

1.	As an Admin / Authorised User I can log in so that I can access the back end of the site (Must have)
2. As an Admin / Authorised User I can toggle booking confirmation to auto or manual mode so that on busy days manual mode can be used to reduce double bookings. (Must have)
3.	As an Admin / Authorised User I can manually add a booking so that I can book a table if someone phones, or emails the business (Should have)
4. As an Admin / Authorised User I can accept or reject bookings so that we avoid double bookings (Must have)
5. As an Admin I can log in to add or remove items from the food and cocktail menu so that we can add more food and drinks or remove them. (Must have)
6.	As an Admin I can create, read, update, and delete food and drinks items from the database so that we can add, remove, rename, and view all our food and drinks items (Must have)
7. As an Admin / Authorised User I can search through bookings and menus so that I can find the information I am looking for	 (Should have)
8. As an Admin / Authorised User I can filter bookings by date so that I can see what bookings we have for a particular day (Should have)

### Site Owner 

1. As a Site Owner I can provide a fully responsive site for my customers so that they have a good user experience. (Must have)
2. As a Site Owner I can validate data entered into my site so that all submitted data is correct to avoid errors (Must have)

### Kanban, Epics & User Stories

- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban


### Epics
![Epic](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/epic.png)

### User Stories
![User Stories](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/user_stories.png)

### Kanban
![Kanban](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/kanban.png)  

## Design

### Colour Scheme
![Colour Scheme](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/colours.png)

### Fonts 
The fonts selected for this project were from Google Fonts; Poppins, Inter and sans-serif as a backup font.

### Structure

#### Website pages
The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

- The site consists of the following pages:
  - Homepage with courosel and booking button for the user to book for a preferred service.
  - Food menu has the current list of all available foods from the database sorted by starters, mains and desserts
  - Drinks menu has the current list of all available drinks from the databse sorted by type
  - Blog page has a paginated list of blogs posted by an admin or authorised user, 4 per page
  - Blog expanded displays a blog the user has selected so they can read the blog, if they are logged in they can also leave a comment which will then need to be approved before it is displayed
  - Book page allows registered users to book a service , guest count, date requested, time requested and table location
  - My bookings displays all bookings for the user that they have made, bookings in the past are automatically expired
  - Edit booking allows the user to change their date, time, table and guest count
  - Cancel booking allows the user to cancel the booking which will then delete it from the database
  - Contact us allows the user to send us a DM if the are registered, or they can contact us from the displayed email and phone number or visit the address listed.
  - Once registered, users can comment on a blog they have read. they can also edit and delete a previous comment.
  - Login / Logout allows users to login to make bookings, view, edit, and delete bookings
  - Register allows the user to regiser so they can use the booking system
  - 404 error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a database of Postgresql for the deployed Heroku version(production)
- Two database model shows all the fields stored in the database

![Database Model](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/data_models.png)

##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- is_active
- date_joined

##### FoodItem Model
The FoodItem Model contains the following:
- food_id
- food_name
- description
- price
- food_image
- available

##### Booking Model
The Booking Model contains the following:
- booking_id (PrimaryKey)
- service (ForeignKey)
- user (ForeignKey)
- phone
- status
- requested_date
- requested_time
- number_of_people

#### Event Model
The event model contains the following
event_type
event_image
content

##### Post Model
The Post Model contains the following:
- title
- post_id (PrimaryKey)
- author (ForeignKey)
- created_date
- updated_date
- content
- featured_image
- excerpt
- slug
- status

##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- name
- email
- body
- created_date
- approved
- Meta: created_on

##### ContactUs Model
The ContactUs Model contains the following:
- contact_id (PrimaryKey)
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- body

### Wireframes
The wireframes were created using Miro
![Wire Frame](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/wireframe1.png)
![Wire Frame](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/wireframe2.png)

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Miro](https://miro.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

##### Back to [top](#table-of-contents)

## Features

### Home page
- Home page includes nav bar, main body and a footer
![Home Page](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/home.png)

### Logo & Navigation
- Custom logo for the business
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- displayed on all pages

#### Loggin Navbar
![Logo and Navbar](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/logo_nav.png)

#### Logged Out NavBar
![Navbar when logged out](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/nav_logout.png)

### Footer
- Contains social media links and copyright
- displayed across all pages

![Footer](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/footer.png)

### Sign up / Register
- Allow users to register an account
- Username and password are required, email is optional

![Sign Up](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/signup.png)

### Login
- User can login to create a booking, view bookings, edit and delete bookings and comment on blogs

![Login](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/login.png)

### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

![Logout](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/signout.png)

### Book
- Allows the user to book a table using the booking form
- Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format

![Booking](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/booking.png)


### My Bookings
- Allows the user to see all their bookings
- If the booking is older than today it is automatically expired for the user
- Status of the booking is displayed, awaiting confirmation and when approved will then change to confirmed status for the user

![My Booking](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/my_booking.png)

### Edit Booking
- Allows the user to edit their booking to another date, time, guest count and table

![Edit Booking](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/edit_booking.png)

### Cancel Booking 
- Allows the user to cancel their booking, asks user if they are sure to confirm cancellation

![Cancel Booking](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/cancel_booking.png)

### Events
- Shows the user the category of events we cater and is available

![Food Services](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/events_page.png)


### Food Services
- The food menu displays all available foods on the menu
- Menu is seperated by starters, mains and desserts
- Items can be added via the admin panel in the backend by staff
- Staff can create, update and delete foods via the admin panel

![Food Services](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/food_services.png)


### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page

![Blog](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/blog.png)

### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- Only registered users can comment on the blog

![Blog Expanded](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/blog_expanded.png)


### Comments
- Comments made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend

![Comments](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/comment_section.png)

### Contact Information
- Registered users can DM staff via the message box
- Contact info such as, phone, email, and address is displayed
- A Google Map is embedded with the address for users to use

![Contact Info](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/contact_info.png)


### Pagination
- Pagination is used on the bookings list and the blog page
- Ensures the page is kept tidy as only 4 items are displayed per page

#### Pagination Next Page
![Pagination](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/pagination1.png)

#### Pagination Previous Page
![Pagination](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/features/pagination2.png)

### Testing

Test results of this project can be found in the [TESTING.MD file](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/TESTING.md)

### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region

3. Under resources search for postgres, and add a Postgres database to the app

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py

6. Ensure debug is set to false in the settings.py file

7. Add localhost, and and the deployed URL to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a touch_and_bite_PP4

15. Ensure the following environment variables are set in Heroku Config Vars
 - Cloudinary URL
 - DATABASE_URL
 - PORT
 - SECRETE_KEY
 - DISABLE_COLLECTSTATIC

16. Connect the app to GitHub, and enable automatic deploys from main if you wish

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>


## Credits

- Some of the code was borrowed from [I Think Therefore I Blog]
- Code reference to [Arron Beale](https://ci-pp4-the-diplomat.herokuapp.com/)
- Code  reference to [EastStr](https://east-street-bc0671035c95.herokuapp.com/)
- Also, regex for validating passwords was borrowed from [Tutorialspoint](https://www.tutorialspoint.com/password-validation-in-python)
- Stackoverflow
- ChatGPT

### Content
- Some of the contents were generated from ChatGPT
- [W3 Schools](https://validator.w3.org/nu/)
- [Stack Overflow](https://validator.w3.org/nu/)



## Acknowledgements

### Special thanks to the following:
- Code Institute
- My Mentor Mo Shami
- My Wife
- My friend Gabriel who helped me on the journey
