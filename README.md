"# blog-app" 
Blog App
A Django-based blog application that allows users to create and manage blog posts. Authors can register and post content, while the app also supports features like content validation, readability checks, category management, and author tracking.

Features
Author Registration: Authors can sign up, add a bio, and include contact information.
Blog Post Creation: Create and manage blog posts with categories and publishing options.
Content Validation: Includes checks for content length, readability, forbidden words, and plagiarism.
Category Management: Organize posts under categories and display the most popular category.
Top Authors: Retrieve the top three authors with the most posts in the last 6 months.

API Endpoints
Here are the main API endpoints for interacting with the app.

Blog Endpoints
Create Blog Post: POST /blogs/create/
List Blogs: GET /blogs/
Blog Details: GET /blog/details/
Author Endpoints
Create Author: POST /blogs/createauthor/
Top Authors: GET /top-authors/
Category Endpoints
Create Category: POST /blogs/createcategory/
Popular Category: GET /category/popular/


Create Blog Post -json

POST /blogs/create/
{
  "title": "Sample Blog Post",
  "content": "This is an example of blog content with more than 500 characters...",
  "author": 1,
  "category": 1  
}

Create Author - json

POST /blogs/createauthor/
{
  "username": "johndoe",
  "password": "securepassword123",
  "bio": "Enthusiastic writer and blogger.",
  "contact_info": "contact@example.com"
}


Here’s a sample README.md for your blog application. This provides an overview of the project, installation steps, setup instructions, and example usage.

Blog App
A Django-based blog application that allows users to create and manage blog posts. Authors can register and post content, while the app also supports features like content validation, readability checks, category management, and author tracking.

Features
Author Registration: Authors can sign up, add a bio, and include contact information.
Blog Post Creation: Create and manage blog posts with categories and publishing options.
Content Validation: Includes checks for content length, readability, forbidden words, and plagiarism.
Category Management: Organize posts under categories and display the most popular category.
Top Authors: Retrieve the top three authors with the most posts in the last 6 months.
Requirements
Python 3.10+
Django 5.1+
Django REST Framework
textstat (for readability checks)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/blog-app.git
cd blog-app
Set Up a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Database Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (Optional, for admin access):

bash
Copy code
python manage.py createsuperuser
Run the Server:

bash
Copy code
python manage.py runserver
API Endpoints
Here are the main API endpoints for interacting with the app.

Blog Endpoints
Create Blog Post: POST /blogs/create/
List Blogs: GET /blogs/
Blog Details: GET /blog/details/
Author Endpoints
Create Author: POST /blogs/createauthor/
Top Authors: GET /top-authors/
Category Endpoints
Create Category: POST /blogs/createcategory/
Popular Category: GET /category/popular/
Example API Requests in JSON
Create Blog Post

json
Copy code
POST /blogs/create/
{
  "title": "Sample Blog Post",
  "content": "This is an example of blog content with more than 500 characters...",
  "author": 1,
  "category": 1,
  "is_published": true
}
Create Author

json
Copy code
POST /blogs/createauthor/
{
  "username": "johndoe",
  "password": "securepassword123",
  "bio": "Enthusiastic writer and blogger.",
  "contact_info": "contact@example.com"
}

Create Category - json

POST /blogs/createcategory/
{
  "name": "Technology",
  "description": "Latest trends and updates in technology."
}
