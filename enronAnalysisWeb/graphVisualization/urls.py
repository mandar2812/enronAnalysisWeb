from django.conf.urls.defaults import *
from views import *
urlpatterns = ()
urlpatterns = patterns('graphVisualization.views',
                       (r'/admin','django.contrib.admin'),
                       (r'/(\w+)/','detail'),
                       (r'','index')
)
