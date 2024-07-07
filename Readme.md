# Software Bytes

## Project Overview

This project is a tech blog where I write about various topics in technology, from explaining basic data structures to more advanced concepts. The blog aims to provide clear, concise, and informative content to help readers understand and navigate the complexities of the tech world.

## Features
- *Home Page*: Displays a list of recent blog posts.
- *Blog Posts*: Detailed articles on various tech topics.
- *Categories*: Posts categorized by topics. (comming soon)
- *Search*: Ability to search for specific posts. (comming soon)
- *Admin Interface*: Manage blog posts, categories, and other site content.

## Technologies Used
- *Django*: The web framework used to build the blog.
- *SQLite*: The default database for development.


## Installation
1. Clone the repository:
```shell
    git clone  git@github.com:PhilaniMhlongo/Django-Blog.git 

```
2. Create a virtual environment and activate it:
```shell
    python -m venv venv
    source venv/bin/activate
   ```
   
3. Install the dependencies:

```shell
pip install -r requirements.txt
```


4. Run migrations to set up the database:

```shell
python manage.py migrate
```



5. Create a superuser for accessing the admin interface:

```shell
python manage.py createsuperuser
```



6. Start the development server:

```shell
python manage.py runserver
```

    

7. Access the blog:

    Open your browser and go to http://127.0.0.1:8000/blog/.

Usage

    Admin Interface:
        Go to http://127.0.0.1:8000/admin/
        Log in with the superuser credentials
        Manage posts, categories, and other content

    Creating a New Post:
        Go to the admin interface
        Add a new post under the "Posts" section
        Fill in the title, content, and select a category
        Save the post

    Viewing Posts:
        Navigate to http://127.0.0.1:8000/blog/
        Browse through the list of posts or use the search feature to find specific topics



