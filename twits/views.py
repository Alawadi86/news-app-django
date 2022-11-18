from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .forms import CommentForm
from .models import Twit

class TwitListView(LoginRequiredMixin, ListView):
    model = Twit
    template_name ="twit_list.html"

class CommentGet(DetailView):
    model = Twit
    template_name = "twit_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Twit
    form_class = CommentForm
    template_name = "twit_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.twit = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk":twit.pk})
    
    

class TwitDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, **args, **kwargs)



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


class TwitLikeView(LoginRequiredMixin, View):
    """ Twit like view """

    def get(self, request, *args, **kwargs):

        """Get Request """
        # Get out the data from the GET request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":

            # Do like stuff
            twit.likes.add(request.user)
          
        else:
            # Do unlike stuff
            twit.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )

     
