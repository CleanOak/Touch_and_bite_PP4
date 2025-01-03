# Touch and Bite | Blog Testing Results

[Developed By: Morgan Asare]

![mockup page](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/mockup.png)

### Live Website
[Link to the live website](https://touch-and-bite-b5dacde13c2d.herokuapp.com/)

## Table of Content
-[Validation](#testing)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
- [Appendix](#appendix)

## Validation
### Manual Testing

### W3C Validator Results
W3C validator was used to test the html files for all the templates in this project. Even though the validator produced a lot of warnings and errors were because Django relied on extensions and did not rely on tags like <head> and declaration of DOCTYPE.

#### HTML Validation
The Below errors where resolved.
Error 1
![HTML](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/html_error1.png)

Error 2
![HTML Error](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/html_error2.png)

Error 3
![HTML Error](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/html_error3.png)

Final HTML Validation
![HTML Validation Success](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/html_val.png)

#### CSS Validation
![CSS](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/css_validation.png)

#### JSHint Validator

![JSHINT](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/jshint_comment.png)

![JSHINT](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/jshint_nav.png)

### Lighthouse

#### Home Page Performance
![Home Page](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/home_perf.png)

#### Events Page Performance
![Events](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/event_perf.png)

#### About Page Performance
![About](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/about_perf.png)

#### Food Service Page Performance
![Food Performance](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/foodserv_perf.png)

#### Login Page Performance
![Login](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/login_perf.png)

#### Registration Page Performance
![Registration](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/Validations/signup_perf.png)


### Function Testing

| Category                      | Features                                        | Expected Outcome                                                                                                                                                          | Testing Performed                                                                                               | Pass/Fail                             |
| ----------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Navbar                        | Logo link                                       | The logo should direct user back to the Home page, regardless of what page they are currently on.                                                                         | Clicked on logo.                                                                                                | Pass✅                                 |
|                               | Recipes                                         | Each recipe category should show recipes only within that category.                                                                                                       | Clicked on each category.                                                                                       | Pass✅                                 |
|                               | Register                                        | Should take you to a sign up page to enter details in order to create an account.                                                                                         | Clicked link.                                                                                                   | Pass✅                                 |
|                               | Sign In and Sign out                            | Sign in form should log a user in.                                                                                                                                        | Clicked link.                                                                                                   | Pass✅                                 |
|                               | Profile                                         | Once logged in this should show a users profile with the details they filled in when registering, and also any favourite recipes they have saved.                         | Clicked and saw profile information. Added a recipe to favourites.                                              | Pass✅                                 |
|                               | Responsiveness                                  | The website is fully responsive on different screen sizes and devices.                                                                                                    | Viewed the site on a laptop and mobile phone. Used Google Chrome Developer Tools to check other responsiveness. | Pass✅                                 |
| Register / Sign In / Sign Out | Check if username / password are correct or not | If a username has already been used, or if a user inserts incorrect information, they will get an alert to notify them.                                                   | Tried registering with a username already registered, and tried signing in with the wrong password.             | Pass✅                                 |
|                               | Confirm password                                | Passwords should match when registering and be a certain length. The user will get an alert if they don't match.                                                          | Tried a short password and mismatched passwords.                                                                | Pass✅                                 |
|                               | Registering                                     | When a user registers they will get alerted it has been successful and their profile page will be available to view.                                                      | Filled in the sign up form and received an alert it was successful.                                             | Pass✅                                 |
|                               | Signing In                                      | A username and password must match a previously registered account.                                                                                                       | Tried logging in with wrong details and got an alert.                                                           | Pass✅                                 |
|                               | Signing Out                                     | Once clicked, it should confirm the user is sure they want to, or they can return to the home page and stay logged in. Will also alert that sign out has been successful. | Clicked on sign out. Both buttons of sign out and return to home page were clicked.                             | Pass✅                                 |
| Comments                      | Add a comment                                   | A users comment should appear to the logged in user only, and will only appear when approved by admin. An alert will show informing them of this.                         | Added a comment and clicked submit.                                                                             | Pass✅                                 |
|                               | Edit a comment                                  | A logged in user should be able to edit their comment, whether it's been approved or not. The comment will updated once clicked on Edit.                                  | Tried editing both an approved comment and an unapproved one.                                                   | Pass✅                                 |
|                               | Delete a comment                                | A logged in user should be able to delete their comment, whether approved or not. They will get an alert notifying if successful and the comment will be removed.         | Deleted both an approved commment and an unapproved one.                                                        | Pass✅                                 |
| Pagination                    | Next & Prev                                     | Users should be taken to the next page or the previous page.                                                                                                              | Both buttons clicked.                                                                                           | Pass✅                                 |
|                               | Back to previous page                           | Users should be taken to the page they were previously viewing.                                                                                                           | Button clicked.                                                                                                 | Pass✅                                 |
|                               | Jump to Recipe                                  | The page should scroll to the start of the recipe ingredients section of the recipe page.                                                                                 | Button clicked.                                                                                                 | Pass✅                                 |
|                               | Back to top                                     | The page should scroll to the top of the page.                                                                                                                            | Button clicked.                                                                                                 | Pass✅ NB. Not appearing on home page. |
| Footer                        | Social Media Links                              | Footer social media links should take you to the relevant page of the companies socials.                                                                                  | Clicked on icons.                                                                                               | Pass✅                                 |
|                               | Contact                                         | Contact icon should allow the user to send an email.                                                                                                                      | Clicked on icon.                                                                                                | Pass✅                                 |
## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| css not loading for production| css for production was not loading from staticfiles until I copied static files manually because collectstatic was not transferring files over |
| Performance of the website was recording low| I added lazy loading to images to optimise the performance of the webpages |
| Card links not working on home page for book a table, food menu and drinks menu | The links were not set within urls.py so just needed to be wired up to load each relevant page |
| Comment resubmits when page is reloaded| This issue keeps occurring even after several attempts|
| Error in html validator which shows p tag not closed| This issue kept occuring until removed the closing p tag. |

### Pylint

Pylint was installed on Gitpod to validate the code. All errors where resolved. However, there were some warnings regarding docstring even though it was added. this could be due to different version of the linter.

![Pylint](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/appendix.png)

### Unfixed Issue
- Same Comments are added when the page reloads
- Booking could be duplicated when page reloads

## Appendix
There is an issue with the site.webmanifest file which throws an error in the console.

![Appendix](https://github.com/CleanOak/Touch_and_bite_PP4/blob/main/docs/pylint1.png)



##### Back to [top](#table-of-contents)<hr>
