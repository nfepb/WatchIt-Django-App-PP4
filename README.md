# **WatchIt! - Project Portfolio 4**

![WatchIt Website Responsive Mockup](docs/images/watchit-website-mockup.png)

# **Introduction**

Welcome to WatchIt!,

WatchiIt is my fourth portfolio project that I have been working on in the Full Stack Developer Programme, as a student of the Code Institute. 

The purpose of this project was a build a full-stack website based around a business logic used to control a centrally-owned dataset. The main technologies used for this project are HTML, CSS, Python, and Django. Heroku Postgres is used as a relational database.

WatchIt! is a website for reviewing movies and searching for new movies to watch. Anyone that enjoys watching a movie can look up movies they think are interesting. They can read on other website's user thoughts of the said movie and how they rate it. WatchIt! also allows logged in users to add movies to their watchlist and publish reviews on movies they have watched. 

WhatchIt! is a fictional brand. This project is for educational purposes only.

You can find the live site here - <a href="https://watchit-project-portfolio-4.herokuapp.com/" target="_blank"> WatchIt! </a>
---

# **User Experience Design - UXD** 

A large part of the inspiration behind the planning for this project came from Jason James Garretts’s, “The Elements of User-Experience”.

By keeping the user in mind throughout the design and development of the project, it would be easier to make the user experience a satisfying and cohesive.

The planning of the project is broken into 5 planes,

