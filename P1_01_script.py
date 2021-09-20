# -*- coding: utf-8 -*-
import os, requests, uuid, json # Import des modules

key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]               # Permet de récupérer la variable environnement contenant la clé d'abonnement

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
if not endpoint_var_name in os.environ:
     raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]                   # Permet de récupérer la variable environnement contenant l'URL de base permettant d'envoyer la requête API TRANSLATOR 3

path = '/detect?api-version=3.0' # permet de selectionner la détection de langues dans l api translator 3
constructed_url = endpoint + path                       # URL de base permettant d'envoyer la requête API TRANSLATOR 3 concaténée endpoint
headers = {                                             # en-tete permet la transmission de la cle d'abonnement Azure de l API TRANSLATOR 3 et la localisation etc..
    'Ocp-Apim-Subscription-Key': subscription_key,  
    'Ocp-Apim-Subscription-Region':'westeurope',
    'Content-type': 'application/json',                 #En-tête de demande obligatoire.Spécifie le type de contenu de la charge utile. Les valeurs possibles sont les suivantes : application/json.
    'X-ClientTraceId': str(uuid.uuid4())                # *Facultatif*.GUID généré par le client pour identifier de façon unique la demande. Vous pouvez omettre cet en-tête si vous incluez l’ID de trace dans la chaîne de requête à l’aide d’un paramètre de requête nommé `ClientTraceId`.
}
# You can pass more than one object in body.
body = [
    {'id': 1,'text': 'Ne l fin de l seclo XIX l Japon era inda çconhecido i sótico pa l mundo oucidental. Cula antroduçon de la stética japonesa, particularmente na Sposiçon Ounibersal de 1900, an Paris, l Oucidente adquiriu un apetite ansaciable pul Japon i Heiarn se tornou mundialmente coincido pula perfundidade, ouriginalidade i sinceridade de ls sous cuntos. An sous radadeiros anhos, alguns críticos, cumo George Orwell, acusórun Heiarn de trasferir sou nacionalismo i fazer l Japon parecer mais sótico, mas, cumo   '},
    {'id': 2,'text': 'Des County liegt im middlan Sidwestn vo Mississippi, is im Sidn uma 45 km vo Louisiana  '},
    {'id': 3,'text': 'Noadat Napoleon versloagen was ien 1814, wör op t Wiener kongres ien 1815  '},
    {'id': 4,'text': ' Extension of Universities Act of 1959'},
    {'id': 5,'text': 'O panteyón de nobles, puesto a on son apedecatos muitos nobles aragoneses que quisioron descansar chunto a os reis '}
    ]
 #Création de la requête pour détecter la langue

# You can pass more than one object in body.
#body = [
 #   {'id': 1,'text': 'plat, gelege  '},
 #   {'id': 2,'text': 'Salve, mondo!'}
 #   ]
 #Création de la requête pour détecter la langue

# You can pass more than one object in body.
#body = [{
#    'text': 'Salve, mondo!'
#}]

request = requests.post(constructed_url, headers=headers, json=body) #requête POST: l’URL concaténée endpoint, les en-têtes de requête headers et le corps de la demande body
response = request.json() 
print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': '))) # Permet l'affichage de la réponse à la requête de détection au format JSON