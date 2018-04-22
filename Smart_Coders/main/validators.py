from django.core.exceptions import ValidationError




curse_list = ["غبي"]


def validate_title(value):
    if value in curse_list:
        raise ValidationError("{}:  ليست كلمة مقبولة".format(value))


def validate_num_slug(value):
    if value < 1 or value > 3:
        raise ValidationError("الرقم {} لا يقابل اي نوع من المقالات".format(value))
