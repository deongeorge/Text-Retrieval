from text.viewsets import TextViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('text', TextViewset)

