# Overview

This is a template for a sample point-of-sale (POS) system project with SQL. With the prevalence of CRUD operations, a POS system is a perfect project to get more comfortable when dealing with SQL.

In this project, Interview Query provides you with a bare bones template project with all of the basic groundwork done for you. 

# Get Started With This Project

Before we continue, we should first lay basic pre-requisites for this project. A basic understanding of these concepts is imperative in order to execute this project properly.

- Basic SQL Skills
- Basic Python Skills
- Experience or Familiarity with Flask
- Experience or Familiarity with HTML

## Getting To Know The Source Tree

To fully understand how to get started with this project, let’s explore the source tree below:

```
src/
├── app/
│   ├── templates/
│   │   ├── index.html
│   ├── app.py
│   ├── sql.py
├── init.py
```

**Note that while there are other directories, we opted to not include them in this visualization as they are not relevant.* 

Most of the project’s code resides inside the ******`src`****** directory. This folder contains all your source code. In this directory, we have the ******`app`******folder, a subdirectory which contains all the code that runs the POS system. 

We also have the **************`init.py`************** script. When starting your project, this will be the first script to run as this initializes all the packages and defines the initial database schema. Before running this script, however, you must run your database first.

Let’s talk about how to host a SQL database for this project.

### **`init.py`** and Database Hosting Solution

For this project, we recommend downloading XAMPP. Not only will you have a GUI to work with when starting and terminating your SQL Server, you will also have a dashboard that allows you to directly interact your database.

By using XAMPP, you are eliminating hosting costs, and the production will be relatively easy and fast.

Run the XAMPP control panel and start the MySQL server. If you want to use the admin dashboard, make sure to run the Apache web server as well.

Now that you have it up and running, run the **`init.py`** script. You’ll notice that the python package manager or pip will start downloading packages. Don’t worry— this is normal. You should also see that the database is being initialized. Try viewing the MySQL **********`admin`********** panel using XAMPP. You will now see the **********`POS_IQ`********** database. This will be the database that we will use throughout our project.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58af1fd9-625e-4e11-a367-8fa05cb2392e/Untitled.png)

### App Directory

Now that we have initialized all the packages and database schema, let’s introduce ourselves to the ********app******** directory.

- **************app.py************** contains the backend server’s source code. This loads the html content and processes form submissions. This is heavily documented, so feel free to open the source code for more details. Modify this according to your project’s needs.
- ******************sql.py****************** is a wrapper class that handles the driver imports, initialization, and querying. This is heavily documented, so feel free to open the source code for more details. ********************************************************************This does not need to be modified.********************************************************************

### Templates

Contains your frontend source codes. For now, in contains just the **************`index.html`************** file. However, feel free to add styles, other pages, and Javascript logic. Make sure to render them accordingly in your ******`app.py`******.

## Database Schema

The database schema for this project is very simple. Below is a simple ERD representation of the initial database.

```
+----------------+     +----------------+     +----------------+
|     orders     |     |  order_items   |     |     items      |
|----------------|     |----------------|     |----------------|
| orderID (PK)   |<---1| orderID (FK)   |     | itemID (PK)    |
| Customer_Name  |     | itemID (FK)    |1--->| item_name (UQ) |
+----------------+     +----------------+     +----------------+
```

## What to do for this project:

Currently, this project sports a few food items and barely has any style and only supports CREATE functions. Here are a few milestones that you can impose:

- Add more products. Maybe shift to another industry (i.e., apparel)
- Implement all CRUD operations
- Add style and scripts.
- Add an admin dashboard with visualization.
- Create an analytics dashboard that aggregates sales per item, per time of day, etc.