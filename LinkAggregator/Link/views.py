# from django.shortcuts import render
from django.http.response import Http404

# from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Link
from .serializers import LinkSerializer


class BaseLinkAPIView(APIView):
    # Get a Link object
    def get_object(self, pk):
        try:
            return Link.objects.get(pk=pk)
        except Link.DoesNotExists:
            raise Http404


class LinkAPIView(BaseLinkAPIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = LinkSerializer(data)
        else:
            data = Link.objects.all().order_by("-score")
            serializer = LinkSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = LinkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "message": "Link object is created successfully",
            "serializer": serializer.data,
            "status": status.HTTP_200_OK,
        }
        return response


class LinkUpVoteAPIView(BaseLinkAPIView):

    # upvotes the link
    def post(self, request, pk, format=None):
        link = self.get_object(pk)
        link.upvotes += 1
        link.save()
        response = Response()
        response.data = {
            "message": "Link object is upvoted successfully",
            "status": status.HTTP_200_OK,
        }
        return response


class LinkDownVoteAPIView(BaseLinkAPIView):

    # downvotes the link
    def post(self, request, pk=None, format=None):
        link = self.get_object(pk)
        link.downvotes += 1
        link.save()
        response = Response()
        response.data = {
            "message": "Link object is downvoted successfully",
            "status": status.HTTP_200_OK,
        }
        return response
