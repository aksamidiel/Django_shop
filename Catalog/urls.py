from django.urls import path
from .views import *

urlpatterns = [
    path('author/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('binding/<int:pk>', BindingDetail.as_view(), name='binding_detail'),
    path('format/<int:pk>', FormatDetail.as_view(), name='format_detail'),
    path('genre/<int:pk>', GenreDetail.as_view(), name='genre_detail'),
    path('publish/<int:pk>', PublishDetail.as_view(), name='publish_detail'),
    path('serie/<int:pk>', SerieDetail.as_view(), name='serie_detail'),

    path('author/', AuthorList.as_view(), name='author_list'),
    path('binding/', BindingList.as_view(), name='binding_list'),
    path('format/', FormatList.as_view(), name='format_list'),
    path('genre/', GenreList.as_view(), name='genre_list'),
    path('publish/', PublishList.as_view(), name='publish_list'),
    path('serie/', SerieList.as_view(), name='serie_list'),

    #create_field
    path('Create/Genre_Create', Genre_Create.as_view(), name='genre_create'),
    path('Create/Serie_Create', Serie_Create.as_view(), name='serie_create'),
    path('Create/Binding_Create', Binding_Create.as_view(), name='binding_create'),
    path('Create/Publish_Create', Publish_Create.as_view(), name='publish_create'),
    path('Create/Format_Create', Format_Create.as_view(), name='format_create'),
    path('Create/Author_Create', Author_Create.as_view(), name='author_create'),


    #update fields
    path('Update/Genre_Update', Genre_Update.as_view(), name='genre_update'),
    path('Update/Serie_Update', Serie_Update.as_view(), name='serie_update'),
    path('Update/Binding_Update', Binding_Update.as_view(), name='binding_update'),
    path('Update/Publish_Update', Publish_Update.as_view(), name='publish_update'),
    path('Update/Format_Update', Format_Update.as_view(), name='format_update'),
    path('Update/Author_Update', Author_Update.as_view(), name='author_update'),


]
