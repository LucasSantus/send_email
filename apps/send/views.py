from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from project.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
from send.forms import ValidacaoForm

import string
import random

def send_email():
    def generated_code_random():
        tamanho=6
        codigo = '-'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tamanho))
        return codigo

    subject = 'Confirmação de E-mail.'
    template_html = "email/confirmacao.html"
    from_email = DEFAULT_FROM_EMAIL
    to = ["leos9877@gmail.com"]

    context = {
        "code": generated_code_random(),
    }

    html_content = render_to_string(template_html, context)
    mensagem = EmailMultiAlternatives(subject, template_html, from_email, to)
    mensagem.attach_alternative(html_content, "text/html")
    mensagem.send()

def validacao(request):
    send_email()
    form = ValidacaoForm()
    if request.POST:
        form = ValidacaoForm(request.POST)
        if form.is_valid():
            # messages.success(request,"Sala de Votação registrada com sucesso!")
            return redirect("index")
    
    context = {
        "form": form,
    }

    send_email()

    return render(request, "send/validacao.html", context)

