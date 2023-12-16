# TimothyLin_T2A2
***
[Timothy Lin Github T2A2](https://github.com/timtam8181/TimothyLin_T2A2 "Visit Timothy's Github")
[Timothy Lin Trello T2A2](https://trello.com/b/QE54OS1q/timothylint2a2 "Visit Timothy's Trello")
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
### Flask
- Flask is a Python web framework known for its simplicity and flexibility. It facilitates fast web application development through a micro-webframework approach,
offering essential components to enable developers to do this. Flask is widely used for building web applications and APIs due to its ease of use and scalability.
### PostgreSQL
- PostgreSQL is an open-source relational database management system, known for efficient management of details queries and substantial datasets. It implements ACID compliance, it has widespread support and use across divers applications as it has compatibility with different data types.
### SQLAlchemy
- SQLAlchemy is a Python SQL library, it facilities the integration of Python objects with relational database tables. Supporting diverse database engines, it incorporates a Object-Relational Mapping system. This library streamlines interactions with databases, enhances code efficiency, and enables developers to work using Python conventions.
### Marshmallow
- Marshmallow is a Python library that makes it easy to change complex data types to and from Python data types. It makes it more convenient to serialise and deserialise data. It is widely employed in web APIs to validate, parse, and format data which ensures smooth interactions with databases and efficient response handling.
### Psycopg2
- Psycopg2 is a tool that enables Python code to interact with PostgreSQL databases. Python applications can then connect and share information with PostgreSQL databases, which can handle data tasks. 
### Bcrypt
- Bcrypt is a guard for passwords on websites. It turns stored passwords into a random code that prevents them from being used by unauthorised parties. They are a good layer of protection against brute force attacks.
### JWT Manager 
- JWT manager handles JSON web tokens in web applications. It acts as a virtual ID card for web users, ensuring their identity is verified and granting access for a limited time.

***
### R8 - Describe your projects models in terms of the relationships they have with each other
### User
- Represents a user in the system. Users can create multiple daily plans. The relationship is made through the 'daily_plans' attribute, which represents a one-to-many relationships between users and their daily plans.
```
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
     
    daily_plans = db.relationship('DailyPlan', back_populates='user')
```

### Daily Plan
- Represents a daily plan created by a user. It holds references to selected restaurants, hotels, and attractions. The association with the 'User' model is established through the 'user' attribute, and has a many-to-one relationship. Each user can have many different daily plans, but each daily plan must belong to only one user.
```
class DailyPlan(db.Model):
    __tablename__ = "daily_plans"

    id = db.Column(db.Integer, primary_key=True)

    restaurant = db.Column(db.String())
    hotel = db.Column(db.String())
    attraction = db.Column(db.String())
    date = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d'))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', back_populates='daily_plans')
```

### Location
- Represents geographical locations to visit. It is a central place for different types of attractions, hotels and restaurants. The model has three one-to-many relationships. A location can have multiple restaurants, hotels and attractions.
```
class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    restaurants = db.relationship('Restaurant', back_populates='location')
    hotels = db.relationship('Hotel', back_populates='location')
    attractions = db.relationship('Attraction', back_populates='location')
```

### Restaurant
- Represents information about a restaurant. Restaurants are associated with a specific location. This is achieved through a many-to-one relationship with the 'location' attribute, indicating the that many restaurants can belong to a single location.
```
class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)

    cuisine = db.Column(db.String, nullable=False)
    price = db.Column(db.String)
    rating = db.Column(db.String, default=[])
   
    # Define ForeignKey with constraints
    location_id = db.Column(db.Integer, nullable=False)
    location = db.relationship('Location', back_populates='restaurants')

    # Add ForeignKeyConstraint
    __table_args__ = (ForeignKeyConstraint(['location_id'], ['locations.id']),)
```
### Hotel
- Stores information about hotels. Hotels are also related with a specific location in a many-to-one relationship. Each location can have many hotels associated with it.
```
class Hotel(db.Model):
    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.String, default=[])
   
    # Define ForeignKey with constraints
    location_id = db.Column(db.Integer, nullable=False)
    location = db.relationship('Location', back_populates='hotels')

    # Add ForeignKeyConstraint
    __table_args__ = (ForeignKeyConstraint(['location_id'], ['locations.id']),)
```
### Attraction 
- Stores details about attractions. Similar to hotels and restaurants, each attraction is associated with a specific location. Also through a many-to-one relationship established through the 'location' attribute.
```
class Attraction(db.Model):
    __tablename__ = "attractions"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.String, default=[])
   
    # Define ForeignKey with constraints
    location_id = db.Column(db.Integer, nullable=False)
    location = db.relationship('Location', back_populates='attractions')

    # Add ForeignKeyConstraint
    __table_args__ = (ForeignKeyConstraint(['location_id'], ['locations.id']),)
```

Together, these models represent a relational database where each entity has a specific role, and associations allow for efficient and easy navigation between them. Understanding these associations is paramount for creating proper queries and handling data within. 
***
### R9 - Discuss the database relations to be implemented in your application
- **In my application, I have created a Travel Plans database which has six different tables. My tables are Users, Daily Plans, Locations, Restaurants, Hotels and Attractions. I have used PostgreSQL because a relational database is required for this application as the tables need to connect with each other to create the features of the app.

- There is a One-to-many relationship with User to Daily Plans. Every User is allowed to have multiple daily plans but each Daily Plan belongs to only one User. This is implemented via the 'user_id' foreign key in the 'DailyPlan' model, and this is referencing the primary key in the 'User' model. The solid line in the ERD connecting the 'User' entity and the 'DailyPlan' entity, shows the one-to-many relationship. The arrow points from 'User' to 'DailyPlan' to signify the direction of the relationship.

- In turn, there is a Many-to-one relationship between Daily Plans to User, and this is represented with the user attribute in the 'DailyPlan' model. Which shows which user the daily plan belongs to.

- Also, I have three One-to-many relationships with Location to Restaurants, Hotels and Attractions. The 'restaurants', 'hotels', 'attractions' attributes in the 'Location' model represent the respective details that belong to each Location for users to select from if they would like. All three of the tables have the foreign key 'location_id' referencing the primary key 'id' in the 'Location' model. The 'Location' entity is connected to 'Restaurant', 'Hotel', and 'Attraction' entities with solid lines, illustrating one-to-many relationships. Arrows points from 'Location' to each of these entities.

- Lastly, There is a Many-to-one relationship where many restaurants, hotels and attractions can belong to one location.

***  
### R10 - Describe the way tasks are allocated and tracked in your project

