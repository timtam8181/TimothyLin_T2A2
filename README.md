# TimothyLin_T2A2
***
[Timothy Lin Github T2A2](https://github.com/timtam8181/TimothyLin_T2A2 "Visit Timothy's Github")
***
## Installment steps:

***
### R1 - Identification of the problem you are trying to solve by building this particular app.
I am building this app to assist tourists plan out their holiday when they visit Melbourne. The problem is that when travelling, it can be stressful to plan out where to stay, visit and eat delicious local food. Tourists do not have a means to store all the information in one location and not only that, they do not have an idea of what to do or where to go for some recommendations!

By utilising this app, tourists will be able to receive recommendations if they are at a loss for finding a hotel, activities to do or places to eat. On top of that, they can put their plans into a consolidated set of daily plans, which will map out their visit to Melbourne.
***
### R2 - Why is it a problem that needs solving?
It is a problem that needs solving because as a tourist, visiting Melbourne for the first time, it is hard to know where are the best places to visit, to eat and hotels to stay. Additionally, to prevent confusion, there needs to be one place to store all this information as well as get some recommendations. 
- **Complicated:** Travel planning for a foreign location is very complicated. There are many different variables to consider such as picking activities, accommodation, restaurants to try. This app aims to simplify things by providing a centralised platform to create, update and manage their plans.  
- **Time wastage:** People are busy. When planning a trip, do not want to nor do they have time to spend countless hours scouring through different blogs, magazines, books to find the information required to visit. This API condenses all the information and makes it available to the user, saving time and effort.
- **Enhanced experience:** With a lack of information, people may not visit attractions that they would otherwise enjoy. Or, with the lack of planning, they may even run out of time to do things they would like to do. This can lead to deep regret and unfathomable sadness. This API alleviates these problems.
***
### R3 - Why have you chosen this database system. What are the drawbacks compared to others?
To build this application, I have decided to use the PostgreSQL database system. Because PostgreSQL is a relational database, it has many benefits that assist with creating a travel planning API. It offers Data integrity and relationships, Complex queries and reporting, ACID Compliance and it has much support since inception amongst developers all over the world. It is well recognised as one of the most reliable database systems in the world. With that being said, there are some drawbacks comapred to other database systems.

**PostgreSQL vs MongoDB**

**Data Model:** Travel planning involves having structured data, with locations, restaurants, activities, hotels and schedules.PostgreSQL supports this feature with it's pre-defined schema. The downside of this is that there is less flexibility compared to MongoDB, which utilises the schema-less method. If this app required more dynamic data structures, then MongoDB would be more efficient.

**Queries:** PostgreSQL has superior querying capabilities compared to MongoDB, which allows users in this API to complete complex queries to retrieve detailed information and find results based on more specific attributes. 

**Consistency:** ACID(Atomicity, Consistency, Isolation, Durability) compliance ensures data consistency and integrity is followed. In managing travel plans, transactional integrity is very important and PostgreSQL offers this whereas MongoDB prioritises availibility and scalability over consistency.

**Scaling:** As the Travel Itinerary API gains popularity and user numbers increase, MongoDB's ability to scale horizontally becomes advantageous. It can efficiently distribute data across multiple servers, ensuring seamless scalability. 

In summary, I have chosen to use PostgreSQL because my travel API requires data that has a clear and fixed schema, is ACID compliant, can handle complex queries and relational features for travel planning and vertical scaling is sufficient for performance needs.

**References:** 
[https://www.sprinkledata.com/blogs/mongodb-vs-postgres#:~:text=Both%20MongoDB%20and%20PostgreSQL%20can,may%20require%20additional%20hardware%20resources.](https://www.sprinkledata.com/blogs/mongodb-vs-postgres#:~:text=Both%20MongoDB%20and%20PostgreSQL%20can,may%20require%20additional%20hardware%20resources.)

[https://aws.amazon.com/compare/the-difference-between-mongodb-and-postgresql/#:~:text=MongoDB%20is%20a%20non%2Drelational,tables%20with%20rows%20and%20columns.](https://aws.amazon.com/compare/the-difference-between-mongodb-and-postgresql/#:~:text=MongoDB%20is%20a%20non%2Drelational,tables%20with%20rows%20and%20columns.)
***
### R4 - Identify and discuss the key functionalities and benefits of an ORM
The purpose of ORM is to assist object-oriented progamming developers interact with relational databases. They are able to abstract the low-level languages such as SQL queries and developers can utilise high-level programming constructs that come in methods to interact with the database, this in turn helps to simplify CRUD operations. By having ORM align with the principles of object-oriented programming, developers can work with objects and classes directly. This combination makes the mapping of database tables to application entities easier to understand. It makes code more readable and and developers are able to understand the database interaction more clearly from a holistic point of view of the whole application.

**Portability:** ORMs make it easier for developers to transition between different databases without needing to change too much code. This flexibility is useful because projects might need to change database systems down the line and with this measure, it alleviates concerns in regards to being locked into the database.

**Simplified database access:** ORM allows more ease of use for developers to access the database. Using an ORM is easier to understand and developers can interact with the database by using objects and methods instead of needing more complex SQL syntax for queries. This saves developers time and effort when programming, leading to increase efficiency and quicker task completion. 

**Automatic table creation:** Furthermore, ORM framerworks are able to create database tables using object classes instead of having to write SQL statements.

**Consistency:** ORM, with creation of frameworks creates a standard method for developers interact with databases. This allows for a roadmap that creates simplified and efficient code that is more maintainable and errors are easier to diagnose and handle.   


***
### R5 - Document all endpoints for your API
***
### R6 - An ERD for your app
***
### R7 - Detail any third party services that your app will use
***
### R8 - Describe your projects models in terms of the relationships they have with each other
***
### R9 - Discuss the database relations to be implemented in your application
***
### R10 - Describe the way tasks are allocated and tracked in your project
