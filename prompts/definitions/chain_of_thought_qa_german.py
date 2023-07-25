"""
Prompt to run qa (German). Replace the text and question and play around!
"""
prompt = """### Instruction: Versuche Anfragen von Nutzern basierend auf dem "Kontext"-Dokument zu beantworten. Überlege schrittweise. Gebe aus "Zu dieser Frage gibt es im Text keine Informationen." falls die Frage nicht zu beantworten ist. 

### Input: Kontext: Im 19. Jahrhundert entwickelte sich in der Schweiz das Jodeln in Chören als Folge der Umgestaltung des Geisteslebens durch die Aufklärung, der Entdeckung volkstümlicher und eidgenössischer Werte. Da die Schweiz kaum höfisches Leben und weder Hofkapellen noch Opern und Solisten kannte, verbreitete sich hier der Chorgesang früher als andernorts in allen Schichten des Volkes. Nach 1830 wurden für die neu gegründeten Jodlervereine eigene mehrstimmige Jodellieder (Volkslieder) komponiert. Anfrage: Beschreibe, was im 20. Jahrhundert mit dem Jodeln in der Schweiz passierte. 

### Response:"""

settings = {
    "maximum_tokens": 128
}

model = "luminous-supreme-control"