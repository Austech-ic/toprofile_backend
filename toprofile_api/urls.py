from django.urls import path,re_path
from .views import (
    SingleAboutAPiView,
    SingleBlogApiView,

    SingleOurServicesAPiView,
    SinglePrivacyAPiView,SinglePropertyApiView,
SingleTermsofserviceAPiView,
    PrivatePolicyApiView,

    TermsOfServiceApiView,
    BlogApiView,
    AboutApiView,
    FeatureSectionApiView,
    SingleFeatureSectionAPiView,
    HeroSectionApiView,
    SingleHeroSectionAPiView,
    AgentMemberApiView,
    SingleAgentMemberAPiView,
    PropertyApiView,
    OurServicesApiView,
    OurTeamApiView,
    SingleOurTeamAPiView,
    TestimonyApiView,
    SingleTestimonyApiView,
    FillFormAPiView,
    AgentApiView,
    SingleAgentAPiView,
    HomeSectionApiView,
    AdminAppearanceApiView
)
urlpatterns = [
    path("home/",HomeSectionApiView.as_view()),
    path("admin_appearence/",AdminAppearanceApiView.as_view()),
    path("blog/",BlogApiView.as_view()),
    path("blog/<int:pk>/",SingleBlogApiView.as_view()),
    path("property/",PropertyApiView.as_view()),
    path("property/<int:pk>/",SinglePropertyApiView.as_view()),
    path("about/us/",AboutApiView.as_view()),
    path("about/us/<int:pk>/",SingleAboutAPiView.as_view()),
    path("our_service/",OurServicesApiView.as_view()),
    path("our_service/<int:pk>/",SingleOurServicesAPiView.as_view()),
    path("privatePolicy/",PrivatePolicyApiView.as_view()),
    path("privatePolicy/<int:pk>/",SinglePrivacyAPiView.as_view()),
    path("term/of/service/",TermsOfServiceApiView.as_view()),
    path("term/of/service/<int:pk>/",SingleTermsofserviceAPiView.as_view()),
    path("our_team/",OurTeamApiView.as_view()),
    path("our_team/<int:pk>/",SingleOurTeamAPiView.as_view()),
    path("testimony/",TestimonyApiView.as_view()),
    path("testimony/<int:pk>/",SingleTestimonyApiView.as_view()),
    path("fill/form/",FillFormAPiView.as_view),
    path("agent/",AgentApiView.as_view()),
    path("agent/<int:pk>/",SingleAgentAPiView.as_view()),
    path("agent_member/",AgentMemberApiView.as_view()),
    path("agent_member/<int:pk>/",SingleAgentMemberAPiView.as_view()),
    path("hero_section/",HeroSectionApiView.as_view()),
    path("hero_section/<int:pk>/",SingleHeroSectionAPiView.as_view()),
    path("feature_section/",FeatureSectionApiView.as_view()),
    path("feature_section/<int:pk>/",SingleFeatureSectionAPiView.as_view()),
]
