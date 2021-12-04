from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from codeInOne_API.quickstart.serializers import ChallengeSerializer
from codeInOne_API.quickstart.models import Challenge

class ChallengeViews(APIView):
    def post(self, request):
        serializer = ChallengeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        serializer_context = {
            'request': request
        }

        if id:
            item = Challenge.objects.get(id=id)
            serializer = ChallengeSerializer(item, context = serializer_context)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Challenge.objects.all()
        serializer = ChallengeSerializer(items, many=True, context = serializer_context)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = Challenge.objects.get(id=id)
        serializer = ChallengeSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):
        item = get_object_or_404(Challenge, id=id)
        item.delete()
        return Response({"status": "success", "data": "Challenge Deleted"})