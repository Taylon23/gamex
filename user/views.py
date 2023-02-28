from django.views.generic import CreateView, UpdateView
from .models import Perfil
from .forms import UserResisterForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class UserCreate(CreateView):
    template_name = 'UserResister.html'
    success_url = reverse_lazy('home')
    form_class = UserResisterForm

    def form_valid(self, form):
        url = super().form_valid(form)

        Perfil.objects.filter(user=self.object)

        return url


class PerfilUpdate(UpdateView):
    model = Perfil
    template_name = 'PerfilUpdate.html'
    success_url = reverse_lazy('perfil')

    def get_object(self,queryset=None):
        self.object = get_object_or_404(Perfil,user=self.request.user)

        return self.object

# Create your views here.
