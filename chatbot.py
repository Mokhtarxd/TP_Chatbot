from nltk.chat.util import Chat, reflections

dialog = [
    [
        r".*fili(?:è|e)res?.*|.*formations?.*",
        ["Ynov propose plusieurs filières : Informatique, Cybersécurité, Intelligence Artificielle & Data, 3D & Jeu Vidéo, Marketing & Communication Digitale, et Design & Création."]
    ],
    [
        r".*modules?.*",
        ["Les modules d'enseignement à Ynov sont fortement axés sur la pratique avec une pédagogie par projets, simulant des conditions réelles d'entreprise."]
    ],
    [
        r".*mati(?:è|e)res?.*",
        ["Les matières dépendent de la filière choisie. En Informatique par exemple, vous aurez des matières comme le développement logiciel, le Cloud, l'administration réseau ou la Data."]
    ],
    [
        r".*campus.*|.*villes?.*",
        ["Ynov est présent sur de nombreux campus : Aix-en-Provence, Bordeaux, Lille, Lyon, Montpellier, Nantes, Paris, Rennes, Toulouse, ainsi qu'à Casablanca et en 100% ligne avec Ynov Connect."]
    ],
    [
        r".*tarifs?.*|.*prix.*|.*co(?:û|u)t.*",
        ["Les tarifs annuels en statut initial se situent généralement entre 7 000 € et 9 000 €. Si vous êtes en alternance, les frais de scolarité sont intégralement pris en charge par l'entreprise d'accueil !"]
    ],
]

chatbot = Chat(dialog, reflections)
chatbot.converse()