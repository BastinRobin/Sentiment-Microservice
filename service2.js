var http = require('http');

// User from the given MongoDB instance
var users = [
	{
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

//create a server object:
http.createServer(function (req, res) {

  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(users));

}).listen(8001); //the server object listens on port 8080