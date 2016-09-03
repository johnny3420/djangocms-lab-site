import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
"""
Django settings for cms_lab_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Application definition
ROOT_URLCONF = 'cms_lab_site.urls'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'cms_lab_site', 'static'),
)
SITE_ID = 1

# Django Pipeline config
# http://django-pipeline.readthedocs.org/en/1.4.7/
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_CSS = {
    'site': {
        'source_filenames': (
            'cms_lab_site/css/main.css',
            'cms_lab_site/css/nav.css',
            'cms_lab_site/css/genome-browser.css',
            'cms_lab_site/css/lab-members.css',
            'cms_lab_site/css/shiny-app.css',
        ),
        'output_filename': 'css/site.css',
    },
    'vendor': {
        'source_filenames': (
            'bower_components/bootstrap/dist/css/bootstrap.css',
        ),
        'output_filename': 'css/vendor.css',
    }
}
PIPELINE_JS = {
    'site': {
        'source_filenames': (
            'cms_lab_site/js/nav.js',
        ),
        'output_filename': 'js/site.js',
    },
    'vendor': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/vendor.js',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'cms_lab_site.context_processors.lab_settings',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'cms_lab_site', 'templates'),
)

DEFAULT_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
)

THIRD_PARTY_APPS = (
    'cms',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_teaser',
    'djangocms_video',
    'menus',
    'pipeline',
    'reversion',
    'sekizai',
    'treebeard',
    'easy_thumbnails',
    'filer',
    'mptt',
    'friendlytagloader',
    'taggit',
    'colorfield',
)

LOCAL_APPS = (
    'cms_lab_site',
    'lab_members',
    'cms_lab_members',
    'cms_shiny',
    'cms_lab_carousel',
    'cms_lab_data',
    'cms_lab_publications',
    'cms_genome_browser',
    'system_maintenance',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LANGUAGES = (
    ## Customize this
    ('en-us', gettext('en-us')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'hide_untranslated': False,
            'code': 'en-us',
            'redirect_on_fallback': True,
            'public': True,
            'name': gettext('en-us'),
        },
    ],
    'default': {
        'hide_untranslated': False,
        'public': True,
        'redirect_on_fallback': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('genome-browser.html', 'Genome Browser'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'filer': 'filer.migrations_django',
}

# For easy_thumbnails to support retina displays (recent MacBooks, iOS)
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_QUALITY = 95
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
THUMBNAIL_SUBDIR = 'versions'

# Custom lab settings
LAB_NAME = 'Maloof Lab'


# Pre-populate placeholder content
CMS_PLACEHOLDER_CONF = {
    'research interests': {
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':"<p><em>[Enter 'Edit Mode' and double-click here to add your research interests.]</em></p>",
                },
            },
        ],
    },
    'personal interests': {
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':"<p><em>[Enter 'Edit Mode' and double-click here to add your personal interests.]</em></p>",
                },
            },
        ],
    },
    'scientist sidebar': {
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':"<p><em>[Enter 'Edit Mode' and double-click here to add sidebar content.]</em></p>",
                },
            },
        ],
    },
}

CKEDITOR_SETTINGS = {
    'disableNativeSpellChecker': False,
    'removePlugins': 'contextmenu,liststyle,tabletools',
    'skin': 'bootstrapck',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['Find', 'Replace', '-', 'Scayt'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-',
            'TextColor', 'BGColor', '-', 'RemoveFormat'],
        ['Format', 'Styles'],
        ['Source', '-', 'ShowBlocks', '-', 'Maximize'],
        '/',
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
            'Blockquote', '-', 'Table', '-', 'HorizontalRule'],
        ['cmsplugins'],
    ],
}
