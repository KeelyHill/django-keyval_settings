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

1. Add "keyval-settings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'keyval-settings',
        ...
    )

2. Include the keyval-settings URLconf in your project urls.py like this:: 
    :code:`url(r'^settings/', include('keyval-settings.urls')),`

3. Run `python manage.py migrate` to create the keyval-settings models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to start creating settings.

5. Visit http://127.0.0.1:8000/settings/ to see a dictionary of the settings.


In Code Usage
-------------
Settings *are* just normal models. This app includes some helper functions.

.. code-block:: python

    from keyval_settings.models import Setting

    Setting.create('ios_update_available', True)
    Setting.get('ios_update_available')  # True

    Setting.create('andriod_update_available', 'false')
    Setting.get('andriod_update_available')  # False

