from django.shortcuts import render
from django.views import View


class HelloView(View):
    def get(self, request):
        return render(request, 'app1/hello_world.html')


hello_view = HelloView.as_view()
