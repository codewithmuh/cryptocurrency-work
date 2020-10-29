from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from accounts.models.group.group import Group


class UserProfile(models.Model):
    TRADER = 'trader'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    description = models.CharField(max_length=250, null=True, blank=True)
    first_time_signed_in = models.BooleanField(default=False)

    @classmethod
    def create_user_and_send_email(cls, first_name, last_name, email, password):
        user = User.objects.filter(username=email).first()

        if user is not None:
            response = "Exist"
        else:
            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=email, password=password)

            user_profile = cls.objects.create(user=new_user)

            if user_profile:
                # subject = 'Email verification link'
                # message = 'Thanks for registeration'
                # msg_html = render_to_string('mails/email.html',
                #                             {'rec_username': str(first_name) + ' ' + str(last_name)})
                # from_email = settings.EMAIL_HOST_USER
                # to_list = [email, settings.EMAIL_HOST_USER]
                # send_mail(subject, message, from_email, to_list, html_message=msg_html, fail_silently=True)

                response = "Success"

        return response

    @property
    def get_user_name(self):
        return self.user.username

    @property
    def get_user_full_name(self):

        full_name = "{} {}".format(self.user.first_name, self.user.last_name)

        return full_name

    @property
    def get_user_first_name(self):

        return self.user.first_name

    @property
    def get_user_last_name(self):

        return self.user.last_name