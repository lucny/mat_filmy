from django.shortcuts import render
from django.views.generic import ListView
from .models import Film

# Pohled pro úvodní stránku s výpisem tří nejlepších filmů
def index(request):
    context = {
        # Výběr tří nejlepších filmů (uspořádány sestupně podle hodnocení)
        'filmy': Film.objects.order_by('-rate').all()[:3],
    }
    return render(request, 'index.html', context=context)


# Generická třída vytvářející pohled pro výpis všech filmů
class FilmListView(ListView):
    model = Film
    # Určujeme název klíče, pod nímž budou v šabloně přístupná data o záznamech filmů
    context_object_name = 'filmy'
    # ORM dotaz, který upřesňuje sadu vybraných dat
    # (v tomto případě budou filmy primárně seřazeny podle data uvedení - sestupně, sekundárně podle názvů - abecedně)
    queryset = Film.objects.order_by('-release_date', 'title')
    # Název a umístění šablony, v níž budou filmy vypsány
    template_name = 'film/list.html'

    # Metoda, pomocí které můžeme do existujícího kontextu přidat další vlastní data
    def get_context_data(self, **kwargs):
        # Zdědíme standardní kontext (v našem případě už obsahuje klíč 'filmy')
        context = super().get_context_data(**kwargs)
        # Přidáme do kontextu vlastní klíč titulek s hodnotou 'Seznam filmů'
        context['titulek'] = 'Seznam filmů'
        return context

# Metoda, která řeší pohled pro zobrazení stránky s detailem filmu
# Kromě požadavku předáváme atribut pk (primární klíč záznamu s daným filmem)
def film_detail(request, pk):
    context = {
        # Do kontextu přidáme klíč film a vložíme do něj data z databáze
        # Používáme k tomu ORM dotaz, který vybere právě film, jenž má id rovno požadovanému pk
        'film': Film.objects.get(id=pk),
    }
    # Vykreslíme šablonu a předáme ji původní požadavek i připravený kontext
    return render(request, 'film/detail.html', context=context)

# Metoda, která řeší pohled pro zobrazení stránky s výpisem filmů podle žánru
# Kromě požadavku předáváme atribut genre (název žánru)
def film_genre(request, genre):
    context = {
        # Do kontextu přidáme klíč zanr, který bude obsahovat název požadovaného žánru
        'zanr': genre,
        # Do kontextu přidáme klíč filmy a vložíme do něj data z databáze
        # Používáme k tomu ORM dotaz, který vybere právě filmy, obsahující požadovaný žánr
        # Filmy budou uspořádány podle data uvedení (sestupně)
        'filmy': Film.objects.filter(genres__name__contains=genre).order_by('-release_date'),
    }
    return render(request, 'film/genre.html', context=context)
