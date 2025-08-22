from django.shortcuts import render
from django.views import View
from app.models import UserData
from .forms import ContactForm


class HomeView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "home.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохранение данных в базу данных
            UserData.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                message=form.cleaned_data["message"],
            )
            return render(request, "success.html")
        return render(request, "home.html", {"form": form})


class XabarView(View):
    def get(self, request):
        xabarlar = UserData.objects.all()
        return render(request, "table_form.html", {"xabarlar": xabarlar})
