# QA-DevOps-Fundamental-Project - Library System
This repository contains my delivarable for the QA devops fundamental project.

## Contents
* [Objectives](#Project-Brief)
* [Scope](#Project-Brief)
* [Application Design](#Project-Brief)
* [Database Schema](#Project-Brief)
* [Trello Board](#Project-Brief)
* [Risk Assessment](#Project-Brief)
* [Version Control](#Project-Brief)
* [The Application](#Project-Brief)
* [Future Work](#Project-Brief)
* [Usage](#Project-Brief)

## Objectives 
To create an application with CRUD functionality (Create, Read, Update, Delete) with utilisation of supporting tools, methodologies and technologies - including Databases, Python, Flask, Testing, Basic Linux, Git and Project Management.

## Scope 
The requirements of the project are as follows: <br>
* A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
* A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
* A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
* A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board.
* Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
* A functioning front-end website and integrated API's, using Flask.
* Code fully integrated into a Version Control System using the
Feature-Branch model.

## Application Design
I decided to develop a library management system that is designed to manage all functions of a library. The application was developed to help librarians maintain the database of new books, and existing books that are borrowed by members of the public. A use case diagram was designed to model the functionality of the system and how users may interact with it:

<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/use-case.png?raw=true">
</p>

The library management system allows the admin to create a new book, update an existing book's information and remove an existing book from the database. On the otherhand, when a user logs into the application, they can hire a book, review a book and request a book that is not available in the database. The admin can handle the user's book requests and dimiss the request if it not feasible. Finally, the admin has the ability to delete any review that is not appropriate. 

## Database Schema 
All of the previous functionality is possible with the help of a MySQL database. The schema is as follows:
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/class-diagram.png?raw=true">
</p>

## Trello Board
Trello was used from start to finish on the project to track progress and ensure that no task slipped through the cracks. Within the trello application, a kanban board was used to help visualise the workflow. 
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/moscow.png?raw=true">
</p>
Items were assigned story points, acceptance criteria and MoSCoW prioritsation, and moved from to "to-do" and then "doing" and finally "done" as the project progressed. The following image displays the initial state of the trello board at the beginning of sprint one:
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/1-TrelloBoard.png?raw=true">
</p>
The following image displays the state of the trello board after the minimum viable product (MVP) was achieved: 
<br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/2-TrelloBoard.png?raw=true">
</p>

## Risk Assessment
This placeholder will be updated by the end of the day - 16/11/2022

## Version Control
This placeholder will be updated by the end of the day - 16/11/2022

## The Application
### Admin side
Once logged in, the admin is presented with all of the books in the database. This is where the admin can make use of the CRUD functionality.
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/1-admin-books.png?raw=true">
</p>
To add a book, the admin presses on the green button named "Add Book" and is displayed with a form that asks for the book title, author, a description of the book and a number of copies. 
<br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/2-add-book.png?raw=true">
</p>
To edit a book, the admin presses on the green button named "Edit." The form is populated with the information on the same row as the button. From here, the admin can update the book's information. <br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/3-edit-book.png?raw=true">
</p>
To delete a book, the admin presses on the red button named "Delete." An "are you sure" message is presented to the admin incase of a mistake. If "OK" is pressed, the book is deleted from the database. <br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/4-delete-book.png?raw=true">
</p>

## User
Once logged in, the user is presented with all of the books in the database.
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/5-user-books.png?raw=true">
</p>
To review a book, the user presses on the green button named "Review." The user can then enter their thoughts on the book within the area provided. <br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/6-review-book.png?raw=true">
</p>
To request a book, the user first must access the requests tab in the sidebar. The user is then presented with a form which asks for the book title, author and a description of the book. <br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/7-request-book.png?raw=true">
</p>
To return a book, the user first must access the records tab in the sidebar. The user is then presented with a list of books currently issued to them and the expected return date. From here, a user can return a book using the return button. <br><br>
<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/8-return-book.png?raw=true">
</p>

## Extra 
The reviews are visible on both the user and admin side of the system. However, the admin has the option to delete a review if it is not appropriate.

<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/4.1-manage-reviews.png?raw=true">
</p>

Also, the user's requests are visible on the admin side of the system. The admin can handle the request by either adding the book to the database or deleting the request.

<p align="center">
    <img src="https://github.com/Adamcoakley/LibrarySystem/blob/main/readme-images/4.2-manage-requests.png?raw=true">
</p>

## Future Work
This placeholder will be updated by the end of the day - 16/11/2022

## Usage
