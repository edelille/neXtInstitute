from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Question, Choice

'''

DEFAULT

TO REPLACE WITH SEARCH RESULTS FOR PUBLICATIONS


'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'main/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/detail.html', {'question': question})

def results(request, question_id):
    choices = get_list_or_404(Choice, pk=question_id)
    return render(request, 'main/results.html', {'choices': choices})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)