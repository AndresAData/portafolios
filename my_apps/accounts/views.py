from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# 🔐 LOGIN
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True  # si ya está logueado, lo redirige

    def get_success_url(self):
        return reverse_lazy("portafolios:home")  # ajusta a tu ruta principal


# 🚪 LOGOUT
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")  # a dónde va después de salir


# 🧑‍💻 SIGNUP
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Auto login después de registrarse (opcional)
        login(self.request, self.object)
        return response