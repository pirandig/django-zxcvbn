from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import zxcvbn

# Settings
PASSWORD_MIN_LENGTH = getattr(settings, "PASSWORD_MIN_LENGTH", 8)   # This is a sensible minimum
PASSWORD_MAX_LENGTH = getattr(settings, "PASSWORD_MAX_LENGTH", 128) # Django auth user model is max_length 128
PASSWORD_MIN_SCORE = getattr(settings, "ZXCVBN_MIN_SCORE", 2)

class LengthValidator(object):
    message = _("Password must be between %s and %s chars" % (PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH))
    code = "length"

    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        if self.min_length and len(value) < self.min_length:
            raise ValidationError(
                self.message % _("Must be %s characters or more") % self.min_length,
                code=self.code)
        elif self.max_length and len(value) > self.max_length:
            raise ValidationError(
                self.message % _("Must be %s characters or less") % self.max_length,
                code=self.code)

class ZXCVBNValidator(object):
    message = _("Passwords must be at least %s characters and of sufficient complexity")
    code = "zxcvbn"

    def __call__(self,value):
        res = zxcvbn.password_strength(value)
        if res.get('score') < PASSWORD_MIN_SCORE:
            raise ValidationError(
                self.message % _("Password is too weak"),
                code=self.code)


length_validator = LengthValidator(PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH)
zxcvbn_validator = ZXCVBNValidator()
