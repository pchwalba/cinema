from django.urls import path, include
from .views import (CreateMovie, UpdateMovie, MovieDetail, CreateScreening, ScreeningDetail,
                    MovieList, TicketLatest, SearchView, MovieListAll)
from . import api_views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'ticket', api_views.TicketViewSet)

urlpatterns = [path('', MovieList.as_view(), name='index'),
               path('all_movies/', MovieListAll.as_view(), name='movie_list'),
               path('api/ticket/<int:sc_pk>/', api_views.TicketViewSet.as_view({'get': 'list'})),
               path('api/', include((router.urls, 'api'))),
               path('create_movie/', CreateMovie.as_view(), name='create_movie'),
               path('edit_movie/<int:pk>', UpdateMovie.as_view(), name='update_movie'),
               path('movie/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
               path('movie/<int:movie_pk>/screening_create/', CreateScreening.as_view(), name='screening_create'),
               path('screening/<int:pk>', ScreeningDetail.as_view(), name='screening_detail'),
               path('ticket/<int:pk>', TicketLatest.as_view(), name='ticket'),
               path('search/', SearchView.as_view(), name='search_view'),
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
