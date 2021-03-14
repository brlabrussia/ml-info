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
router.register(r'investments/share', views.ShareViewSet)
router.register(r'investments/bond', views.BondViewSet)
router.register(r'investments/iia', views.IiaViewSet)
router.register(r'investments/mutual', views.MutualViewSet)
router.register(r'insurance/company', views.CompanyViewSet)
router.register(r'finance/person', views.PersonViewSet)
router.register(r'mfo/lender', views.LenderViewSet)
router.register(r'mfo/loan', views.LoanViewSet)
urlpatterns += router.urls
