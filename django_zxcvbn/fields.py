from django.forms import CharField, PasswordInput

from django_zxcvbn.validators import length_validator, zxcvbn_validator

class PasswordField(CharField):
    default_validators = [length_validator, zxcvbn_validator ]

    def __init__(self, *args, **kwargs):
        if not kwargs.has_key("widget"):
            kwargs["widget"] = PasswordInput(render_value=False)
        
        super(PasswordField, self).__init__(*args, **kwargs)