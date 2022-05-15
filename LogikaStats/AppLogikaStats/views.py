from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
# from .form import RegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import*

# Create your views here.
# функция деавторизации
def logoutUser(request):
    logout(request)
    return redirect("login")
#
class RegisterUser(TemplateView):
    template_name = "appLogikaStats/registration.html"
    errortext = 0
    #
    def dispatch(self, request):
        #
        try:
            #
            if request.method == "POST":
                username = request.POST.get("user_name") #
                password1 = request.POST.get("password_1") #
                password2 = request.POST.get("password_2") #
                if password1 == password2: #
                    User.objects.create_user(username, password1, password2) #
                    self.errortext = 0 #
                    return redirect("login") #
                else: #
                    self.errortext = "Пароли не совпадают!" #
        except:
            self.errortext = "Данные введены некоректно!!!" #
        #
        return render(request, self.template_name, context= {"errortext": self.errortext})
#
class LoginView(TemplateView):
    template_name = "appLogikaStats/login.html"
    #
    def dispatch(self, request):
        context = {}
        #
        if request.method == "POST":
            username = request.POST.get("user_name")
            password1 = request.POST.get("password_1")
            #
            user = authenticate(request, username = username, password = password1)
            if user is not None:
                #
                login(request, user)
                #
                return redirect("home") 
            else:
                #
                context["errortext"] = "Введенный логин или пароль не верны. ЛУзер !!!"
        #
        return render(request, self.template_name, context)
#
def getBase(request):
    return render(request, 'appLogikaStats/base.html', context = None) 

def getHome(request):
    # Словарь всех принемаемых параметров
    data = BasicData.objects.all()
    context = {
                "h1": "Головна",
                "title": "Home",
                "data": data
            }
    return render(request, 'appLogikaStats/home.html', context= context)

def getCours(request):
    # Словарь всех принемаемых параметров
    context = {
                "h1": "Мій курс",
                "title": "My Course"
            }
    return render(request, 'appLogikaStats/mycours.html', context= context)

def getProfile(request):
    context = {
                "h1": "Мій профіль",
                "title": "Мій профіль"
            }
    return render(request, 'appLogikaStats/profile.html', context= context)



# class RegisterUser(CreateView):
#     form_class = RegistrationForm
#     template_name = "appLogikaStats/registration.html"
#     success_url = reverse_lazy('home')
#     # def get_context_data(self,**kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context["form"] = RegisterUser.form_class
#     #     return context
