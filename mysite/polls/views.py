from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class DetailView(LoginRequiredMixin ,generic.DetailView):
    model = Question
    template_name= "polls/detail.html"
    
    login_url='/polls/login/'

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question form
        return render(request,"polls/detail.html", {"question": question, "error_message": "you didn't select a choice!"})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after succesfully dealing with PostData
        # This prevents data from being posted twice if a user hits the Back button
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def registration(request):
    context={}
    return render(request, "polls/register.html",context)

def register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    user = User.objects.create_user(username, email, password)
    user.save()

    login(request, user)

    return HttpResponseRedirect(reverse("polls:index"))

def loginForm(request):
    context= {}
    return render(request, "polls/login.html", context)

def authenticateUser(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("polls:index"))
    else:
        return render(request,"polls/login.html", {"error_message": "Username or password incorrect"})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("polls:index"))
