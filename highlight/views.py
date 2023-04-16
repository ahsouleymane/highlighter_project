from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
import json 
import colorama

# Create your views here.

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def acceuil(request):

    """ Récuperation du contenu des champs content et highlight 
    depuis le navigateur """

    if request.method == "POST":
        content = request.POST['content']
        highlight = request.POST['highlight']

        # Enlever les espaces du début de la chaine
        content = content.lstrip()

        # Enlever toute les espaces dans la chaine
        highlight = highlight.strip()

        # Convertion de la chaine de caractere en liste
        highlight = json.loads(highlight)

        """ Découpage de la chaine en trois parties et convertion de 
        ces parties en dictionnaire avec la fonction json.loads() """    
        liste_foo = highlight[0]
        liste_bar = highlight[1]
        liste_baz = highlight[2]

        # Affichage des trois chaine sur la console
        print(liste_foo)
        print(liste_bar)
        print(liste_baz)

        # Affectation des valeurs à travers leurs clés start, end, comment
        value_start_foo = liste_foo["start"]
        value_end_foo = liste_foo["end"]
        value_comment_foo = liste_foo["comment"]

        print(value_start_foo)
        print(value_end_foo)
        print(value_comment_foo)

        value_start_bar = liste_bar["start"]
        value_end_bar = liste_bar["end"]
        value_comment_bar = liste_bar["comment"]

        print(value_start_bar)
        print(value_end_bar)
        print(value_comment_bar)

        value_start_baz = liste_baz["start"]
        value_end_baz = liste_baz["end"]
        value_comment_baz = liste_baz["comment"]

        print(value_start_baz)
        print(value_end_baz)
        print(value_comment_baz)

        text_foo = content[value_start_foo: value_end_foo]
        text_bar = content[value_start_bar: value_end_bar]
        text_baz = content[value_start_baz: value_end_baz]

        print(text_foo)  
        print(text_bar) 
        print(text_baz)

        #text_foo = (colorama.Fore.RED + text_foo + colorama.Fore.RESET)
        #print(text_foo)

        text_cont_1 = content[:value_start_foo]
        text_cont_2 = content[value_end_foo: value_start_bar]
        text_cont_3 = content[value_end_bar: value_start_baz]
        text_cont_4 = content[value_end_baz:]

        text_cont_1_dict = {"1": text_cont_1}
        text_cont_2_dict = {"2": text_cont_2}
        text_cont_3_dict = {"3": text_cont_3}
        text_cont_4_dict = {"4": text_cont_4}

        text_dict_1 = {"1": text_foo}
        text_dict_2 = {"2": text_bar}
        text_dict_3 = {"3": text_baz}

        data = {
            "data_dict_1": text_dict_1,
            "data_dict_2": text_dict_2,
            "data_dict_3": text_dict_3,
            "data_dict_4": text_cont_1_dict,
            "data_dict_5": text_cont_2_dict,
            "data_dict_6": text_cont_3_dict,
            "data_dict_7": text_cont_4_dict,
        }

        print(text_dict_1)
        print(text_dict_2)
        print(text_dict_3)

        #content = (str.replace(content[value_start_foo: value_end_foo], text_foo_colored))
        
        #context = {'content': content}
        template = loader.get_template('highlight/acceuil.html')
        response = template.render(data, request)
        return HttpResponse(response)
        #return render(request, , {'data': sorted(text_dict.items())})
    else:
        context = {}
        return render(request, 'highlight/acceuil.html', context)
