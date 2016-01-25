# EventbriteDjango

This is an Eventbrite app, which lets user select 3 categories and displays the list of events happening in those categories.
It has full setup with Virtual environment. 
___

## Usage Instructions

1. Download or Clone this Repo
2. To start virtual environment traverse to folder cloned or extracted too
3. source bin/activate
4. cd src_eventbrite_django
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver (can also give ip:port_number to run on specific combo | default is 127.0.0.1:8000)

###Note
SECRET_KEY and AUTH_TOKEN have been masked for security reasons.
This can be substituted in file [bin/activate] (https://github.com/vipulkanade/EventbriteDjango/blob/master/bin/activate) on line 46, 47 respectively.

```bash
export SECRET_KEY='XXXXXXXXXXXXXXXXXXXX'
export AUTH_TOKEN="XXXXXXXXXXXXXXXXXXXX"
```
_AUTH_TOKEN can be generated or used from existing_ [Eventbrite Apps](http://eventbrite.com/myaccount/apps/)

_SECRET_KEY is key generated for your Django App_

___

## Demo 
### [Evenbrite App Demo] (http://eventbrite-app.herokuapp.com/)

___

## License

###Code
MIT License [see here] (https://github.com/vipulkanade/EventbriteDjango/blob/master/LICENSE)

###Images
[Creative Commons Attribution 3.0 Unported (CC BY 3.0) License] (http://creativecommons.org/licenses/by/3.0/)
