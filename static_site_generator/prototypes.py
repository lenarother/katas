import sys

from django.conf import settings
from django.core.management import execute_from_command_line


settings.configure(
    DEBUG=True,
    SECRET_KEY='verysecret',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,	
        },
    ),
    STATIC_URL='/static/',
)


if __name__ == '__main__':
     execute_from_command_line(sys.argv)
