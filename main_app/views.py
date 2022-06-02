from django.views.generic.base import TemplateView
from .models import Champion
# from django.views.generic.edit import CreateView,UpdateView,DeleteView


class Home(TemplateView):
    template_name = 'index.html'
    

class ChampionList(TemplateView):
    template_name = 'champs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        

        if name != None:
            context["champions"] = Champion.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"

        else:
            context["champions"] = Champion.objects.all()
            context["header"] = "List of Champions"

        return context
