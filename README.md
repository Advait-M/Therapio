## Inspiration

In todays society, mental health problems have become seriously profound. At least 1 in 4 Canadians will have some form of serious anxiety disorder at some point in their lives, with almost 3 million Canadians aged 18 years or older reporting to have depression or anxiety. Moreover, by age 40, about 50% of the population will have or have had a mental illness, and suicide is one of the leading causes of death in both men and women from adolescence to middle age.

Mental illnesses affect people of all ages, education, income levels, and cultures. They indirectly affect all Canadians through family members, friends, or collegues, so though all of us may have not experienced severe mental health problems, most of us had been touched by it.

These realizations, along with our own experiences, and the knowledge that the wait time for psychiatrists in Canada was about 12 months, inspired us to create Therapybot, a Twitter Chatbot acts as a companion to traditional therapy and an entry point for those seeking help.

## What it does

At its base level, Therapybot analyzes your social media feed (namely twitter), listening for posts that contain "hot words", and language that could indicate that you are feeling, troubled, depressed, anxious, paranoid, or even suicidal. Upon realizing this, it sends you a text message asking if everything is okay, and if need be, informs you of the addresses of nearby therapists. This makes your journey when looking for help easier, as information is presented to you directly.

Then, Therapybot is open to hearing your story, and you are able to tell it how you feel. The resulting output is a motivational and supportive statement related to your problem, that helps you feel better. 

## How We built it

Twitter and Tweepy API is used to get tweets and send tweets using Python listeners in the backend.
MongoDB is used to securely store user accounts and their details e.g. location. Passwords are encrypted and hashed.
Node.js is used to create the website (browserified several node modules) and the server for communicating with the MongoDB.
PyMongo is used in Python to access the MongoDB.
Subprocesses are used in Python to enable multithreading, allowing for several tasks to run at once.


## Challenges We ran into

Twitter imposes a rate limit on API requests which severely impacted our testing. We had to create several Twitter accounts and user agents to get around this limitation.
It was our first time using Jade for HTML templating which was very cool.
Also our first time implementing a login system. Encrypting the password and hashing it was quite difficult.
Sentimentality analysis was not optimized for our data sets therefore we had to train it on some sample data.

## Accomplishments that We're proud of

* Simplifying the way we added GIFs.
* Training the chatbot to react to different scenarios and text inputs using NLTK.
* Building a chatbot on top of twitter.
* Analyzing twitter feeds.
* Setting up location recognition so Therapybot could find 

## What We learned

* How to write RESTful API calls (Faizaan)
* How to build a chatbot using API.ai and twitter.

## What's next for Therapio

* Make MongoDB database availible to therapists, so they may take cases, and gain useful information about how patients are doing when they are not in session with them, considering that the average time between sessions is 2 weeks in Canada.
* Allowing for the chatbot to message the user first, if it notices "hot words" or other kinds of language that could indicate mental illness and/or tendency for suicide on the user's timeline. We are not currently able to do this because of technical limitations in chatbot software today, and due to privacy, ethical and political reasons. However, receiving permission from governments and organizations to allow our bot to inititiate conversations (like Amber Alerts) could be very useful in developing our bot further, as it could move forward to treat mental health scenarios before they get out of hand.
