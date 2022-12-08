from django.urls import path

from .views import LinkAPIView, LinkDownVoteAPIView, LinkUpVoteAPIView

urlpatterns = [
    path("", LinkAPIView.as_view(), name="links"),
    path("<int:pk>", LinkAPIView.as_view(), name="link"),
    path("<int:pk>/upvote", LinkUpVoteAPIView.as_view(), name="upvote"),
    path("<int:pk>/downvote", LinkDownVoteAPIView.as_view(), name="downvote"),
]
