from nltk.chat.util import Chat, reflections

dialog = [
    # Général
    [
        r"(.*)bonjour(.*)|(.*)salut(.*)",
        ["Bonjour ! Je suis ton tuteur virtuel pour l'année de B1 à Ynov. Pose-moi des questions sur l'algorithmique, Go, Python, Java, l'Infra, la Sécu ou les Bases de Données (BD)."]
    ],
    # Algorithmique
    [
        r".*algorithme.*|.*algo.*",
        ["Un algorithme est une suite logique et finie d'instructions pour résoudre un problème. En B1, tu vas utiliser le pseudo-code pour structurer ta pensée avant de coder !"]
    ],
    [
        r".*boucle.*",
        ["Une boucle (comme FOR ou WHILE) est une structure qui permet de répéter une série d'instructions tant qu'une condition est remplie."]
    ],
    # Golang
    [
        r".*golang.*|.*go.*",
        ["Go (ou Golang) est un langage compilé et performant créé par Google. À Ynov, tu l'étudieras en B1 pour découvrir un langage moderne, excellent pour l'infrastructure et le backend."]
    ],
    [
        r".*variable.*go.*|.*d(?:é|e)clarer.*go.*",
        ["En Go, tu peux déclarer une variable avec le mot-clé 'var' (ex: var nom string) ou utiliser l'assignation courte très pratique : nom := \"Ynov\"."]
    ],
    # Python
    [
        r".*python.*",
        ["Python est un langage interprété, très lisible et idéal pour débuter. En B1, il te servira beaucoup pour l'algorithmie et tu pourras faire de la Data plus tard !"]
    ],
    [
        r".*liste.*python.*",
        ["Une liste en Python est une structure de données qui permet de stocker plusieurs éléments. Elle s'écrit avec des crochets, par exemple : ma_liste = [1, 2, 3]."]
    ],
    # Java & POO
    [
        r".*java.*",
        ["Java est un langage orienté objet très robuste, massivement utilisé en entreprise. Il utilise la JVM (Java Virtual Machine) pour fonctionner sur n'importe quel OS."]
    ],
    [
        r".*poo.*|.*orient(?:é|e) objet.*",
        ["La Programmation Orientée Objet (POO) est un concept où l'on modélise le code autour d'« objets » et de « classes ». Tu verras ça en profondeur avec Java !"]
    ],
    # Infrastructure
    [
        r".*infra.*|.*r(?:é|e)seau.*|.*linux.*",
        ["L'infrastructure regroupe le matériel, les OS (comme Linux) et les réseaux. En B1, tu apprendras les bases de l'administration système et comment les ordinateurs communiquent entre eux."]
    ],
    [
        r".*adresse ip.*",
        ["Une adresse IP est comme l'adresse postale d'un appareil sur un réseau. Elle permet aux machines de se trouver et de s'échanger des données."]
    ],
    # Sécurité
    [
        r".*s(?:é|e)cu.*|.*cybers(?:é|e)curit(?:é|e).*",
        ["En B1, la cybersécurité t'apprendra à protéger les systèmes et les données contre les attaques. Tu verras les bonnes pratiques et comment sécuriser ton propre code."]
    ],
    [
        r".*phishing.*|.*hame(?:ç|c)onnage.*",
        ["Le phishing est une attaque classique en sécu où l'attaquant se fait passer pour une entité de confiance pour te voler tes mots de passe. Ne clique pas sur n'importe quel lien !"]
    ],
    # Base de données (BD)
    [
        r".*bd.*|.*base de donn(?:é|e)es.*",
        ["Une base de données permet de stocker des informations de manière organisée. En B1, on se concentre souvent sur les bases de données relationnelles."]
    ],
    [
        r".*sql.*",
        ["Le SQL (Structured Query Language) est le langage utilisé pour interagir avec les bases de données relationnelles. Tu vas apprendre à faire des SELECT, INSERT, UPDATE, etc."]
    ],
    # Par défaut (Fallback)
    [
        r"(.*)",
        ["C'est une excellente question pour un B1 ! Peux-tu reformuler pour préciser si cela concerne l'Algorithmique, Python, Java, Go, l'Infra, la Sécu ou la BD ?"]
    ]
]

chatbot = Chat(dialog, reflections)

print("=========================================================")
print("🤖 Tuteur B1 Ynov - Prêt à répondre à tes questions !")
print("Pose des questions sur : Algo, Go, Python, Java, Infra, Sécu, BD.")
print("Tape 'quit' pour quitter.")
print("=========================================================")

chatbot.converse()
