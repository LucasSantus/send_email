from django.shortcuts import render
from sms import send_sms

from django.core.mail import EmailMultiAlternatives
from unincare.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string

def send_email(request):
    subject = 'Seja Bem Vindo a UNINCARE'
    template_html = "email/cadastro.html"
    from_email = DEFAULT_FROM_EMAIL
    to = [perfil.usuario.email]

    # context = {
    #     "first_name": perfil.usuario.first_name,
    # }

    html_content = render_to_string(template_html, context)
    mensagem = EmailMultiAlternatives(subject, template_html, from_email, to)
    mensagem.attach_alternative(html_content, "text/html")
    mensagem.send()

    return render(request, "home/index.html")