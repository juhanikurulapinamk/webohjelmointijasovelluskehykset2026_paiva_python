
# app.py

from flask import Flask, jsonify, request

from controllers import users_controller
from models import User

app = Flask(__name__)

""" Mikä tässä koodissa on vikana?

Jos tätä arvoidaan vain sillä perusteella, toimiiko kaikki, 
niin koodissa ei ole mitään vikaa, koska kaikki ominaisuudet
toimivat oikein

Arkkitehtuurin näkökulmasta koodi on aivan käyttökelvotonta.

Tehdään tämä seuraavaksi käyttäen MVC:tä.

"""






# Hakee kaikki käyttäjät JSON-muodossa
#@app.route('/api/users', methods=['GET'])

app.add_url_rule('/api/users', 'get_all_users', users_controller.get_all_users_handler, methods=['GET'])


# Lisää uuden käyttäjän request data oltava json-muodossa
# Voit käyttää tähän vaikka Postmania tms. vastaavaa Rest Clientiä
#@app.route('/api/users', methods=['POST'])
app.add_url_rule('/api/users', 'add_user', users_controller.add_user_handler, methods=['POST'])


# Hakee käyttäjän id:n perusteella
app.add_url_rule('/api/users/<_id>', 'get_user_by_id', users_controller.get_user_by_id, methods=['GET'])



# Muokkaa id:n mukaan valitun käyttäjän tietoja
# request data lähetettävä JSON-muodossa
app.add_url_rule('/api/users/<_id>', 'edit_user', users_controller.update_user_by_id_handler, methods=['PUT', 'PATCH'])


# Käyttäjän poisto id:n perusteella
app.add_url_rule('/api/users/<_id>', 'remove_user_by_id', users_controller.remove_user_by_id, methods=['DELETE'])




if __name__ == '__main__':
    app.run(port=5001)