import tornado.ioloop
import tornado.web
import requests
import json
from textblob import TextBlob


SERVICE1_URL = 'http://localhost:8000/service1.php'
SERVICE2_URL = 'http://localhost:8001'


def sentiment(text):
	"""
	Calculate the sentiment for the 
	given text and return the polarity
	"""
	blob = TextBlob(text)

	if blob.sentiment.polarity == 0:
		return 'NEUTRAL'

	if blob.sentiment.polarity > 0:
		return 'POSITIVE'

	if blob.sentiment.polarity < 0:
		return 'NEGATIVE'



def find_user(users, user_id):
	"""
	Finds an user using the give users list

	"""
	for user in users:
		if user['id'] == user_id:
			return user


def calculate_sentiment(feedbacks, users):
	"""
	Loop through each feedback and calculate the 
	sentiment for each feedback and also gather their 
	user details
	"""
	feedbacks = json.loads(feedbacks)
	users = json.loads(users)

	for feed in feedbacks:

		feed['polarity'] = sentiment(feed['comments'])
		u = find_user(users, feed['user_id'])
		feed.update(u)

	return feedbacks




class MainHandler(tornado.web.RequestHandler):
    def get(self):

    	feedbacks = requests.get(SERVICE1_URL).text
    	users = requests.get(SERVICE2_URL).text
    	response = calculate_sentiment(feedbacks, users)
        self.write(json.dumps(response))


def make_app():
    return tornado.web.Application([
        (r"/service", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8002)
    tornado.ioloop.IOLoop.current().start()