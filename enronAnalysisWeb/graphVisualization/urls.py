from django.conf.urls.defaults import *
urlpatterns = patterns('graphVisualization.views',
                       (r'/admin','django.contrib.admin'),
                       (r'/(\w+)/','detail'),
                       (r'','index'),
)
