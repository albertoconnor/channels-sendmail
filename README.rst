=================
Channels Sendmail
=================

Simple package to wrap Django's built-in `send_mail` function with
channels, sending the mail with whichever backend you are using
asynchronously.

Install
=======

Requires Django 1.8+ and Channels.

.. code:: bash

  pip install channels-sendmail


Usage
=====

Add to your routing

.. code:: python

  channel_routing = [
    # ...
    include('sendmail.routing.channel_routing'),
  ]

Use where you have used `django.core.mail.send_mail` in the past:

.. code:: python

  from sendmail import send_mail

  send_mail(...)  # Normal arguments to send_mail


Configuration
=============

* `CHANNELS_SENDMAIL_CHANNEL_NAME` which defaults to
  "django.core.mail.send_mail"
