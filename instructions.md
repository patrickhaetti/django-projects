
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
- see also "Serving Static Files (via S3)"  18. for updated required files 

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
    
### Potential issues AWS/elasticbeanstalk
+ Changes in AWS are not applying (eg modified env variables) -> Go to Actions/restart server
+ uploaded requirements file didn't accept psycopg2 along with psycopg2 -> use psycopg2-binary library



### Further
+ Custom domain with "AWS Route 53"
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html
+ Configuring HTTPS for your Elastic Beanstalk environment https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html


# Connect to PostgreSQL ()
1. 
    + pip install psycopg
    + https://docs.djangoproject.com/en/5.0/ref/databases/
    + https://pypi.org/project/psycopg/

2. neon.tech offers free postgres tier. DATABASES info for settings.py will be offered to copy/paste from dashboard.
    https://neon.tech/docs/guides/django

3. Set environemnts variables in host environment


### Further
+ AWS RDS Postgres Free Tier only for 1st year
+ elephantsql.com has for free tier (Turtle plan) only postgres v.10 which is too low


# Serving Static Files (via elasticbeanstalk)

1. add .ebextensions/static-files.config
where /static points to STATIC_ROOT = BASE_DIR / "staticfiles" as in settings.py
and /files point to MEDIA_ROOT = BASE_DIR / "uploads"

```yaml
option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles
    /files: uploads
```
this instructs the server to handle requests targeting /static and /files with the files stored in staticfiles respectively uploads

2. remove static from urlpatterns
2. Change webserver configuration in settings.py



# Serving Static Files (via S3)
 
## Set Up AWS + Backend

 1.  open S3 console
    - add new bucket (used Europe (Frankfurt) eu-central-1)
    - uncheck "Block all public access" (makes it publicly accessible)  & acknowledge danger warning

2. 
 go into bucket / properties
 go to Static website hosting: Enable
 choose "Host a static website"
 add index.html but it doesnt matter, aws just asks for a name

 3. 
 go into bucket / permissions
 go to "Cross-origin resource sharing (CORS)"
 add
 ```json
[
    {
        "AllowedHeaders": [
            "*"
            ],
        "AllowedMethods": [
            "GET", "POST"
            ],
        "AllowedOrigins": [
            "*"
            ],
        "ExposeHeaders": []
    }
]
```
this means resources can be fetched from other domains, ie beanstalk has another address than bucket

4. Ensure that requests can reach this bucket:
go into bucket / permissions
Bucket policy


 add
 ```json
{
  "Version": "2012-10-17",
  "Statement": [{
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::bucket-name/*"
    }
  ]
}
```

make sure bucket-name is the name from the created bucket


5. Grant access to bucket for django with IAM service
* go to IAM Dashboard / User Groups
* create User Group
* add policy "AmazonS3FullAccess"
* Add users -> create new user &  & add to user group created in step before


for creating access key and  secret access key, choose
"local code"

save keys


6. go to project

```bash
pip install django-storages boto3
```

7. update requirements


8. 
go to settings.py

add 

INSTALLED_APPS = [
    ....
    'storages',



9. overwrite default storage mechanism:

add AWS settings which will be picked up by boto3

go to settings.py

add 


AWS_STORAGE_BUCKET_NAME = ""
AWS_S3_REGION_NAME= ""
AWS_ACCESS_KEY_ID= ""
AWS_SECRET_ACCESS_KEY_ID = ""

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"



10. collectstatic

```bash
python3 manage.py collectstatic
```
This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: 

-> "yes"


11. Check if all is working locally

start dev server without local static files
```bash
python3 manage.py runserver --nostatic
```


## Moving File Uploads to S3

12. create custom_storages.py file in root directory
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticFileStorage(S3Boto3Storage):
    location = settings.STATICFILES_FOLDER

class MediaFilesStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_FOLDER
```

13.  add 'static'/'media' folder names in settings to be created in S3

- folder name of choice, not related to 'static'/'media' dirs from above. 
- Folder with this name will then be created in S3 bucket
STATICFILES_FOLDER = "static" 
MEDIAFILES_FOLDER = "media"

14. Update STATICFILES_STORAGE / DEFAULT_FILE_STORAGE
with names from classes in custom_storages.py,
ie. 
* storages.backends.s3boto3.S3Boto3Storage -> custom_storages.StaticFileStorage
* storages.backends.s3boto3.S3Boto3Storage -> custom_storages.MediaFilesStorage

15. If there are old files in Bucket, delete them now

16. collect static files and upload them 
```bash
python3 manage.py collectstatic
```

17. Run locally for testing without the built in static file serving capabilities

```bash
python3 manage.py runserver --nostatic
```

18. required files for deployment:
    * requirements.txt
    * manage.py
    * db.sqlite3 (can be left out when using cloud DB)
    * .ebextensions
    * project folder
    * app folders
    * templates
    * custom_storages.py