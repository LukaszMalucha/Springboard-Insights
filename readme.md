# Springboard Analytics


#### [Visit the App](https://springboardanalytics.herokuapp.com/)

<br>

![1](https://user-images.githubusercontent.com/26208598/71312488-7b575e00-2423-11ea-9001-304de387c566.PNG)

<br>

## App Description

Django App that allows user to:

1. Scrape and clean course data from Springboardcourses.ie.
2. Load course data to postgres db.
2. Interact with data through Vue.js fronted or directly through Django REST backend.


## App Views

#### Main Dashboard
##### `/`

Main App Navigation

<br>

![1](https://user-images.githubusercontent.com/26208598/71312488-7b575e00-2423-11ea-9001-304de387c566.PNG)

<br>

-----------------


#### User Handling
##### `/user/`

 User Handling views - resgister, login, forgot password

<br>

![2](https://user-images.githubusercontent.com/26208598/53902094-592d5480-4038-11e9-8000-704917c1da6a.jpg)

<br>

-----------------

#### Data Preprocessing
##### `/preprocessing`

 Springboard data ETL.

<br>

![2](https://user-images.githubusercontent.com/26208598/71312489-7b575e00-2423-11ea-83cb-5a7de7cab667.PNG)

<br>

-----------------

#### Springboard Statistics
##### `/course-statistics`

 Statistical data with Chart.js.

<br>

![3](https://user-images.githubusercontent.com/26208598/71312490-7b575e00-2423-11ea-8fd8-bd7712209c3a.PNG)

#### Online Degrees
##### `/online-courses`

 Latest Springboard.ie online degree offer.

<br>

![4](https://user-images.githubusercontent.com/26208598/71312491-7beff480-2423-11ea-9b0a-a64cdb9fbd7c.PNG)

<br>

-----------------

#### Fastest Diplomas
##### `/fastest-diploma`

 Shorstest diploma courses offered by Springboard.

<br>

![5](https://user-images.githubusercontent.com/26208598/71312492-7beff480-2423-11ea-90a2-cd0d6561b0ed.PNG)

<br>

-----------------

## Django REST Endpoints

#### User
##### `/api/`

 User handling via RESTFUL Api with Token Authorization.

<br>

![7](https://user-images.githubusercontent.com/26208598/53902106-5fbbcc00-4038-11e9-9ed0-848d3e11c1da.png)

<br>

-----------------

#### Courses Data
##### `/api/courses`

 Springboard.ie courses data via RESTFul Api.

<br>

![8](https://user-images.githubusercontent.com/26208598/53902109-60ecf900-4038-11e9-8eda-d26e51ea516a.jpg)

<br>

-----------------

### App Testing:

##### Travis CI: [![Build Status](https://travis-ci.com/LukaszMalucha/Springboard-Insights.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Springboard-Insights)
##### `/api/tests/`
##### `/core/tests/` 
##### `/user/tests/`

-----------------

## TOOLS, MODULES & TECHNIQUES

##### Backend Development:
Django RESTful

##### Data Analysis
pandas | numpy | sklearn | scipy

##### Frontend Development
Vue.js | Materialize | Chart.js

##### Deployment
Docker | Heroku | Travis CI | AWS S3

##### Web Scraping:
beautifulsoup4

##### Testing
django.test | coverage



<br>
<br>

##### Thank you,

Lukasz Malucha