* [The Strategy Plane](#the-strategy-pane)
* [The Scope Plane](#the-scope-plane)
* [The Structure Plane](#the-structure-plane)
* [The Skeleton Plane](#the-skeleton-plane)
* [The Surface Plane](#the-surface-plane)


[Back to top](<#watchit---project-portfolio-4>)
---

# **The Strategy Pane**

## **App Creator's Goals**

* To provide the users a website where they can view movie listings, see how other rate the movie, and read other user's review of the movie.
* To allow users to create, update and delete reviews.
* To allow users to submit new movies for other users to discover and/or review.
* To allow the admin user to approve, update and delete movie listings from the frontend.
* To provide users with clear and adequate responses based on their input or actions.

## User Stories

To help in defining the most important benefits of the app and the features required to deliver this value, I created a flowchat that goes through the different stages of the app user. It starts with the visitor (as the user), and evolves into a connected user, which is also identified as a regular user. 

[User Flowchart](./planning-docs/user-stories/images/user-flowchart.png)

### **Admin User Stories**

### **Site User Stories**

### **Logged-In User Stories**

My user stories were obtained by doing research into other apps/websites and analyzing how the user was accompanied through their journey. The [IMDb](https://www.imdb.com/) and [AlloCiné](https://www.allocine.fr/) helped me define what were some of the critical features to get to a MVP, and which features were considered 'nice to have' for later development. 


[Back to top](<#watchit---project-portfolio-4>)
---

# **The Scope Plane**

## **Agile methodology**

The principles of the Agile Methodology framed how this project was tackled. The project was initially started on another repository of GitHub - <a href="https://github.com/nfepb/WatchIt-Django-App-PP4">PP4-Django-Full-Stack</a>. However, due to server issues, I was advised by my mentor to start over for risk of not submitting the project in time. For more flexibility, the Kanban board was implemented through [Quip](https://salesforce.quip.com/). For centralisation of the assets, the Kanban Board was later re-created in this repository. <a href="https://github.com/users/nfepb/projects/4/views/1">WatchIt Kanban Board</a>

The project issues were divived into a 3 different sections:
* 📚 Backlog
* 🚧 In Progress
* ✅ Done

![Kanban board Watchit]()

Github issues were used to create the User Stories and to keep track of bugs identified during this project. Each User Story and Bug had a clear title, acceptance criteria and smaller tasks (if adequate). 

Milestones were added to keep track of the different Iterations. There were 3 separate Iterations. User Stories were completed based on the Iteration that was in progress. Not every User Story in each Iteration was delivered in time. Too many ideas, not enought time. Too much ambition for the defined deadline. This is the reason why I opted for a phased approach to help digest and define what I would work on in an initial deployment, and what would come in the later stage. After each Sprint in each Iteration, the User Stories that I could not deliver on were re-evaluated to define if they were "must-haves" in the following Iteration. 

## **User Stories**

**Phase 1**
- As a user, I can easily understand the purpose of this website on the homepage, so that I can easily understand the value proposition.
- As a user, I can easily navigate through the website, so that I can access the pages that I relevant for my usage.
- As a user, I can browse a list of movies, so that I can discover newly added movies easily.
- As a user, I can browse a list of movie genres, so that I can discover reviewed movies in a genre I am interested in.
- As a user, I can read more information about a movie in which I am interested in, so that I can judge if I am interested in this movie.
- As a user, I can read other people's review of the movie, so that I can read other people's thoughts of the movie. 
- As a user, I can write a review for a movie, so that so that I can share my opinion and rating of the movie. 
- As a user, I can create a personal account, so that so that I can review movies I have watched and save movies to my watchlist.
- As a user, I can add a movie, so that I can share my opinion on movies that are not being reviewed yet or new add movies to my watchlist.
- As a user, I can add a movie to a genre, so that the movie can be easily discovered by other users and potentially discover new movies in the same genre.
- As an admin, I can create a new movie entry, so that users can review the movie that does not yet exist on the website.
- As an admin, I can create a new genre entry, so that users can link movies to a genre and discover movies associated to this genre.
- As an admin, I can approve or decline new movie additions created by users, so that I can keep a clear database.

**Phase 2**
- As a user, I can add movies to my watchlist, so that I can keep track of the movies that I wish to watch in the future.
- As a user, I can see the list of movies I added to my watchlist, so that I can keep track of movies I find interesting.
- As a user, I can see the list of reviews I posted, so that I can keep track of my thoughts on the movies I reviewed.
- As a user, I can rate the movies I have watched, to guide other users to the movies I think are worth watching and discover good movies.
- As a user, I can search through the website, so that I easily find a specific movie I am interested in.
- As a user, I can update or delete a posted review, so that I can control my posted content.

**Phase 3**
- As an admin, I can validate or delete new movie listings to be approved through the site, so that my role is made easier.
- ~~As an admin, I can update movies already approved, so that the information on the site is correct.~~ [not delivered]
- ~~As a user, I can search for a movie from any page of the website, so that my navigation is even more easy.~~ [not delivered]
- ~~As a user, I can see which movies are the highest rated, so that I can benefit from other user input.~~ [not delivered]


[Back to top](<#watchit---project-portfolio-4>)
---

# **The Structure Plane**

5 pages are visible from the navigation bar. The genre_details page is accessible from the home page or from the book_detail page. The submit a movie form-page is only accessible when submitting a movie to the database.

The Homepage, Moviebox, Login, Signup and Contact pages can be accessed by all users. Once a user logs in or signs in they have access to the My Watchlist page. The Sign up & Login pages are removed from the navigation after the user logs in. Also, the log in page is changed to a log out page.

## **Color Palette**

![Color pallete used throughout the project](docs/images/watchit-color-palette.png)

The main colors, being #bde1e1e & #0000000 are associated with movie theaters and a famous streaming service brand. 

The color #ede7d9 is used in contrast to the 2 previous colour to help text stand out, without being too aggressive on the eyes. The color is close to the one of popcorn, which has a strong association with the entertainment industry as well.

The color #d98324 was used mainly for links and spans in order to make information stand out versus the lighter text color on the different pages.

## **Fonts**

'Poppins' is the only font family that is used throughout the website. It is a 'smooth' writing style with several font-weights, which offers a lot of diversity in the use, without having to pick another font-family for the different use through the website. It bring unity to the user experience on the different pages.

## **Images**

## **Database Design**

SQLite was used throughout the development of the WatchIt! app. During deployment to a production environment, Heroku PostgreSQL was used.

In order to support the functionalities defined in the user stories for each Epic, mapping the architecture became crucial. This helped foresee how we could get to an MVP.

### **Key Models**

[Database Diagram](docs/schema/watchit-database-diagram.png)

**User**

* The User is created based on the User model, which is created by Allauth on registration.

**Movie**

* The Movie holds information about each movie entry in the database. Each product has a unique ID.
* The Movie model is connected to the WatchlistItem model. This allows the user to add multiple movies to a single watchlist. 

**Review**

* Reviews can be posted by the users on the movies with this model
* The Review model has a one-to-many relationship to the User model to obtain the username. One user can post multiple reviews. 
* The Review model also is linked to the Movie model based on a one-to-many relationship. This allows one movie to have multiple reviews. 

**WatchListItem**

* The WatchListItem is used to allow the many-to-many relationship between the users and the movies. 
* One user can have multiple movies in their watchlist through the movie lookup in the Movie model. 
* One movie can be added to multiple users' watchlist through the user ID in the User model.


[Back to top](<#watchit---project-portfolio-4>)
---

# **The Skeleton Plane**

<details><summary>Low fidelity mobile wireframes</summary>

![Index page](docs/wireframes/wireframe-mobile-index.png)

![Navigation](docs/wireframes/wireframe-mobile-nav.png)

![Signup page](docs/wireframes/wireframe-mobile-signup.png)

![Login page](docs/wireframes/wireframe-mobile-login.png)

![Navigation](docs/wireframes/wireframe-mobile-nav.png)

![Movie Details page](docs/wireframes/wireframe-mobile-movie-details.png)

![Genre Details page](docs/wireframes/wireframe-mobile-genre-details.png)

![Moviebox page](docs/wireframes/wireframe-mobile-moviebox.png)

![My Watchlist page](docs/wireframes/wireframe-mobile-my-watchlist.png)

</details>

<details><summary>Low fidelity desktop wireframes</summary>

![Index page](docs/wireframes/wireframe-desktop-index.png)

![Navigation](docs/wireframes/wireframe-desktop-nav.png)

![Signup page](docs/wireframes/wireframe-desktop-signup.png)

![Login page](docs/wireframes/wireframe-desktop-login.png)

![Movie Details page](docs/wireframes/wireframe-desktop-movie-details.png)

![Genre Details page](docs/wireframes/wireframe-desktop-genre-details.png)

![Moviebox page](docs/wireframes/wireframe-desktop-moviebox.png)

![My Watchlist page](docs/wireframes/wireframe-desktop-my-watchlist.png)

</details>


[Back to top](<#watchit---project-portfolio-4>)
---

# **The Surface Plane**

## **Features**

### **Home Page**

<details><summary>*Navigation Bar*</summary>

[Navbar Guest User](docs/features/navbar-guest.png)

[Navbar Admin & User](docs/features/navbar-admin.png)

* The navigation through the site is mainly done through the navbar at the top of the page. The style does not change through the navigation.
* The navigation bar is responsive and will adapt rendering and display based on the screen size. 
* Based on the type of user, specific NavItems will be displayed, which are only accessible as specific user (Guest vs. User vs. Admin).
* After logging in, a user will not longer see the login / sign up options. 
* A logged in user will see the navitem for 'My Watchlist'.
* An admin will see the navitem for 'Admin Only'. 
* A logged in user will see the navitem to logout. 
</details>

<details><summary>*Hero Image*</summary>

![Hero Section Guest](docs/features/hero-section.png)

* The brand name is repeated for any user of the site to know where they are. 
* A subtitle explains the site's purpose and value proposition.
* A third title is there to inspire the users to try the site and seek new movies or genres.
* Guests will be invited to log in or to sign up through 2 separate buttons appearing, redirecting them to the respective pages.

![Hero Section User](docs/features/hero-section-user.png)
* When logged in, the user is greeted with their name on the home page. 
* The buttons for guests are not visible, but users are invited to navigated to their watchlist.
</details>

<details><summary>*Newly Added Movies*</summary>

![Newly Added Movies](docs/features/newly-added-movies.png)

* Any visitor can browse through the Owl Carousel.
* Users can see what are the 8 last added movies.
* If a movie was uploaded without an image, a placeholder image will be displayed instead, with its tiles on top of the image. 
* If not all 8 movies can be displayed at the same time time, navigation arrows appear below the carousel. 
* The carousel is responsive and image size & number of movies displayed will vary based on the screen size. 
</details>

<details><summary>*Genre Section*</summary>

![Genre Section](docs/features/genre-section.png)

* Any visitor can browse through the Owl Carousel.
* Users can go over the different genres listed on the site.
* If 8 genres cannot be displayed at the same time time, navigation arrows appear below the carousel. 
* The carousel is responsive and image size & number of movies displayed will vary based on the screen size. 
</details>

<details><summary>*Footer*</summary>

![Footer](docs/features/footer.png)

* Appears on every page and contains social links.
* To avoid losing visitors and users, links are opened in a new tab.
</details>

### **Login Page**

<details><summary>*Login Page*</summary>

![Login](docs/features/login.png)

* All the login buttons and `<a>` links redirect users to this page.
* Users can find 2 input fields to verify their identify.
* Django-Allauth is used for user authentification. 
* For guest users without an account, there is a link that will re-direct them to the signup page.
</details>

### **Signup Page**

<details><summary>*Signup Page*</summary>

![Signup](docs/features/signup.png)

* All the login buttons and `<a>` links redirect users to this page.
* Users can find 4 input fields to verify their identify, where we defined the email as optional.
* Django-Allauth is used for user authentification. 
* Requirements: unique username, number of characters in password.
* For users who already have an account, there is a link that will re-direct them to the login page.
</details>

### **Logout Page**

<details><summary>*Logout Page*</summary>

![Logout](docs/features/logout.png)

* Displays a button to confirm the user's wish to log out. 
</details>

### **Moviebox Page**

<details><summary>*Moviebox Page*</summary>

![Moviebox](docs/features/moviebox.png)

* Accessible to guests and users.
* If it is a user accessing this page, then the "Add a movie" button will appear. 
* The search function allows any user to look for the database based on the typed key words. It will look based on the movie title, the director, and the synopsis. 
* This page displays a list of movies that have the status `movie_approved = True` and are ordered by latest day of creation. 
* Users can find some information such as, the title, the director, the average rating, and the synopsis.
* Each movie card works as a link to re-direct the user to the specific movie page. 
* If a movie was uploaded without an image, a placeholder image will be displayed instead. 
* Pagination at the bottom of the list allow users to browse through the catalogue of movies if there are more than 8 movies displayed.  
</details>

### **Movie Details Page**

<details><summary>*Movie Details*</summary>

![Movie Detail](docs/features/movie-detail.png)

* Accessible to guests and users.
* Each movie detail page is unique for every movie entry, so it its URL.
* This section displays data from the DB: movie title, director, poster, synopsis.
* If a guest lands on this page, they cannot add the movie to their watchlist, instead, they are prompted to log in or sign up through links. 
* The Star Rating components also invites the guest to log in in order to rate the movie. 
* Users must be logged in order to add a movie to their watchlist. 
* User can remove movies from their watchlist by clicking on the watchlist icon. 
* Guests and users are provided with the information of how many users added this movie to their watchlist.
* When a movie is added to the watchlist, users receive visual confirmation by having the icon button changing color, and the number increase or decreasing based on their actions. 
</details>

<details><summary>*Review Section*</summary>

![Review Section](docs/features/movie-details-review-section.png)

* Readable by guests and users, they can read posted reviews.
* In order to view the text input box and to be able to post their review, a user must be logged in.
* The review button within the movie details above brings the user to this section of the page.
</details>

### **My Watchlist Page**

<details><summary>*My Watchlist Section*</summary>

![My Watchlist Section](docs/features/my-watchlist-section.png)

* Page only accessible if the user is logged in. 
* The username of the user is displayed as a subtitle to the page.
* The list of their saved movies is displayed with some information about each movie. 
* Users can find out more about any of the movies by clicking on it.
</details>

<details><summary>*MyReviews Section*</summary>

![My Reviews Section](docs/features/my-reviews-section.png)

* Users can find the list of their posted comments here.
* They can edit or delete any of their comments.
* If the user clicks on 'Delete', they are redirected to the delete review page.
* If the user clicks on 'Edit', they are re-directed to the edit review page.
</details>

### **Admin Only Page**

<details><summary>*Movie Approval Section*</summary>

![Movie Approval Section](docs/features/admin-only.png)

* This page can only be accessed if the user is a superuser.
* It allows the admin to take approval actions that would otherwise take place in the Django Admin view.
* The admin can find here the list of unapproved movies.
* They can find all the information submitted by the user.
* 2 displayed buttons allow the user to approve the new movie listing, or to delete it.
* The approve button will re-direct the admin to review and/or modify the fields prior to automatically changing the movie status to approved. The movie will then be removed from the list of the admin and be visible to all. 
* The delete button will redirect to a confirmation page prior to removing it from the list. 
</details>

### **404 Page**

<details><summary>*404 Page*</summary>

![404 Page](docs/features/admin-only.png)

* Not my proudest creation.
* This page provides feedback that the page was not found in the style of the website. 
</details>

## **Future Features**

### Watchlist

* For the moment, and due to time constraints, users cannot add movies to other user's watchlist. 

### Social Media Signup/Login

* To allow guests to easily create an account using their favourite social media and to log in easily. 

### Admin Edit/Delete actions

* To have the admin to be able to take actions on movies that have already been approved. 

### Img converter

* For better performance and quicker rendering, to have uploaded images automatically converted to the WebP format and to limit the file sizes. 

### Improved styling 

* Further improve the style throughout the website to allow an even better user experience. Better responsive page and pagination. 

### Search functionality througout the website

* To allow improved navigation, users should be able to search for movies from anywhere, not only in moviebox. 

[Back to top](<#watchit---project-portfolio-4>)
---

# **Technologies Used**

| Technology | Comment |
| :---: | :--- |
| [dbdiagram](https://dbdiagram.io/home) | Used to design the ERD for WatchIt! |
| [Grammarly](https://www.grammarly.com/) |	Used to fix the grammar errors across the project. |
| [Canva](https://www.canva.com/)	| Used to create the wireframes for the website for the different supports. |
| [Coolors](https://coolors.co/) | Used to define the color palette for the website. |
| [Github](https://github.com/) | Used as the development environment. |
| [HTML](https://html.com/) | Used for the structure in all the templates of the website. |
| [CSS](https://www.w3schools.com/css/) | Used for styling the pages throughout the website. |
| [Bootstrap 5.2.2](https://blog.getbootstrap.com/2022/10/03/bootstrap-5-2-2/) | Used for layout and styling the pages throughout the website. |
| [Pep8](https://peps.python.org/pep-0008/)	| Used to test my code for any issues or errors. |
| [Django](https://www.djangoproject.com/) | Framework used to build the project and its apps. |
| [Django Star Ratings](https://django-star-ratings.readthedocs.io/en/latest/) | Used for rating and star-rating functionalities on the movies. |
| [Python](https://www.python.org/) | Python is the core programming language used to write all of the code in this application to make it fully functional. |
| [Heroku](https://dashboard.heroku.com/login) | Used to deploy the WatchIt! application. |
| [Google Fonts](https://fonts.google.com/) | Used to add the ratings on the movies through the Djanog model. |
| [Cloudinary](https://cloudinary.com/) | Used to store all of my static files and images. |
| [JavaScript](https://www.javascript.com/) | Used in a minimalist way. It is the supporting language for some of the packages used. It allows interaction with the user inputs. |
| [jQuery](https://jquery.com/) | jQuery is required in order to use the Owl Carousel components. |
| [Owl Carousel](https://owlcarousel2.github.io/OwlCarousel2/) | Used to display the movies and genres in a carousel. |
| [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/index.html) | Used to control the rendering behavior of your Django forms. |
| [Crispy Bootstrap 5](https://github.com/django-crispy-forms/crispy-bootstrap5) | Used for Bootstrap5 for django-crispy-forms. |
| [Django Bootstrap DatePicker Plus](https://pypi.org/project/django-bootstrap-datepicker-plus/) | Used for date input in the forms. |
| [Font-Aweome](https://fontawesome.com/) | Used for the icons. |


[Back to top](<#watchit---project-portfolio-4>)
---

# **Testing**

Please have a look at <a href="TESTING.md"> TESTING.md </a>.

[Back to top](<#watchit---project-portfolio-4>)
---

# **Deployment**

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institute student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.

**Requirements**

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Django Setup

- Add your env variables to your env.py file. Add the `env.py` to the `.gitignore` to avoid disclosing any sensible information.
- Install the project requirements - `pip3 install requirements.txt`
- Apply database migrations - `python3 manage.py migrate`
- Create a superuser - `python3 manage.py createsuperuser`
- The project can be run with the following - `python3 manage.py runserver`
- Install the `dj_database_url` and `psycopg2` packages with the following commands: `pip3 install dj_database_url` & `pip3 install psycopg2`.
- Install `gunicorn` - `pip3 install gunicorn`.
- Create a `Procfile`, and add `web: gunicorn moose_juice.wsgi:application`.
- Disable Heroku from collecting static files.
- Add the hostname to project settings.py file: `ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']`.

## Initial Heroku Deployment

-   Navigate to [Heroku](https://www.heroku.com/).
-   [Log in](https://id.heroku.com/login) or [Sign Up](https://signup.heroku.com/) for an account.
-   Click on **Create new app**.
-   Enter a suitable **App Name** and **Region**.
-   Click **Create App**.
-   Under the **Deploy** tab, under the heading **Deployment Method**, click the **GitHub** icon, and proceed to click the button which states **Connect to GitHub**.
-   Enter your credentials for **GitHub.**
-   Search for the repository required, and click **Connect.**
-   Within Heroku, navigate to **Resources.**
-   Search for **Heroku Postrgres.**
-   In the Settings tab, scroll down to `Reveal Config Vars` and copy the text in the box beside DATABASE_URL.


# Credits

* [Code Institute](https://codeinstitute.net/ie/) - 'I think therefore I blog' was a strong source of inspriation throughout the project. 
* [Willem Van Onsem](https://stackoverflow.com/users/67579/willem-van-onsem) for his answer in Stackoverflow for [How to make an average from values of a foreign key in Django?](https://stackoverflow.com/questions/59479908/how-to-make-an-average-from-values-of-a-foreign-key-in-django)
* [Racool_studio](https://www.freepik.com/free-photo/delicious-popcorn_6543855.htm#query=pile%20movies&position=28&from_view=search&track=sph) for the image used in the hero image. 
* [Freepik](https://www.freepik.com/) - All images used througout the website (except movie posters)were taken from their creators.
---

# **Acknowledgements**

* My fiancée for being supportive throughout this programme.
* Ronan for his help and feedback at the planning stage of the project.
* Sean and Gemma (tutors) for helping me and reassuring me when I was panicking because I could't fix my url path or CSS. Real rockstars!


[Back to top](<#watchit---project-portfolio-4>)
------