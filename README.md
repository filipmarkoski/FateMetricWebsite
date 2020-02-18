### Commands needed to activate the repository:

open `cmd.exe`

before anything else please ensure you're running python `3.6`, `3.7` or `3.8` by running 
```
python -V
```
or, in case you have multiple python versions installed
```
python3 -V
```



## Cloning the git repository
clone this repository
```
git clone https://github.com/filipmarkoski/FateMetricWebsite.git
```
go into the folder
```
cd FateMetricWebsite
```
## Creating a virtual environment
create a virtual environment sandbox in the folder named `venv`
```
python -m venv venv
```
activate the virtual environment with:
```
cd venv/Scripts
```

and then running

```
activate
```

then go back to your root directory `FateMetricWebsite/`
```
cd ../..
```

within your root directory there is a textual file named `requirements.txt` using it run the following command which will install all needed python packages within the virtual enviroment, i.e. the `venv/` directory's subfolder named `site-packages`
```
pip install -r requirements.txt
```

wait while the installation finishes

## Initializing the local sqlite database
if the installation of packages was successful run the following django-related commands: 
```
python manage.py migrate
```

you use `manage.py` for all django-related functions such as django-project-level modifications.

because all migration files are already made there shouldn't be a problem. But in case there is, please run: 
```
python manage.py makemigrations
```
and then run:
```
python manage.py migrate
```

run the local django server:
```
python manage.py runserver
```

go to http://127.0.0.1:8000/ and ensure proper function of the web-app

# About FateMetric

This same text is displayed on the About page of the website.

FateMetric is currently in an alpha state and perhaps shall remain in such. 
There is a GitHub repository link provided at the bottom of the page, in the footer.

FateMetric is powered by the Python framework, Django. It's contains a blog where a person can log in, make a post, view other posts and even comment on them. 

Each post contains a comment thread which can be accessed by clicking the "Comment" button featured on the home page for each individual post, as well as a "Like" and "Dislike" button for the same one appropriately.

Furthermore, with regard to the blog, while making a post it is recommended that the posts be unique, in the sense that they provide original content, a creative view or opinion on a certain subject or material.

Thank you for using this website, we hope you enjoy the content provided by some of our users and/or staff.

For more information, feel free to contact us using the feature at the bottom of the page.