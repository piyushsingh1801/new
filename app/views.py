from .models import Song
from .serializers import SongsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SongsView(APIView):

    def get(self,request,id=None):

        if id is not None:
            media = Song.objects.get(id=id)
            serializer = SongsSerializer(media)
            return Response(serializer.data,status=status.HTTP_200_OK)
        media = Song.objects.all()
        serializer = SongsSerializer(media,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = SongsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Status':"Posted/Created successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({'Status':"Unable to post successfully"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        media = Song.objects.get(id=id)
        serializer = SongsSerializer(media,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Status':"Updated successfully"},status=status.HTTP_200_OK)

        return Response({'Status':"Unable to update"},status = status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        media = Song.objects.get(id=id)
        if media:
            media.delete()
            return Response({'msg':'record deleted of given id'},status = status.HTTP_204_NO_CONTENT)
        else:
            return Response({'Status':"Record not found with given id"},status = status.HTTP_404_NOT_FOUND)
