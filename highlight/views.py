from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
import json 
# Create your views here.

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

        """ Convertion de la chaine de caractere en liste
        avec la fonction json.loads() """
        highlight = json.loads(highlight)

        """ Découpage de la liste en trois parties formant 
        des dictionnaires de données  """    
        liste_foo = highlight[0]
        liste_bar = highlight[1]
        liste_baz = highlight[2]

        print(liste_foo)
        print(liste_bar)
        print(liste_baz)

        """ Affectation des valeurs à value_start_***, value_end_***, value_comment_*** 
        à travers les clés start, end, comment contenue dans le dictionnaire  """
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

        """ Affectation d'une partie de la chaine à text_*** allant de l'index 
        value_start_*** à value_end_*** dans la chaine content """
        text_foo = content[value_start_foo: value_end_foo + 1]
        text_bar = content[value_start_bar: value_end_bar + 1]
        text_baz = content[value_start_baz: value_end_baz + 1]

        print(text_foo)  
        print(text_bar) 
        print(text_baz)

        # Insertion des bouts de text dans des dictionnaires
        text_dict_1 = {"1": text_foo}
        text_dict_2 = {"2": text_bar}
        text_dict_3 = {"3": text_baz}

        print(text_dict_1)
        print(text_dict_2)
        print(text_dict_3)

        text_cont_1 = content[:value_start_foo]
        text_cont_2 = content[value_end_foo: value_start_bar]
        text_cont_3 = content[value_end_bar: value_start_baz]
        text_cont_4 = content[value_end_baz:]

        text_cont_1_dict = {"1": text_cont_1}
        text_cont_2_dict = {"2": text_cont_2}
        text_cont_3_dict = {"3": text_cont_3}
        text_cont_4_dict = {"4": text_cont_4}

        print(text_cont_1_dict)
        print(text_cont_2_dict)
        print(text_cont_3_dict)
        print(text_cont_4_dict)

        find_text_bar_in_text_foo = text_foo.find(text_bar)
        print(find_text_bar_in_text_foo)
        if find_text_bar_in_text_foo != -1:
            text_foo_1 = text_foo[:value_start_bar]
            text_foo_2 = text_foo[value_end_bar:]

        find_text_baz_in_text_foo = text_foo.find(text_baz)
        print(find_text_baz_in_text_foo)
        if find_text_baz_in_text_foo != -1:
            text_foo_3 = text_foo[:value_start_baz]
            text_foo_4 = text_foo[value_end_baz:]

        find_text_foo_in_text_bar = text_bar.find(text_foo)
        print(find_text_foo_in_text_bar)
        if find_text_foo_in_text_bar != -1:
            text_bar_1 = text_bar[:value_start_foo]
            text_bar_2 = text_bar[value_end_foo:]

        find_text_baz_in_text_bar = text_bar.find(text_baz)
        print(find_text_baz_in_text_bar)
        if find_text_baz_in_text_bar != -1:
            text_bar_3 = text_bar[:value_start_baz]
            text_bar_4 = text_bar[value_end_baz:]

        find_text_foo_in_text_baz = text_baz.find(text_foo)
        print(find_text_foo_in_text_baz)
        if find_text_foo_in_text_baz != -1:
            text_baz_1 = text_baz[:value_start_foo]
            text_baz_2 = text_baz[value_end_foo:]

        find_text_bar_in_text_baz = text_baz.find(text_bar)
        print(find_text_bar_in_text_baz)
        if find_text_bar_in_text_baz != -1:
            text_baz_4 = text_baz[:value_start_bar]
            text_baz_5 = text_baz[value_end_bar:]


        #text_dict = {"1": text_cont_1, "1": text_foo, "2": text_cont_2, "2": text_bar, "3": text_cont_3, "3": text_baz, "4": text_cont_4}

        data = {
            "data_dict_1": text_dict_1,
            "data_dict_2": text_dict_2,
            "data_dict_3": text_dict_3,
            "data_dict_4": text_cont_1_dict,
            "data_dict_5": text_cont_2_dict,
            "data_dict_6": text_cont_3_dict,
            "data_dict_7": text_cont_4_dict,
        }

        template = loader.get_template('highlight/acceuil.html')
        response = template.render(data, request)
        return HttpResponse(response)
    else:
        context = {}
        return render(request, 'highlight/acceuil.html', context)
