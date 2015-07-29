===============
KeyVal Settings
===============

A very basic Django app that gives admins an interface to set (for now) public settings.
Essentially, it is a 'dictionary for your project'.

Important Notes:
----------------
- :code:`False`, :code:`True`, :code:`None` will get converted into their json counter-parts when calling the view, but normal when calling functions in code.
- There is currently no support for 'true' arrays and dictionaries, however, a json dictionary will properly format.
- At the moment, there is nothing preventing duplicates.

Potential uses
--------------
* Versioning a mobile application to alert the user of an update.

Quick start
-----------

1. Building & Installing::

    cd django-keyval_settings/
    python[3] setup.py sdist
    cd ..
    pip install django-keyval_settings

2. Add "keyval_settings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'keyval_settings',
        ...
    )

3. Include the keyval_settings URLconf in your project urls.py like this:: 

    url(r'^settings/', include('keyval_settings.urls')),

4. Run :code:`python manage.py migrate` to create the keyval_settings models.

5. Start the development server and visit http://127.0.0.1:8000/admin/ to start creating settings.

6. Visit http://127.0.0.1:8000/settings/ to see a dictionary of the settings.


In Code Usage
-------------
Settings *are* just normal models. This app includes some helper functions.

.. code-block:: python

    from keyval_settings.models import Setting

    Setting.create('ios_update_available', True).save()
    Setting.get('ios_update_available')  # True

    Setting.create('andriod_update_available', 'false').save()
    Setting.get('andriod_update_available')  # False

