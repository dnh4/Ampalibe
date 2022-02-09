import ampalibe
'''
    Principal fonction, où les messages réçu sur
    la page facebook rentrent.

    @param user_id: identifiant facebook de l'exp.
    @param cmd: message de la personne.
    @param extends: contiennent la liste des autres
        données envoyé par facevook (heure d'envoi, ...)
'''
@ampalibe.commande('/')
def main(user_id, message, **extends):
    print("Hello, world")


@ampalibe.commande('/test')
def test(user_id, message, **extends):
    print("Hello, test")

