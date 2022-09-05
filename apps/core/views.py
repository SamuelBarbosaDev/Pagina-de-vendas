from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'core/index.html'
    context = {
        'dfa':'dfadsfasdf'
    }
    return render(request, template_name=template_name, context=context)