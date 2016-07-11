## To start server

```python
 python manage.py runserver
```

### Login Route

http://127.0.0.1:8000/admin/
* After logging in you'll need to go to the home route yourself, there is no redirect

### Home Route

http://127.0.0.1:8000/

### Run Tests

./manage.py test

### Requires

[Django](https://www.djangoproject.com/)

[Django Nocaptcha Recaptcha](https://github.com/ImaginaryLandscape/django-nocaptcha-recaptcha)
* Use ``` pip install django-nocaptcha-recaptcha ``` to install

## Superuser Credentials

Username: PatchmanAdmin

Email: patchman@admin.com

Password: patchmanpassword

## Regular User Credentials

Username: SecondUser

Password: number2password

Does have staff status, does not have superadmin status


Username: ThirdUser

Password: number3password

Does have staff status, does not have superadmin status