Django Passwords
================

django-zxcvbn brings a zxcvbn password strength validator to Django.

What is zxcvbn?
---------------

It's a realistic password strength estimator.

https://tech.dropbox.com/2012/04/zxcvbn-realistic-password-strength-estimation/

So many websites either permit crappy passwords, or impose rules that enforce crappy passwords. This library is to promote a better way.


Installation
------------

You can install django-zxcvbn with pip by typing::

    pip install django-zxcvbn
    
Or with easy_install by typing::

    easy_install django-zxcvbn
    
Or manually by downloading a tarball and typing::

    python setup.py install

Or via pip and git with::

    pip install -e git://github.com/piran/django-zxcvbn.git#egg=django-zxcvbn

Requirements
------------

    pip install -e git://github.com/rpearl/python-zxcvbn.git#egg=zxcvbn
    
Settings
--------

django-zxcvbn adds 3 optional settings

Optional:
    Specifies minimum length for passwords::

        PASSWORD_MIN_LENGTH = 8 # Defaults to 8

    Specifies maximum length for passwords::

        PASSWORD_MAX_LENGTH = 128 # Defaults to 128 since this is max_length in contrib.auth

    Specifies a list of common sequences to attempt to match a password against::

        PASSWORD_MIN_ENTROPY = 25 # defaults to a pragmatic 25


Usage
-----

    Use in your signup form like this:

        from django import forms
        from django_zxcvbn.fields import PasswordField

        class ExampleForm(forms.Form):
            password = PasswordField(label="Password")

Javascript
----------

For convenience the zxcvbn javascript is included in this package (using contrib.static)

    <script type="text/javascript" src="zxcvbn-async.js">
    </script>

zxcvbn-async in turn loads the full zxcvbn library from dropbox.

zxcvbn adds a single function to the global namespace:

zxcvbn(password, user_inputs)

It takes one required argument, a password, and returns a result object.
The result includes a few properties:

result.entropy            # bits

result.crack_time         # estimation of actual crack time, in seconds.

result.crack_time_display # same crack time, as a friendlier string:
                          # "instant", "6 minutes", "centuries", etc.

result.score              # [0,1,2,3,4] if crack time is less than
                          # [10**2, 10**4, 10**6, 10**8, Infinity].
                          # (useful for implementing a strength bar.)

result.match_sequence     # the list of patterns that zxcvbn based the
                          # entropy calculation on.

result.calculation_time   # how long it took to calculate an answer,
                          # in milliseconds. usually only a few ms.

The optional user_inputs argument is an array of strings that zxcvbn
will add to its internal dictionary. This can be whatever list of
strings you like, but is meant for user inputs from other fields of the
form, like name and email. That way a password that includes the user's
personal info can be heavily penalized. This list is also good for
site-specific vocabulary.

When zxcvbn loads (after the async script fetch is complete), it'll
check if a function named zxcvbn_load_hook is defined, and run it with
no arguments if so. Most sites shouldn't need this.

For full usage instructions see: https://github.com/lowe/zxcvbn


Acknowledgments
---------------

My work in bringing this to life was minimal, thanks to all these awesome people:

Ryan Pearl, creator the excellent python implementation of zxcvbn, https://github.com/rpearl/python-zxcvbn

Donald Stufft, who's django-passwords app was the starting point for this project:
https://github.com/dstufft/django-passwords/

Dropbox, for supporting independent projects both inside and
outside of hackweek.

Dan Wheeler (https://github.com/lowe) for the CoffeeScript implementation
(see above.) To repeat his outside acknowledgements (which remain useful, as always):

Many thanks to Mark Burnett for releasing his 10k top passwords list:
http://xato.net/passwords/more-top-worst-passwords
and for his 2006 book,
"Perfect Passwords: Selection, Protection, Authentication"

Huge thanks to Wiktionary contributors for building a frequency list
of English as used in television and movies:
http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

Last but not least, big thanks to xkcd :)
https://xkcd.com/936/


Redistribution
--------------

zxcvbn lives at https://github.com/lowe/zxcvbn

The zxcvbn js library is redistributed under the terms of this license:

Copyright (c) 2012 Dropbox, Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


BSD License
-----------

django-zxcvbn is made available under the BSD license

Copyright (c) 2012 Piran Digital Pty Ltd

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.