from flask_restx import Namespace, Resource
from project.container import favorites_service, user_service
# from project.setup.api.models import favorites
from project.setup.db.favorites import FavoritesSchema
from project.views.auth.user import auth_required

favorites_ns = Namespace('favorites/movies')

favorites_schema = FavoritesSchema(many=True)


@favorites_ns.route('/')
class FavoritesView(Resource):
    # @favorites_ns.marshal_with(favorites, as_list=True, code=200, description='OK')
    @auth_required
    def get(self, email=None):
        user = user_service.get_by_email(email)
        return favorites_schema.dump(favorites_service.get_all_by_user(user.id))
        # return favorites_service.get_all_by_user(user.id)


@favorites_ns.route('/<int:movie_id>/')
class FavoriteView(Resource):
    @favorites_ns.response(404, 'Not Found')
    @auth_required
    def post(self, movie_id: int, email=None):
        user = user_service.get_by_email(email)
        favorites_service.create(movie_id, user.id)
        return "", 201

    @favorites_ns.response(404, 'Not Found')
    @auth_required
    def delete(self, movie_id: int, email=None):
        user = user_service.get_by_email(email)
        favorites_service.delete(movie_id, user.id)
        pass
