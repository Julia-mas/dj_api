from rest_framework import routers
from .views import ScheduleView

router = routers.DefaultRouter()
router.register('schedule_list', ScheduleView)

urlpatterns = router.urls
