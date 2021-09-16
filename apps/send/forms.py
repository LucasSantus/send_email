from django import forms

class ValidacaoForm(forms.Form):
    codigo = forms.CharField(label = '*Código:', required = True)

    class Meta:
        fields = ("__all__")

        error_messages = {
            "codigo":{
                "required": "O código é obrigatório.",
                "invalid": "Insira um código válido.",
            },
        }