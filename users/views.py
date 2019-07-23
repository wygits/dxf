from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import Student
from .serializers import StudentSerializer

@csrf_exempt
def QueryStudent(request):
    """
    API endpoint that allows users to be viewed or edited.
    """
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many= True)
    return JsonResponse(serializer.data,safe=False)

