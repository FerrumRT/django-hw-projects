from django.shortcuts import render

from new_app.models import MyModel


# Create your views here.
def index(request):
    my_models = MyModel.objects.all()
    return render(request, 'new_app/index.html',
                  context={'my_models': my_models})
