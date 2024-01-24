
# Add file upload to app
- my_site_blog (chapter 186-187, 5582f07)
- add Comment functionionality (chapter 189, )


# Add Admin
- my_site_blog (chapter 196)

# Read Later Setup (Using Sessions)
- my_site_blog (chapter 197 - 200)
    * chapter 197, 4ba9686 
    * add sessions in chapter 198
    * remove "Read Later" functionality


# Deployment
- see branch also "my_site_blog_deployable" (chapter 208-215 / 4a98c56)

## Checklist 
+ set DEBUG to False in production / replace with env var
+ static files
+ Add host to 'ALLOWED_HOSTS' in settings (use env variable)
    * getenv("APP_HOST") didn't work
    * environ.get('APP_HOST') works
+ replace SECRET_KEY with env variable 

## Deploy on AWS - Elasticbeanstalk (with zip file)
1. create Service "elasticbeanstalk"
2. create .ebextensions folder with django.config file:
    ```
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: my_site.wsgi:application
    ```
3. create zip file:
    * requirements.txt
    * manage.py
    * db.sqlite3
    * .ebextensions
    * project folder
    * app folders
    * staticfiles
    * templates
    * uploads

### In AWS/elasticbeanstalk 
4.
    + click through until environment variables and add 

        | Var name      | value     | Comment
        |-------------  |-----------| -----------
        | IS_PRODUCTION | True      | DEBUG, dont use
        | DEBUG         | FALSE     | DEBUG 
        | APP_HOST      | abc       | when deploying first use dummy value|

    + create / adjust IAM role

    + create / adjust IAM instance for EC2

5. Submit

6. In "Environment overview" / "Domain" open link. If this is first time deployment, take the url and add to APP_HOST environment variable in "configuration"
    
### Potential issues
+ Changes in AWS are not applying (eg modified env variables) -> Go to Actions/restart server

    
### Further
+ Custom domain with "AWS Route 53"
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html
+ Configuring HTTPS for your Elastic Beanstalk environment https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html


# Connect to PostgreSQL ()
1. 
    + pip install psycopg
    + https://docs.djangoproject.com/en/5.0/ref/databases/
    + https://pypi.org/project/psycopg/

### Further
+ AWS RDS Postgres Free Tier only for 1st year
+ elephantsql.com has for free tier (Turtle plan) only postgres v.10 which is too low