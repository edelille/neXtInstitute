from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#part 4
class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'main/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'main/results.html'


# Views destined by Ramy

#Principal Investigator | Teaching | Research | Service | Statement | Photos | Links

class PrincipalInvestigatorView(TemplateView):
    template_name = 'main/principal_investigator.html'

class TeachingView(TemplateView):
    template_name = 'main/teaching.html'

class ResearchView(TemplateView):
    template_name = 'main/research.html'

class ServiceView(TemplateView):
    template_name = 'main/service.html'

class StatementView(TemplateView):
    template_name = 'main/statement.html'

class PhotosView(TemplateView):
    template_name = 'main/photos.html'

class LinksView(TemplateView):
    template_name = 'main/links.html'
