"""
choices used in core models.
"""


class GENDER:
    """
    address type choice options
    """
    MALE = 1
    FEMALE = 2

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'))


class ROLES:
    """
    Available Roles
    """
    USER = 1

    CHOICES = ((USER, 'USER'),)
