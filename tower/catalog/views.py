from django.shortcuts import render

def home(request, template_name='catalog/home.html', **kwargs):
    'Example view that inserts content into the dash context passed to the dash application'
    context = {}
    dash_context = request.session.get('django_plotly_dash', dict())
    dash_context['django_to_dash_context'] = 'I am Dash receiving context from Django'
    request.session['django_plotly_dash'] = dash_context
    return render(request, template_name=template_name, context=context)