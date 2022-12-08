from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from .models import Link

client = Client()


class BaseLinkTest(TestCase):
    def setUp(self):
        self.data = {"url": "https://xyz.com", "upvotes": 7, "downvotes": 3}
        self.link = Link.objects.create(**self.data)


class LinkTest(BaseLinkTest):
    def test_post_new_url(self):
        url = {"url": "https://abc.com"}
        response = client.post(
            reverse("links"), data=url, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["message"], "Link object is created successfully"
        )

    def test_post_existing_url(self):
        response = client.post(
            reverse("links"), data=self.data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["url"][0], "link with this url already exists."
        )

    def test_link_score(self):
        score = self.data["upvotes"] - self.data["downvotes"]
        self.assertEqual(self.link.score, score)


class LinkUpVoteTest(BaseLinkTest):
    def test_upvote_url(self):
        response = client.post(
            reverse("upvote", kwargs={"pk": str(self.link.id)}),
            data=self.data,
            content_type="application/json",
        )
        link_after_upvote = Link.objects.get(url=self.data["url"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(link_after_upvote.upvotes, self.data["upvotes"] + 1)


class LinkDownVoteTest(BaseLinkTest):
    def test_downvote_url(self):
        response = client.post(
            reverse("downvote", kwargs={"pk": str(self.link.id)}),
            data=self.data,
            content_type="application/json",
        )
        link_after_downvote = Link.objects.get(url=self.data["url"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(link_after_downvote.downvotes, self.data["downvotes"] + 1)
