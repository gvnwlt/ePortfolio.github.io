![profile picture](/images/viewprofileimage.d2l.jpg)

## ePortfolio Introduction

My experience in the computer science curriculum and capstone has enhanced my current and future career contributions by gaining a deeper understanding of the fundamentals of computer science.  The computer science curriculum has provided me with the required competencies across a broad range of topics so that I can be a better asset in the field. This portfolio highlights the foundational work that I have produced. 

Collaborating with team environments has played a large part in various courses throughout the curriculum so far as receiving and providing feedback to fellow classmates on development projects. Using version control software, such as Git, to carryout code reviews and to perform operations on different development branches was a vital process, as working in the real-world of development utilizes collaboration in this form heavily. All of the projects that are presented in this portfolio are a result of that process in one way or another, meaning that each project was a result of utilizing collaboration or feedback to produce the best possible product outside of my own bias. Design approach methodologies such as Agile have played a large role in the development process as well, providing the necessary framework to rapidly stand up a project and continuously make progress towards the deliverable. 

The artifacts in this portfolio represent four of the main aspects of computer science in the industry: 
 - software engineering and design
 - data structures and algorithms
 - databases
 - security
    
Each of these projects incorporates all of these aspects (for the exception of databases), but some are more representative of a certain aspect than others. Security is included as a component of creating code that is safe in operation and encapsulated where needed. 

The takeaway from these projects is that the core components of computer science have been internalized to produce quality work in the field as a software engineer. I currently work as a software engineer (started half way through the curriculum in 2017) and have found these principles of computer science  to be the biggest part of having success in my career so far. Going forward, I plan on enhancing these skills further to be a better software engineer that can adapt to various technologies quickly and I also intend on using what I have learned in this degree and in my current career to contribute to my graduate studies later on. 

### Computer Science Artifacts Code Review 

[Code Review](https://youtu.be/BmnVwuQxGuQ)

## Artifact Enhancements 

### 1. Software Engineering and Design: Zoo User Access from Java to Python
The Zoo User Access application was a final project for a foundations and application development course for the May 2017 term. Zoo User Access was written in Java using an object oriented approach. This program receives standard input from a user for a user name and password, for which it then verifies by importing a text document containing user credentials such as login in name (first.last), an md5 hashed password, and the user's role within the zoo access system. The program displays a message to the user and exits if three failed login attempts are made. If the user provides the correct login information, the zoo user system is accessed and displays a message imported from a text file that is associated with the user account based on the user's role in the credentials file. Once in the system is accessed, the user is given an option to logout at any time by command line input. 

I selected this application for the portfolio to demonstrate my understanding of developing efficient code and as an oppurtunity to show that I can adapt between programming languages as a full-stack developer/software-engineer by converting it to Python. This also seemed to be a good way to gauge how much I have improved in sofware engineering over the past year. During the code review I noticed that this application had some flaws even though it was functional. There was a lot of unecessary code that made the application less readable and efficient in the use of runtime processes. 

This enhanced artifact showcases a deeper understanding of code design and use of object-oriented developement to create well-crafted applications. Comparing the source code between the old and new artifacts, there was clearly a reduction in unecessary code as the Java application was written with a total of approximately 200 lines of code while the Python application was written using only 100 or so lines. Also, the use of control structures was dramatically improved in the enhanced version where there were nearly 80% less conditional and loop structures. This may correlate with the some of benefits of the Python language and standard libraries, but much of the design that was employed concerning control structures could have been applied the Java application. The enhanced Zoo User Application application also consumes less resources in terms of memory and computation while providing oppurtunities for further development via object-oriented design. 

The overall outcome as stated in the enhancement plan was to make the application simpler in its design which I believe was achieved by the elimination of uncessary control structures and by the usage of clear syntax to enhance readability outside of using descriptive comments. The only challenge I struggled with during the enchancement of this artifact was the shear number of ways I could use Python to extract text from a file while maintaining a simple code design. In the end, I decided to utilize a Python standard library for regular expressions to validate user entries against the text documents as well as construct statements that efficiently performed file opening, stream reading, and file closing operations safely. I learned a great deal on the benefits of Python for string/text operations and object-oriented programming. I look forward to utilizing Python more in my career as I have discovered many great libraries over the course of this development that are suitable for robotics and low-level intefacing. 

[ZooUserAccess Project](https://github.com/gvnwlt/ePortfolio.github.io/tree/master/ua_1)

### 2. Data Structures and Algorithms: Linked List to Doubly Linked List
The artifact used to demonstrate knowledge with data structures and algorithms was an assignment used for a final project in CS 260 during the January 2018 term. This project was involved implementing a linked list in c++ to read from a “csv” file and store its entries into the data structure. Basic operations to interact with the list were created to insert, delete, and read entries using the appropriate algorithms to manage the list. 

I chose to include this artifact to demonstrate one of the most fundamental aspects in computer science—that is implementing data structures and logic to handle data or operations efficiently. This artifact includes various aspects of computer science from software engineering and design to data structures and algorithms. It highlights understanding of the underlying operations that take place under the hood of many of the libraries and frameworks that take care of these operations in a given API. 

The primary objective in this plan was stated as demonstrating competency in implement these data structures . I believe I carried out this plan by implementing a doubly linked list to replace the linked list while also improving the previous application overall. I decided this was suitable for an enhancement because it still demonstrated where I was able to enhance the original code while also implementing a new data structure with newer capabilities. It also gave me an opportunity to clean up the code from before and enhance the design further. 

One thing I learned from this enhancement is that the code can always be improved. I generally use a task list of things to carry out during a project to make sure I stay on track with the requirements. It was very hard to restrain from finding other things that could use an upgrade or be tweaked differently. I still met the requirements I had laid out, but I found myself getting carried away at times with wanting to fix or work on other details which ends up spiraling into getting away from the main objective. The main takeaway is that having a back-burner list is a useful tool to keep track of a list of “wants” in terms of improving a project to keep moving forward in the interest of time. 
 
 [Doubly Linked List Project](https://github.com/gvnwlt/ePortfolio.github.io/tree/master/ua_2)

### 3. Databases: Impelmenting Trained Machine Learning Model with PyMongo
The artifact included for the database enhancement was from my Advanced Programming course during the July 2018 term. This project was used as a RESTful API service incorporating Python, MongoDB, and the Bottle framework. It consists of a number of functions that operate on a Mongo database. A user can send HTML POST/REQUEST to invoke a function that will perform CRUD operations on a given collection.  

For the enhancement I decided to implement a trained machine learning model to predict a companies profit margin with a market database. It uses a set of given predictors and a dependent variable to generate a linear model. Once the model is trained it is serialized and exported to the main python file so that a function may be called to get a batch of predictors for a specified company in the database and use them as input on the imported model. I feel that the code contains a good functional approach and includes the major CRUD operations needed to interact with a database. 

I selected this artifact because I enjoy working with Python and I wanted to implement a machine learning model in a practical situation such as gaining insight on information in a database. The plan has been executed well so far, and I feel that this artifact is very close to being ready for the portfolio after feedback. 

Some of the issues I had during this enhancement involved configuring the necessary Python libraries on a remote system. I believe I would better off just implement my own MongoDB on my host machine (most likely a virtual machine). For the most part, I learned that Python is a very powerful tool for creating useful code simply and efficiently. And, I finally learned how to deployed a trained machine learning model as a functional piece of software, rather than just generating models and evaluating the output. Machine learning is something I want to bring into practice more in my software engineering projects by training models and importing them in as functions or parts of functions. 

 [Database/Machine Learning Project](https://github.com/gvnwlt/ePortfolio.github.io/tree/master/ua_3)

