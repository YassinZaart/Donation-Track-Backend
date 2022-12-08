# About

Donation Track is there to make all of the donations of organizations or individuals visible to everyone. Organizations and trusted users will be able to lookup their own donations and lookup the donation history of every person who is in need for help.
Based on the donee’s history of donations received, the trusted users will decidehow to proceed with the donation and then store the donation. The trusted users will also be able to post about people who are in need and provide all of the information needed of their status so other people/organizations can help them. Which will help shed the light on the people who are in desperate need of help.

# Competition

After scoping out the market looking for platforms that have the same idea or at least a similar idea to mine, I couldn’t find any. There are no apps that globalize donations and posts about people who are in need in Lebanon. There must be private software for storing donations for bigger organizations.However, others won't benefit from it like they do with the app.The app is also free and simple to use which will make it spread through smaller organizations and individuals.

# Features

This app allows guests and unverified users to:

- Search and View public donations by entering the person's id
- View posts about people who are in need

Verified users can do the above in addition to:
 
 - Create a new post
 - Create a new donation
 - View their own donations and posts
 - Edit/Delete their own donations and posts
 - Add their contribution to a post 

Admins can:

- Edit/Delete any donations or posts
- Check incoming verification requests
- Accept/Decline verification requests

# Components

- ## Apis

  The implementation of the REST APIs was done using Flask. I used it to create the APIs and configure their routes

- ## Database Management

  Database management deals with the database connection and queries. It was implemented using SQLAlchemy. 


- ## Schemas
    
    Schemas are used to validate arguments coming for the requests.They ensure that the arguments received and their types are valid. For this module we used Marshmellow schemas. 

- ## Resource Fields
    Resource fields are used to declare the models of the data to be sent by the APIs.

- ## JWT authentication

    These tokens are generated every time the user logs in and are returned when the login is successful. The device stores the token locally and sends it along every http request for authorization.  

## Hosting 

The server is hosted 24/7 on heroku : https://donation-track-backend.herokuapp.com/

