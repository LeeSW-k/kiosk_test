
from django.shortcuts import render
from face_kakao import face
from rest_framework.views import APIView



class faceAPI(APIView):
    def get(self, request):
        # 얼굴인식
        face_age, face_gneder = face()

        if(face_age> 0 and face_age<10 ):
            return render(request,'kiosk_test/main.html')
        elif (face_age >= 10 and face_age < 20):
            return render(request, 'kiosk_test/10.html')
        elif (face_age >= 20 and face_age < 30):
            return render(request, 'kiosk_test/20.html')
        else:
            return render(request, 'kiosk_test/else.html')

class pay(APIView):
    def get(self, request):
        return render(request, 'kiosk_test/pay.html')

class main(APIView):
    def get(self,request):
        return render(request, 'kiosk_test/main.html')
