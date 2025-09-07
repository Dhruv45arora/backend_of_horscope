from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, UserSerializer
import requests

User = get_user_model()

# REGISTER
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# LOGIN
class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

# HOROSCOPE
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import requests

class HoroscopeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get data from request body
        name = request.data.get("name")
        Date_of_birth = request.data.get("Date_of_birth")
        Month_of_birth = request.data.get("Month_of_birth")
        year_of_birth = request.data.get("year_of_birth")
        time_of_birth = request.data.get("time_of_birth")
        zodiac_sign = request.data.get("zodiac_sign")
        time = request.data.get("time", "23:00")  # default to 23:00 if not provided

        # Prepare the payload for n8n webhook
        payload = {
            "name": name,
            "Date_of_birth": Date_of_birth,
            "Month_of_birth": Month_of_birth,
            "year_of_birth": year_of_birth,
            "time_of_birth": time_of_birth,
            "zodiac_sign": zodiac_sign,
            "time": time
        }

        webhook_url = "https://dooruv.app.n8n.cloud/webhook-test/b000a034-0e0b-4649-96fa-43ddeba21196"

        try:
            r = requests.post(webhook_url, json=payload, timeout=10)
            r.raise_for_status()  # Raise an exception for HTTP errors
            result = r.json()      # Parse the JSON response
        except requests.exceptions.RequestException as e:
            result = {"error": f"Request failed: {str(e)}"}
        except ValueError:
            result = {"error": "Invalid JSON response from webhook"}

        return Response({"horoscope": result})