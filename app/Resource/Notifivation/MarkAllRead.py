from flask_restful import Resource, reqparse, abort, output_json
from app.Model.Users import User
import json
import datetime
from app.Model.Notifications import Notifications

parser = reqparse.RequestParser()
parser.add_argument('uid', type=str, help='uid',required=True)

class MarkAllRead(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        user_one = User.get_user_one_by_id(args['uid'])
        print(user_one)
        if user_one == None:
            abort(400, message={'uid':'notfind'})
        notif = Notifications.mark_as_read_by_phone(user_one['mobile'])
        return {'Notifications':notif},200
    

