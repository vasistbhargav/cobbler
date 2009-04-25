from django.conf.urls.defaults import *
from views import *

# Uncomment the next two lines to enable the admin:
# from cobbler_web.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^cobbler_web/$', index),
    (r'^cobbler_web/ksfile/list(/(?P<page>\d+))?$', ksfile_list),
    (r'^cobbler_web/ksfile/edit$', ksfile_edit, {'editmode':'new'}),
    (r'^cobbler_web/ksfile/edit/(?P<ksfile_name>.+)$', ksfile_edit, {'editmode':'edit'}),
    (r'^cobbler_web/ksfile/save$', ksfile_save),
    (r'^cobbler_web/(?P<what>\w+)/list?(/sort/(?P<sort_field>[!\w]+))?(/limit/(?P<limit>\w+))?(/page/(?P<page>\d+))?$', list),
    (r'^cobbler_web/(?P<what>\w+)/search$', search),
    (r'^cobbler_web/(?P<what>\w+)/dosearch?(/sort/(?P<sort_field>[!\w]+))?(/limit/(?P<limit>\w+))?(/page/(?P<page>\d+))?$', dosearch),
    (r'^cobbler_web/distro/edit$', distro_edit),
    (r'^cobbler_web/distro/edit/(?P<distro_name>.+)$', distro_edit),
    (r'^cobbler_web/distro/save$', distro_save),
    (r'^cobbler_web/profile/edit$', profile_edit),
    (r'^cobbler_web/profile/edit/(?P<profile_name>.+)$', profile_edit),
    (r'^cobbler_web/subprofile/edit$', profile_edit, {'subprofile': 1}),
    (r'^cobbler_web/profile/save$', profile_save),
    (r'^cobbler_web/system/edit$', system_edit),
    (r'^cobbler_web/system/edit/(?P<system_name>.+)$', system_edit, {'editmode': 'edit'}),
    (r'^cobbler_web/system/copy/(?P<system_name>.+)$', system_edit, {'editmode': 'copy'}),
    (r'^cobbler_web/system/rename/(?P<system_name>[\w\-]+)$', system_rename),
    (r'^cobbler_web/system/rename/(?P<system_name>[\w\-]+)/(?P<system_newname>[\w\-]+)$', system_rename),
    (r'^cobbler_web/system/save$', system_save),
    (r'^cobbler_web/system/(?P<multi_mode>[\w\-]+)/multi$', system_multi),
    (r'^cobbler_web/system/(?P<multi_mode>[\w\-]+)/domulti$', system_domulti),
    (r'^cobbler_web/repo/edit$', repo_edit),
    (r'^cobbler_web/repo/edit/(?P<repo_name>.+)$', repo_edit),
    (r'^cobbler_web/repo/save$', repo_save),
    (r'^cobbler_web/image/edit$', image_edit),
    (r'^cobbler_web/image/edit/(?P<image_name>.+)$', image_edit),
    (r'^cobbler_web/image/save$', image_save),
    (r'^cobbler_web/random_mac$', random_mac),
    (r'^cobbler_web/random_mac/virttype/(?P<virttype>.+)$', random_mac),
    (r'^cobbler_web/settings$', settings),
    (r'^cobbler_web/sync$', dosync),
)
