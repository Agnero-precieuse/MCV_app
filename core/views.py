from django.shortcuts import get_object_or_404, render
from .models import Evenement, Predications, EgliseInfo
from .forms import ContactForm

def accueil(request):
    return render(request, 'core/accueil.html')

def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire ici
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Vous pourriez envoyer un email ici ou sauvegarder dans la base de données
            return render(request, 'core/contact_success.html', {'nom': nom})
    else:
        form = ContactForm()
    
    # Récupérez les informations de l'église
    eglise_info = EgliseInfo.objects.first()
    
    return render(request, 'core/contacts.html', {
        'form': form,
        'adresse_eglise': eglise_info.adresse,
        'email_eglise': eglise_info.email,
        'telephone_eglise': eglise_info.telephone,
        'programme_hebdomadaire': eglise_info.programme_hebdomadaire
    })
    

def predications(request):
    predications = Predications.objects.all().order_by('-date')  # Tous les predications, triés par date la plus récente
    return render(request, 'core/predications.html', {'predications': predications})

from django.db.models import Q  # Pour effectuer des recherches complexes

def agenda(request):
    query = request.GET.get('q')  # Rechercher par titre
    categorie = request.GET.get('categorie')  # Filtrer par catégorie
    evenements = Evenement.objects.all().order_by('date_debut')

    # Recherche par mot-clé (titre ou description)
    if query:
        evenements = evenements.filter(
            Q(titre__icontains=query) | Q(description__icontains=query)
        )
    
    # Filtrer par catégorie
    if categorie:
        evenements = evenements.filter(categorie=categorie)

    return render(request, 'core/agenda.html', {'evenements': evenements, 'query': query, 'categorie': categorie})


# Vue pour les détails d'un événement
def evenement_detail(request, evenement_id):
    evenement = get_object_or_404(Evenement, id=evenement_id)
    return render(request, 'core/evenement_detail.html', {'evenement': evenement})
