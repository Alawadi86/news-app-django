from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Twit

class TwitListView(LoginRequiredMixin, ListView):
    model = Twit
    template_name ="twit_list.html"

class TwitDetailView(DetailView):
    model = Twit
    template_name ="twit_detail.html"


class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Twit
    fields = (
        "body",
        "image",
    )
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TwitDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Twit
    template_name ="twit_delete.html"
    success_url = reverse_lazy("twit_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitCreateView(LoginRequiredMixin, CreateView):
    model = Twit
    template_name ="twit_new.html"
    fields = (
        # how to add the image here  
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
