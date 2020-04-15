"""
"""
from django.utils.translation import gettext_lazy as _

OSCAR_SHOP_NAME = 'Gurukul Sankalp'
OSCAR_SHOP_TAGLINE = 'Tagline should come here'

# Basket settings
OSCAR_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
OSCAR_BASKET_COOKIE_OPEN = 'oscar_open_basket'
OSCAR_BASKET_COOKIE_SECURE = False
OSCAR_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
OSCAR_RECENTLY_VIEWED_COOKIE_NAME = 'oscar_history'
OSCAR_RECENTLY_VIEWED_COOKIE_SECURE = False
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20

# Currency
OSCAR_DEFAULT_CURRENCY = 'INR'

# Paths
OSCAR_IMAGE_FOLDER = 'images/products/%Y/%m/'
OSCAR_DELETE_IMAGE_FILES = True


# Copy this image from oscar/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
OSCAR_MISSING_IMAGE_URL = 'image_not_found.jpg'
OSCAR_UPLOAD_ROOT = '/tmp'

# Reviews
OSCAR_ALLOW_ANON_REVIEWS = True
OSCAR_MODERATE_REVIEWS = False

# Checkout
OSCAR_ALLOW_ANON_CHECKOUT = False

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'

OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Complete', 'Cancelled',),
    'Cancelled': (),
    'Complete': (),
}
OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Cancelled': 'Cancelled',
    'Complete': 'Shipped',
}

LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

#from django.contrib.messages import constants as messages
#MESSAGE_TAGS = {
#    messages.ERROR: 'danger'
#}
#OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
#OSCAR_ALLOW_ANON_CHECKOUT = False
DISPLAY_VERSION = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Registration
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'oscar@example.com'

# Menu structure of the dashboard navigation
OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Product Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Product Types Options'),
                'url_name': 'dashboard:catalogue-option-list',
            },
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },

            #{
            #    'label': _('Ranges'),
            #    'url_name': 'dashboard:range-list',
            #},

        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Notify Me  requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    #{
    #    'label': _('Offers'),
    #    'icon': 'icon-bullhorn',
    #    'children': [
    #        {
    #            'label': _('Offers'),
    #            'url_name': 'dashboard:offer-list',
    #        },
    #        {
    #            'label': _('Vouchers'),
    #            'url_name': 'dashboard:voucher-list',
    #        },
    #        {
    #            'label': _('Voucher Sets'),
    #            'url_name': 'dashboard:voucher-set-list',
    #        },
    #
    #    ],
    #},
    #{
    #    'label': _('Content'),
    #    'icon': 'icon-folder-close',
    #    'children': [
    #        {
    #            'label': _('Pages'),
    #            'url_name': 'dashboard:page-list',
    #        },
    #        {
    #            'label': _('Email templates'),
    #            'url_name': 'dashboard:comms-list',
    #        },
    #        {
    #            'label': _('Reviews'),
    #            'url_name': 'dashboard:reviews-list',
    #        },
    #    ]
    #},
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]
