from django.contrib import auth
from Middlewares_ORM.backend import auth_backend


class AuthMiddleware:

    def process_request(self, request):
        print("Middleware executed")
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            request.user = auth_backend.AuthBackend.authenticate(email, password)

        return None
