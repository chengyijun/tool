# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def post(self, request, *args, **kwargs):
        print(request)
        print(request.FILES)
        file = request.FILES.get('file')
        print(file.__dict__)
        with open(f'uploads/{file._name}', 'wb') as f:
            for ck in file.chunks():
                f.write(ck)
        print(f'{file._name} 上传成功！')
        return Response({
            'code': 1,
            'message': f'{file._name} 上传成功！'
        })
