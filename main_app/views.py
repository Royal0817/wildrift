from django.views.generic.base import TemplateView
from .models import Champion
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.urls import reverse

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

class ChampionCreate(CreateView):
    model = Champion
    fields = ['name', 'nickname', 'img', 'damage', 'utility', 'toughness', 'difficulty', 'champ_type']
    template_name = "champ_create.html"
    success_url = "/champions/"
    def get_success_url(self):
        return reverse('champ_detail', kwargs={'pk': self.object.pk})

class ChampionDetail(DetailView):
    model = Champion
    template_name = "champ_detail.html"