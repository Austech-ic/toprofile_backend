from django.urls import path,re_path
from .views import (
    ListingCategoryApiView,
    SingleHomePageAPiView,
    SingleAboutAPiView,
    SingleBlogApiView,
    SingleCategoryApiView,
    SingleOurServicesAPiView,
    SinglePrivacyAPiView,SinglePropertyApiView,
    SingleStatementAPiView,SingleTermsofserviceAPiView,
    PrivatePolicyApiView,
    StatmentApiView,
    TermsOfServiceApiView,
    BlogApiView,
    AboutApiView,
    HomePageApiView,
    PropertyApiView,
    OurServicesApiView,
    OurTeamApiView,
    SingleOurTeamAPiView,
    TestimonyApiView,
    SingleTestimonyApiView,
    FillFormAPiView,
    AgentApiView,
    SingleAgentAPiView
)
urlpatterns = [
    path("category/",ListingCategoryApiView.as_view()),
    path("category/<int:pk>/",SingleCategoryApiView.as_view()),
    path("blog/",BlogApiView.as_view()),
    path("blog/<int:pk>/",SingleBlogApiView.as_view()),
    path("property/",PropertyApiView.as_view()),
    path("property/<int:pk>/",SinglePropertyApiView.as_view()),
    path("about/us/",AboutApiView.as_view()),
    path("about/us/<int:pk>/",SingleAboutAPiView.as_view()),
    path("homepage/",HomePageApiView.as_view()),
    path("homepage/<int:pk>/",SingleHomePageAPiView.as_view()),
    path("our_service/",OurServicesApiView.as_view()),
    path("our_service/<int:pk>/",SingleOurServicesAPiView.as_view()),
    path("privatePolicy/",PrivatePolicyApiView.as_view()),
    path("privatePolicy/<int:pk>/",SinglePrivacyAPiView.as_view()),
    path("statement/",StatmentApiView.as_view()),
    path("statement/<int:pk>/",SingleStatementAPiView.as_view()),
    path("term/of/service/",TermsOfServiceApiView.as_view()),
    path("term/of/service/<int:pk>/",SingleTermsofserviceAPiView.as_view()),
    path("our_team/",OurTeamApiView.as_view()),
    path("our_team/<int:pk>/",SingleOurTeamAPiView.as_view()),
    path("testimony/",TestimonyApiView.as_view()),
    path("testimony/<int:pk>/",SingleTestimonyApiView.as_view()),
    path("fill/form/",FillFormAPiView.as_view),
    path("agent/",AgentApiView.as_view()),
    path("agent/<int:pk>/",SingleAgentAPiView.as_view())
]
