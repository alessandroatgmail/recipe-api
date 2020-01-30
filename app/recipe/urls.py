from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tag', views.TagViewSets)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns =[
    path('', include(router.urls)),
    # path('', include(router.urls))

]
