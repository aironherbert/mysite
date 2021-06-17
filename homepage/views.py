from django.shortcuts import render
# Create your views here.
def index(request):
    context={
        'jobs': {
            1: {
                'title': 'Pesquisador Científico',
                'company': 'Instituto Federal de Goiás',
                'date': 'Novembro 2018  - Janeiro 2021',
                'description': 'Desenvolvimento de softwares, relatórios, artigos científicos e manuais na área de energias renováveis e engenharia econômica aplicada para um projeto em parceria com a Enel.'
            }
        }
    }
    return render(request, 'home.html', context)