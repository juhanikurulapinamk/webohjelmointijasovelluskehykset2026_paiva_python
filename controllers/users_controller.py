from flask import jsonify, render_template, request

from custom_exceptions.not_found_exception import NotFoundException
from models import User


def get_all_users_handler():
    try:
            users = User.get_all()
            users_json_list = []
            for user in users:
                users_json_list.append({
                    'id': user._id,
                    'first_name': user.firstname,
                    'last_name': user.lastname,
                    'username': user.username
                })
            
            
            return jsonify(users_json_list)
    except Exception as e:
         return jsonify({'err': str(e)}), 500


def add_user_handler():
    try:
         req_data = request.get_json()
         new_user = User(req_data['first_name'], req_data['last_name'], req_data['username'])
         new_user.save()
         return jsonify({'id': new_user.id, 'first_name': new_user.firstname, 'last_name': new_user.lastname, 'username': new_user.username})
    except Exception as e:
         return jsonify({'err': str(e)}), 500



def update_user_by_id_handler(_id):
    try:
            
            user = User.get_by_id(_id)
            
            request_data = request.get_json()

            new_first_name = request_data.get('first_name', user.firstname)
            new_last_name = request_data.get('last_name', user.lastname)
            new_username = request_data.get('username', user.username)

            user.firstname = new_first_name
            user.lastname = new_last_name
            user.username = new_username
            user.save()
            
            return jsonify(
                {'id': user.id, 'first_name': user.firstname, 'last_name': user.lastname, 'username': user.username})
    except NotFoundException as e:
         return jsonify({'err': 'User not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500


def remove_user_by_id(_id):
    try:
        user = User.get_by_id(_id)
        user.remove()
        # User.remove_by_id(_id)
        return "", 204

    except NotFoundException as e:
         return jsonify({'err': 'User not found'}), 404
    except Exception as e:
        return jsonify({'err': str(e)}), 500


def get_user_by_id(_id):
    try:
        user = User.get_by_id(_id)
        return jsonify({
             'id': user.id,
             'first_name': user.firstname,
             'last_name': user.lastname,
             'username': user.username
        })
    except NotFoundException as e:
         return jsonify({'err': 'User not found'}), 404
    except Exception as e:
         return jsonify({'err': str(e)}), 500
         

                
           
    
    
                 
            

                
            
    