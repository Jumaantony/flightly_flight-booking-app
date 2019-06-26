import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not re.search(r'\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class ContainsUppercaseValidator:
    def validate(self, password, user=None):
        if not re.search('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class ContainsLowercaseValidator:
    def validate(self, password, user=None):
        if not re.search('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class ContainsSymbolValidator:
    def validate(self, password, user=None):
        if not re.search(r'[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("This password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            r"()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
