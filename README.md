# EventbriteDjango

This is an Eventbrite app, which lets user select 3 categories and displays the list of events happening in those categories.
It has full setup with Virtual environment. 
___

## Running the App

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


___

## Demo 
### [Evenbrite App Demo] (http://eventbrite-app.herokuapp.com/)

___

## License

(The MIT License)

Copyright (c) 2015 Vipul Kanade


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

