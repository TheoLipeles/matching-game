from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

SESSION_CONFIGS = [
    dict(
        name='Matching_Game',
        num_demo_participants=1,
        app_sequence=[
            # 'Introduction',
            # 'Introduction_Practice',
            # 'Piece_Rate',
            # 'Piece_Rate_Game',
            # 'Tournament',
            # 'Tournament_Game',
            'Choice',
            'Choice_Game',
            'Choice_II',
            'Investment_Decision',
            'Investment_Decision_Game']
    ),
]

# STATICFILES_DIRS = [
#     path.join(".", "_static/javascript")
# ]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '$n1yiypa)xa!2(q+xcb#-b5os0@8hmur!42-w*nq!mmuk06$c7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'custom_templates']
