from api.v1 import views
from rest_framework.routers import SimpleRouter

urlpatterns = []

router = SimpleRouter()
router.register(r'banks/bank', views.BankViewSet)
router.register(r'banks/debitcard', views.DebitCardViewSet)
router.register(r'banks/creditcard', views.CreditCardViewSet)
router.register(r'banks/autocredit', views.AutoCreditViewSet)
router.register(r'banks/consumercredit', views.ConsumerCreditViewSet)
router.register(r'banks/deposit', views.DepositViewSet)
router.register(r'banks/branch', views.BranchViewSet)
router.register(r'banks/rating', views.RatingViewSet)
urlpatterns += router.urls
