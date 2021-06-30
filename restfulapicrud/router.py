from perfumeapi.viewsets import PerfumeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('perfumes', PerfumeViewset)

# localhost:p/api/