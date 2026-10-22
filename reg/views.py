from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

class IndexView(TemplateView):
    template_name="reg/index.html"

class RegisterView(CreateView):
    form_class=UserCreationForm
    template_name="reg/register.html"
    success_url=reverse_lazy("login")

    def get_form(self, form_class =None ):
        form=super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["class"]="form-control"
        return form

class LoginView(LoginView):
    template_name="reg/login.html"
    next_page = reverse_lazy("dashboard")

class DashboardView(TemplateView):
    template_name="reg/dashboard.html"

