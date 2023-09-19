from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from naseverecodit import html
import sys
sys.path.insert(0, 'hackathon\\ru_punct')
from ru_punct import playing_with_model


# Create your views here.

def result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text_input = data.get('text_input', '')
        processed_text = playing_with_model.rupunc(text_input)
        processed_text = html.analizate_text(processed_text)
        return JsonResponse({'processed_text': processed_text})
    return render(request, 'home.html', {'initial_text': ''})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")