# HowzThat - Celebrating Local Cricket Heroes 
## Description
HowzThat provides a user-friendly web application that enables **real-time tracking of live cricket scores** for local matches and players to showcase their skills and achievements built using Django. It provides a intuitive interface to host live cricket matches. It provides cricket enthusiasts with easy access to information about matches and player statistics.

## Features 
- Live score updates: Real-time updates of scores for ongoing matches using web sockets. **Providing a smooth user experience and reducing the server load without the hassle of page reloads using consistent web socket connection**.
- Match schedules and fixtures: Detailed schedules and information about
upcoming and ongoing matches.
- Player profiles: In-depth profiles of players, including
statistics and match history.
- User registration and authentication: Allowing users to create accounts and
log in to personalize their experience using django authenticate.
- Data storage and retrieval: Efficiently storing and retrieving match data, player
information, and user preferences using MYSQL.
- Error handling and validation: Implementing mechanisms to handle errors and
validate user input.

## Tools and Technologies 
- Django: Web framework utilising python capabilities to build a robust web application
   - Channels and Websockets: Used Django Channels to implement WebSockets, making the web pages dynamic. **This is crucial for real-time score updates, allowing the host to update match information without requiring users to reload the page for every change**
   - Authentication: Django's built-in authentication system used to
manage user logins securely.
- HTML, CSS, JavaScript: To build web pages ensuring a dynamic user experience.
- MySQL: Database manangement system to store all the information about users, matches and scores.
- Git and GitHub: Git for version control and GitHub for code repository hosting, collaboration, and project management.

## Installation and Setup
- Clone the repository
`git clone https://github.com/Sohail4625/HowzThat.git`
- Change the database settings in `liveHost/liveHost/settings.py` to your MySQL database configuration 
```
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'',
    }
}
```

 - Ensure you are in liveHost which has manage.py
 - Install requirements `pip install -r requirements.txt`
 - Migrate `py manage.py makemigrations`
   `py manage.py migrate`
 - Then start the server `py manage.py runserver`
 - Go to url `127.0.0.1:8000/`
### For user guide and complete documentation download the pdf - [Documentation](/Documentation.pdf)
