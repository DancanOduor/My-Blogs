# Blog application
This  application allow users to create blog post

# Users are able to:

* View the blog posts on the site
* Comment on blog posts
* View the most recent posts
* Get an email alert when a new post is made by joining a subscription.
* See random quotes on the site
* Sign in to the blog.
* Create a blog from the application.
* Delete comments that I find insulting or degrading.

# Set-up Requirements
* python3.7
* Flask 1.0
* Virtualenv
# Technologies
* Bootstrap4 -CSS3

# Cloning
* In your terminal:

 * $ git clone https://github.com/DancanOduor/My-Blogs.git

 #  Blog-Post
 * $ cd Blog-Post
 * Running the Application
* Creating the virtual environment

  * $ python3 -m pip install --user virtualenv ( on a Mac)
 *  $ python3 -m virtualenv env
  * $ source env/bin/activate
  * $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
* Installing Flask and other Modules

* While in the virtalenvironment install all * the requirements by running $ pip install -r requirements.txt
* Setting up the quotes base url

# To run the application, in your terminal:

 * $ chmod a+x start.sh
 * $ ./start.sh
* Testing the Application
# To run the tests for the class files:

 *  $ python3.6 manage.py tests
# Known bugs
* The comment functionality is currently not routing as expected and will be fixed in the next iteration.
