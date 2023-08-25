from django.shortcuts import render
from .chatbot import *


def index(request):
    return render(request, 'index.html')


def chatbot_view(request):
    chatbot = ChatBot()

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = chatbot.obtener_respuesta(user_input)
        return render(request, 'index.html', {'response': bot_response})

    return render(request, 'index.html')
