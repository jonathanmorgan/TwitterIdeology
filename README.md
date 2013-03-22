# TwitterIdeology

## Description

TwitterIdeology uses tweetnet to explore ideology in Twitter news-sharing.

Not a whole lot else to say here at the moment until I start integrating code to easily pull in tweets for a user, or based on a topic.

To install, pull the application from github, then place it in a working django site and add it as a new application in settings.py.

From the django-enabled python shell (python manage.py shell), enter "import <site>.TwitterIdeology" to pull in the TwitterIdeology context.

For examples of how to authenticate and interact with twitter using a number of different python twitter and oauth libraries, see sample_code.py.

## Depends on:
- tweetnet: https://github.com/jonathanmorgan/tweetnet.git