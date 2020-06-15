<<<<<<< HEAD

## NLP On Exchanging Diverse Data Microservices

NLP is a subset of AI and Machine Learning, in this usecase we are using three microservices for a calculating sentiment for 
feebacks given by users on a ecommerce sites.

### Service 1
- Build using PHP and MySQL as the databases
- Each feedback consist of user_id, comments for each product

#### To run the service follow the command
    php -S localhost:8000
	
#### Check
    http://localhost:8000/service1.php

#### Data Model

	|id | user_id | product_id  | comments                |
	|---|---------|-------------|-------------------------|
	|1  | 1       | 1           | Iphone has been broken  |
	|---|---------|-------------|-------------------------|
	|2  | 2       | 1           | Computer was best buy   |
	|---|---------|-------------|-------------------------|


### Service 2
- Build using Node and MongoDB as the databases
- Each user has been stored as JSON array

#### To run the service follow the command
    node service2.js

#### Check
    http://localhost:8001
    
#### Data Model

	[{
		'bsonid': 'xusyis892js98siw8',
		'name': 'Jack',
		'email': 'jack@gmail.com',
		'id': 1 
	},
	{
		'bsonid': 'usyu2j9739478992',
		'name': 'James',
		'email': 'james@gmail.com',
		'id': 2
	}];


### Service 3
- Build using Python and TextBlob as the sentiment analysis 
- Each feedbacks has been ranked as JSON array

#### To run the service follow the command
    python service3.py
    
#### Check
    http://localhost:8002/service
    
#### Data Model

	[{
		"polarity":"NEGATIVE",
		"user_id":1,"name":"Jack",
		"comments":"Iphone has been broken",
		"email":"jack@gmail.com",
		"bsonid":"xusyis892js98siw8",
		"id":1},
	{
		"polarity":"POSITIVE",
		"user_id":2,"name":"James",
		"comments":"Computer was best buy",
		"email":"james@gmail.com",
		"bsonid":"usyu2j9739478992",
		"id":2
	},
	{
		"polarity":"NEUTRAL",
		"user_id":1,"name":"Jack",
		"comments":"Microphone was not working",
		"email":"jack@gmail.com",
		"bsonid":"xusyis892js98siw8",
		"id":1
	}]

