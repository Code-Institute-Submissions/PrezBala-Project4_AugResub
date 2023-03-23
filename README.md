# Astro - Project 4

<img src="https://github.com/PrezBala/Project4/blob/main/static/assets/images/astrohome.png">

This project is  based on a forum 'Astro' Community, the ultimate online destination for all space enthusiasts! Where all users can connect with fellow stargazers, aspiring astronauts, and astrophysicists alike. The websites mission is to create a thriving, supportive community where members can explore the wonders of the universe, share their knowledge, and engage in fascinating discussions about space and beyond.

Astro Community utilizes external Python modules to deliver a seamless and efficient user experience. 

To ensure a personalized experience, my platform offers user-friendly login and signup options. Once the user created their account, they'll be able to post and reply to comments, making there voice heard in the vast expanse of the Astro Community.

[Live link to the game](https://prasena-project-3-battleships.herokuapp.com/)

<hr>

# Table of contents   
- [Astro Community](#astrocommunity)
- [Table of contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  * [Site Goals](#site-goals)
  * [Agile Planning](#agile-planning)
  * [Scope](#scope)
  * [Structure](#structure)
    + [Astro Community Features](#astrocommunity-features)
    + [Home Page](#home-page)
    + [Footer](#footer)
    + [Browse Posts](#browse-posts)
    + [Search](#search)
    + [Log In, Log Out, Sign Up](#log-in--log-out--sign-ip)
    + [Create Post](#create-post)
    + [Profile Picture](#profile-picture)
    + [Engagement](#engagement)
  * [Future Features](#future-features)
- [Wireframes](#wireframes)
- [Database](#database)
- [Admin Role](#adminrole)
- [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Profile Pictures](#profilepics)
- [Technologies](#technologies)
  * [External Python Modules](#external-python-modules)
- [Testing](#testing)
  * [Functional Testing](#functional-testing)
    + [Navigation Links](#navigation-links)
    + [Footer](#footer-1)
    + [Sign Up Page](#sign-up-page)
    + [Log out Page](#log-out-page)
    + [Log in](#log-in)
    + [Create New Post](#create-new-post)
    + [Lock or Delete a post](#lock-or-delete-a-post)
    + [Comment on a post](#comment-on-a-post)
    + [Reply on a post](#reply-on-a-post)   
    + [User test](#user-test)
  * [Accessibility](#accessibility)
  * [Validator Testing](#validator-testing)
  * [PP8 Validator](#pp8-validator)
  * [Java Validator](#java-validator)
  * [Lighthouse Report](#lighthouse-report)
- [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [References](#references)
- [Acknowledgements](#acknowledgements)



# User-Experience-Design

## Site Goals

Astro Community aims to unite space enthusiasts in a thriving online platform, fostering knowledge exchange, stimulating discussions, and encouraging the exploration of the wonders of the universe. My goal is to create an engaging, supportive space where members can connect, learn, and share their passion for the cosmos.

## Agile Planning

This project was developed following agile principles, with a series of four sprints. Each feature was prioritized and labeled as either "must-have," "should-have," or "could-have." We began by implementing the must-have features, followed by the should-have features, and finally addressed the could-have features if time and resources permitted. This approach ensured the delivery of a comprehensive website, with optional enhancements added based on capacity.

Our Kanban board, created using GitHub Projects, facilitated project management and can be accessed [here](https://github.com/users/PrezBala/projects/1/views/1). For more detailed information on each task, simply click on the respective view.

![kanban](/static/assets/images/kanban.png)

The user stories were grouped into different Epics

Epic 1 - Setup

The initial step focused on establishing the foundational Django app, as it was crucial to complete this before progressing to other tasks. During this phase, the base HTML, header, and footer were created, and deployment was also addressed to prevent complications at a later stage.

Epic 1 user stories:

As a developer, I need to set up the project to lay the groundwork for incorporating core features.
As a developer, I want to create a base HTML page to maintain a consistent format across all pages.
As a user, I want seamless navigation throughout the site on my mobile and tablet devices.
As a site owner, I want to enable users to sign up for new accounts, fostering communication and interaction.
As a developer, I want to ensure smooth deployment via ElephantSQL to circumvent potential issues.

Epic 2 - Database Model and Admin

The focus of this phase was to establish the database model and admin functions, which would allow the admin to approve or reject new posts. Additionally, the admin would have the ability to lock forum posts once the topic question was adequately addressed.

Epic 2 User Stories:

As a developer, I want to create the foundation for the database, enabling users to update their posts by commenting below them.
As a non-logged-in user, I want to browse ideas from other users, but I will need to log in to post my own.

Epic 3 - Login, Signup, and Logout Pages

Epic 3 User Stories:

As a new user, I want an easy and intuitive signup process.
As a returning user, I want a straightforward login experience.
As a user, I want to safely and easily log out of the site.
Epic 4 User Stories:

As a user, I want to effortlessly share my ideas by submitting them to the site.
As a user, I want the ability to comment on and respond to other users' posts.
As a user, I want to view the post count and points allocated by the admin for any user.
As the site owner, I want to ensure only space-related topics are posted, requiring admin or delegated mod approval for each new post.

Epic 5 - Styling

Epic 5 User Stories:

As a user, I want a clear and self-explanatory front page to confirm I am in the right place.
As a developer, I want to implement a space-themed color scheme for the forum.
As a developer, I want to feature a space-related video on the main page to captivate users.
As a developer, I want to standardize the style of all forms and ensure they look good on various devices.

--

Epic 6 - Documentation

Epic 6 Tasks

- Finalize Readme documentation.
- Conduct comprehensive testing and provide a writeup.

## Scope
- Implement responsive design.
- Create a homepage featuring categories for various topics.
- Provide a search field for users to locate specific topics.
- Display user post count and a point system managed by the administrator.
- Indicate engagement levels using images under each category, representing low engagement, popular topics, closed topics, etc.
- Limit certain features for users who are not logged in.

## Structure

### Astro Community Features

Navbar

User story - As a user I want to be able to navigate easily around the site easily from any devise

Navigation Menu

When the user is not logged in the navigation bar links to the Sign In, Sign Up page and the Home Page and the '+' Button is not visible

![Navbar before login](/static/images/navbar-before-login.png)

Once the user has signed in the navigation menu changes to Log out and Home with the '+' appearing, allow the user to create a new post.

![Navbar](/static/images/navbar.png)

On smaller devices, i ensured the NavBar shows correctly with all text visible.

![Mobile Navbar](/static/images/mob-navbar.png)

### Home Page

- User Story - As a user, I want to easily view the main categories and navigate to the relevant one.

The main page features an engaging .mp4 video of the moon with clouds circulating, emphasizing the space theme of the website.

![Hero Image](/static/images/hero-image-for-readme.png)

A search function is included, allowing users to look for topics of interest. If a match is found, users will be directed to the search results page.

![Welcome Text](/static/images/welcome-text.png)

Once logged in, users can click the '+' symbol to create a new post by entering a title, content, and selecting a category. Tags can also be added to improve search accuracy.

![Welcome Text](/static/images/welcome-text.png)

Forum stats are displayed, showcasing the total post count, details of the latest post, and the user who created it.

![Welcome Text](/static/images/welcome-text.png)

### Footer

- User Story: As site owner, I want to share my name within the footer.

The Footer has been added to the bottom of the site.

![Footer](/static/images/kidsbored-footer.png)

### Browse Posts

- User Story: As a user who is not logged in, I want to have the ability to explore forum posts created by other users.

Even without logging in, anyone can access the website to browse posts, navigate between categories, and read through all posts, comments, and replies

![Brows Ideas Page](/static/images/browse-ideas.png)

### Search

- User Story: As a user, I want to search for topics of interest to discover if other users have shared similar thoughts or comments.

Upon entering their search query, users will be directed to a search results page displaying relevant content, or a message indicating no results were found.

![Detail Page](/static/images/detail-page.png)

-----------
### Log In Log Out Sign Up

User Stories
- As a new user, I want a straightforward and intuitive signup process.
- As a returning user, I want an effortless login experience.
- As a user, I want to safely and easily log out of the site.
- As a developer, I want to standardize the style of all forms and ensure they look good on various devices.

Users can seamlessly sign in and out using consistently styled forms and confirmation pages.

User Stories:

![Log In Page](/static/images/sign-in-page.png)

![Log Out Page](/static/images/sign-up.png)

![Sign Up Page](/static/images/sign-out.png)

As evident, all login and logout pages share a consistent design, featuring white text on a black background for optimal visibility and readability.

### Create Post

- User Story: As a user, I want to effortlessly share my questions or theories on the site so that I can exchange ideas with others.

Upon logging in, users can create their own posts using forms designed with Crispy Forms.

The image below showcases the mobile view, illustrating how the forms adapt to a smaller screen, ensuring a user-friendly experience on mobile devices.

![Create idea form](/static/images/create-idea-form.png)

### Profile Picture

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

![Create idea form](/static/images/create-idea-form.png)

### Engagement

User Stories
- As a user, I want to see the level of engagement for each post, which is represented by clearly labeled images within each category page.

![Edit Idea](/static/images/edit-idea.png)

When a user creates a new post and it is approved by the site admin, the engagement will be displayed as '0 Engagement Topic.'

![Delete Idea](/static/images/delete-idea.png)

As users comment or reply within that post, the engagement indicator will be updated accordingly.

![edit and delete](/static/images/edit-and-delete.png)

## Future Features

- Implement like and dislike buttons to foster user engagement.

- Incorporate additional animations on the homepage for enhanced aesthetics.

# Wireframes

Home Page

![Home page wireframe](/static/images/home-page-wireframe.png)

Sign Up

![Sign up wireframe](/static/images/sign-up-wireframe.png)

Log In

![Log in wireframe](/static/images/log-in-wireframe.png)

Log out

![log out wireframe](/static/images/log-out-wireframe.png)

Browse Ideas

![Browse Ideas wireframe](/static/images/browse-ideas-wireframe.png)

Idea Detail

![Idea Detail wireframe](/static/images/idea-detail-wireframe.png)

Create/Edit Idea Form

![Create/Edit Idea wireframe](/static/images/create-idea-wireframe.png)

Delete Idea Conirmation

![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

# Database

The system was designed to provide the administrator with CRUD functionality upon signing in. The administrator or a moderator assigned by the administrator can authorize posts, remove posts, delete users, lock posts, and perform other related tasks.

![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

# Security

Views were safeguarded using Django's view mixin, UserPassesTestMixin. A test function was implemented to employ the mixin and ensure that the user has the necessary authorization to access the page. Moreover, an else statement is used in detail.html to restrict unauthorized users from commenting or replying to posts unless approved by the administrator or moderators.

![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

Environment variables were stored in an env.py file for security purposes to ensure no secret keys, api keys or sensitive information were added to the repository.  These variables were added to ElephantSQL config vars within the project

# Design

## Colour Scheme

To maintain the space theme of the website, I searched for a suitable color palette using Colorswall, ensuring a cohesive and visually appealing design.

LINK TO https://colorswall.com/

## Imagery  

The hero video featured on the website is an .mp4 file depicting the moon with clouds swirling around it. This captivating visual was found through a Google image search using video filters.

# Technologies

- HTML
  - The site's structure was created using HTML.
- CSS
  - An external stylesheet was utilized to style the website with CSS.
- Python 
  - The Django app was primarily developed using Python.
- Github
  - The source code was hosted on Github.
- Git
  - Git was employed to write, commit, and push code during development.
- Font Awesome
  - Various Font Awesome icons were incorporated throughout the site.
- Balsamiq
  - Balsamiq wireframes were used for planning purposes.
- javascript
  - A minimal amount of JavaScript was implemented to make toast messages disappear.

## External Python Modules

- Django==3.2.16 - Framework used to build the application
- django-crispy-forms==1.14.0 - used to style forms 
- Pillow==9.4.0 - Installed to upload images.
- asgiref==3.6.0 - Installed to provide various ASGI-related utilities,
- sqlparse==0.4.3 - Used for parsing, splitting, and formatting SQL statements
- register==0.1 - Related to user registration within the Django app
- django-etc==1.4.0 - Contains various utilities and extensions for Django projects, aiming to improve productivity and code quality. 
- django-hitcount==1.3.5 - This Django app allows me to track the number of hits/views for chosen objects within my project.
- django-resized==1.0.2 - This package provides a simple Django field for handling resizing of images upon upload. It helps maintain a consistent size for all uploaded images
- django-taggit==3.1.0 -Installed this Django app to simplify the addition of tagging my application, allowing me to associate tags with any model instances
- django-tinymce==3.5.0 - This package integrates the TinyMCE rich text editor with the Django framework, allowing to create and edit rich-text content easily
- pytz==2022.7.1 - This library provides world timezone definitions, allowing me to work with timezone-aware datetime objects in Python

# Testing

## Functional Testing

### Navigation Links

Testing was performed on on all navigation links throughout the site.  I achieved this by clicking on each link to ensure it went to the correct place.

Navbar 'Burger' Menu => Expands Navbar to signin.html, signup.html and index.html
Home page => index.html
Browse Ideas => ideas.html
Idea Title => ideas_detail.html
Delete Button => idea_delete.html
Edit Button => idea_edit_form.html
Edit Button Submit Button => ideas.html
Activity Website => chosen website(opens in new tab)
Register => signup.html
Sign In => signin.html

In the base.html file, there is a reference to code that checks whether the user is authenticated. If the user is authenticated, they are granted the ability to log in, log out, and sign up.

![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

### Sign Up Page

Testing was taken out to ensure a user could sign up to the website.
Steps:
- Navigate to [AstroCommunity](https://)
- Navigate to the Sign Up page.
- Enter User Name and Password
- Enter Full name, Bio and upload profile picture
- Click Update

Expected outcome: The user is redirected to the home page, and the navbar displays the log out and home options along with the '+' symbol.
Actual outcome: The user is indeed redirected to the home page, and the navbar updates to show the log out and home options as well as the '+' symbol.

### Log out Page

Testing was taken out to ensure a user could log out of the website.
Steps:
- Navigate to Log Out page
- Click Confirm button

Expected outcome: Upon completing the action, the user is redirected to the homepage, and the navbar should only display options for signing in, signing up, and returning home. The '+' icon should not be present.

Actual outcome: The expected outcome was met, and the user was redirected to the homepage with the navbar displaying only options for signing in, signing up, and returning home. The '+' icon was not present.

### Log in

Testing was taken out to ensure a user could log in to the website.
Steps:
- Navigate to [AstroCommunity](https://k)
- Navigate to Sign In page
- Enter User Name and Password
- Click Sign in

Expected outcome: Upon completing the action, the user is redirected to the homepage, and the navbar should only display options for logging out and returning home. The '+' icon should be present.

Actual outcome: The expected outcome was met, and the user was redirected to the homepage with the navbar displaying only options for logging out and returning home. The '+' icon was present.

### Create New Post

Testing was taken out to ensure the user could create a new idea.

Assuming user is already logged in
Steps:
- Navigate to the home page
- Click the '+' symbol
- Complete form
  - Title
  - Content
  - Categories
  - Tags
- Click Save

  Expected outcome: If all fields are filled in correctly, the user will be redirected to the home page. The new post will appear for the administrator or forum moderator to review, and they can decide whether or not to authorize it to appear publicly. This function serves to prevent spamming and ensure that all content is reviewed by the administrator or moderators before it is made public on the forum.

  ![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

### Lock / Delete a post

The administrator is able to lock or delete any post within the admin page.

Assuming the administrator is logged in
Steps:
- Navigate to the admin page
- Under Main > Posts
- The administrator can select to either delete (button) or close a post (checkbox).
- Click the delete button
- User is taken to a summary screen of what will be deleted and if the user wishes to continue
- Click 'Yes i'm sure'.

  ![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

Expected outcome:  The user will be redirected back to admin main page.

The outcome was as expected.

### Comment on a post

First I checked the comment section when the user is Logged out.

As expected there is no option to enter a comment at all but a message stating the user must login to post with a link attached in the text.  

If the user is logged in:

Steps

- Navigate to a post within any of the categories
- Click on comment and select submit
- User comment will appear below

  ![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

Expected outcome: The comment will appear below the original post.

The outcome was as expected.

### Reply on a post

If the user is logged in:

Steps

- Navigate to a post within any of the categories
- Click on reply to an existing post with comments and select submit
- User response will appear below
- User response text box will appear shifted to the right to differentiate from standard comment messages.

Expected outcome: The response will appear below the users comment, but will be shifted to the right.

The outcome was as expected.

### User test

I requested my wife's assistance in testing the functionality of the website. She was asked to sign up for an account and create a new post. Additionally, she tested the search functionality and the engagement viewer to ensure that they updated correctly.

## Accessibility

I utilized the [Wave Accessibility](https://wave.webaim.org/) tool for assistance with accessibility testing. All pages displayed zero errors.

However, there are Alerts related to underlined text and a contrast issue. Despite these alerts, multiple user testing sessions have confirmed the clarity of the content.

## Validator Testing

All pages were tested using the [w3 HTML validator](https://validator.w3.org/). At first, there were a few errors, such as missing closing tags and a <p> tag incorrectly placed within a <span>.

All identified issues were resolved, and the pages passed the validator without any errors.

Since Django's template language was used in the HTML files, the HTML code had to be obtained from the live web page by right-clicking and selecting "View Source." This code was then copied and pasted into the validator for testing.

![w3 HTML Validator](/static/images/html-check.png)

## PP8 Validator

All pages were tested using the [PEP8 Validator  ](http://pep8online.com/). Some errors were identified, such as lines being too long and unnecessary whitespace. All issues were addressed, and all pages, except for the settings.py page, have passed the validation. The settings.py file contains code not authored by me, so no changes were made to it.

![PEP8 Validator](/static/images/pep8.png)

## Java Validator

All pages were tested using the [Jshint Validator  ](https://jshint.com/). No errors appeared.

![PEP8 Validator](/static/images/pep8.png)


## Lighthouse Report

Initially, the Lighthouse report indicated a low score for best practices. To improve the score, I added accessible names to specific buttons and made sure links were crawlable. After implementing these changes, the score increased to 100, resulting in high ratings across all four criteria.

![Lighthouse](/static/images/lighthouse.png)

# Responsiveness

I evaluated the website's responsiveness on all devices with widths of 320px and above. The testing was conducted on Chrome, Edge, Firefox, and Safari browsers.

To accomplish this, I utilized developer tools and resized the website down to 320px.

As anticipated, there were no issues with responsiveness.

# Bugs

- I initially had a bug in the URLs that was confusing the browse ideas page with the idea detail page and causing an error.  I solved this by adding post/ to the front of the url.
>path('post/<slug:pk>/<str:activity_name>/', views.IdeaDetail.as_view(

- I had a bug that stopped the images being uploaded from the front end.  They could be uploaded from admin.
After a lot of investigation, I finally worked out that I needed to add the encoding type to the form for it to recognise the image.
>enctype="multipart/form-data"

- There was a bug that stopped the nav bar working when it collapsed down to a button on smaller screens.  The issue was the bootstap link was slightly wrong.  Once corrected the bug was solved.

- I had arranged the image size to all be the same size so that the cards are a uniform height.  I had ‘cover’ on this but this option was cutting the top of the picture off.  To solve this I have changed the css to ‘contain’.  This does not entirely fix the problem because it would be nice to have the pictuers all the same size. In a future development, I would like to add a function for the user to be able to pick the area of the picture they want to upload.

# Deployment

To deploy my site to Heroku I followed the following steps

- Navigate to heroku and create/log into account
- Click the new button in the top right corner
- Select create new app
- Enter app name (kids-bored)
- Select region and click create app (europe)
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click Deploy

The app should now be deployed

# References
- I referenced other people's projects to gather ideas for kanbans and determine which code snippets to search for on Google.
- https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak
- I also followed the Code Institute Blog walkthrough to kickstart my project.
- Youtube - This platform has been incredibly useful and after watching countless videos i've learnt several different ways to code certain things i wouldnt have thought of    
  before, i watched a vast number of channels and listed a few below.
- freeCodeCamp.org - Create a Twitter-like App
- AIOC all in one code - Reddit Clone
- Shadee Merhi - Reddit Clone REACTJS
- I consulted the Django documentation.
- I referred to the Summernote documentation.

# Acknowledgements

I want to thank:

My Mentor Andre Aquilina who has provided me several tips/advise which has helped me in figuring out bugs i encountered during testing phases.
my sister and my wife for testing my site for me.
The slack community


