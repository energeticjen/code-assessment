from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserForm
from .models import User

class HomeView(generic.FormView):
    template_name = "signup/home.html"
    form_class = UserForm

class SubmitView(generic.CreateView):
    form_class = UserForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('signup:confirm')


class ConfirmView(generic.View):
    template_name = "signup/confirm.html"

    def get(self, request):
        user_list = User.objects.order_by("id")
        new_user = User.objects.last()
        context = {
            "new_user": new_user,
            "user_list": user_list
        }
        return render(request, "signup/confirm.html", context)
