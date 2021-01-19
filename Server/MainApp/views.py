from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import *
from .models import *



class Add(APIView):
    def post(self, request):
        data = request.data.get("data")
        serializer = RecordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()

        return Response({"data": "OK"})

class Get(APIView):
    def get(self, request): 
        data = Records.objects.all().order_by('-score')
        records, n = {}, 1
        for i in data:
            records.update({n: {'player': i.player, 'score': i.score}})
            n += 1
            if n > 7:
                break
        return Response(records)