from django.shortcuts import render
# Create your views here.


def index(request):
    context = {
        'jobs': [
            {
                'title': 'Pesquisador Científico',
                'company': 'Instituto Federal de Goiás',
                'date': 'Novembro 2018  - Janeiro 2021',
                'description':
                    '''
                    Responsável pelo <strong>desenvolvimento de softwares</strong> na etapa de
                    Análise de Viabilidade Técnica, Econômica e Ambiental de um projeto de
                    P&D em parceria com a Enel, cujo título é <em>"Eficiência Energética e Minigeração
                    em Instituições Públicas de Educação Superior"</em>. Também fui responsável pela construção de relatórios,
                    artigos científicos e manuais dos programas. Os softwares desenvolvidos foram <strong>registrados pelo INPI</strong>
                    e podem ser utilizados por investidores, pesquisadores e analistas políticos.
                    '''
            },
            {
                'title': 'Monitor de Automação e Supervisão de Processos I',
                'company': 'Instituto Federal de Goiás, Goiânia',
                'date': 'Janeiro 2018  - Agosto 2018',
                'description': '''Auxiliar o professor na preparação das aulas teóricas e práticas. 
                    Auxiliar os alunos no uso adequado dos CLPs e de outros equipamentos eletroeletrônicos 
                    para o desenvolvimento das atividades de aula.'''
            },
            {
                'title': 'Estagiário no Almoxarifado de Eletrotécnica',
                'company': 'Instituto Federal de Goiás, Goiânia',
                'date': 'Maio 2017 - Setembro 2017',
                'description': '''Fazer levantamento dos materiais elétricos do almoxarifado de eletrotécnica, 
                    como máquinas elétricas, painéis elétricos, CLPs, computadores, instrumentos de medições, entre outros; 
                    Categorização e manutenção dos equipamentos eletroeletrônicos em geral; Dar suporte técnico para as aulas 
                    práticas de uso geral de CLPs e microcontroladores.'''
            },
            {
                'title': 'Representante Técnico Bilíngue',
                'company': 'BrasilCenter, Goiânia',
                'date': 'Novembro 2012 - Março 2016',
                'description': 'Desenvolvimento de softwares, relatórios, artigos científicos e manuais na área de energias renováveis e engenharia econômica aplicada para um projeto em parceria com a Enel.'
            },
        ]
    }
    return render(request, 'home.html', context)
