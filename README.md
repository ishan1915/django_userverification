Email Verification for Django 
A simple email verification system for Django projects.

Overview
This project provides a basic email verification system for Django applications. When a user signs up, an email verification link is sent to their email address. The user must click on this link to activate their account.

Features
Email verification using a unique token
Automatic account activation upon clicking the verification link
Customizable email templates and views
Installation
Clone the repository: git clone https://github.com/ishan1915/email-verification-django.git
Install the required packages: pip install -r requirements.txt
Add the email_verification app to your Django project's INSTALLED_APPS setting: INSTALLED_APPS = [..., 'email_verification', ...]
Run the migrations: python manage.py migrate
Configuration
Add the following settings to your settings.py file:
python

Verify

Open In Editor
Edit
Run
Copy code
EMAIL_VERIFICATION_TOKEN_EXPIRY = 60 * 60 * 24  # 1 day
EMAIL_VERIFICATION_EMAIL_TEMPLATE = 'email_verification/email_verification_email.html'
EMAIL_VERIFICATION_SUCCESS_TEMPLATE = 'email_verification/account_activation_success.html'
Create the email templates email_verification_email.html and account_activation_success.html in your project's templates directory.
Usage
In your user registration view, call the send_verification_email function to send the verification email:
python

Verify

Open In Editor
Edit
Run
Copy code
from email_verification.utils import send_verification_email

def register_user(request):
    # ...
    user = User.objects.create_user(...)
    send_verification_email(request, user)
    # ...
In your URL configuration, add a URL pattern for the activation view:
python

Verify

Open In Editor
Edit
Run
Copy code
from django.urls import path
from email_verification import views

urlpatterns = [
    # ...
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    # ...
]
License
This project is licensed under the MIT License. See LICENSE for details.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

Issues
If you encounter any issues or have questions, please open an issue on this repository.

Author
[ISHAN]

Acknowledgments
This project was inspired by the Django documentation and various online tutorials.
