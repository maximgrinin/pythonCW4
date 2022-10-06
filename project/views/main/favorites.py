from flask_restx import Namespace, Resource
from project.container import favorites_service, user_service, movie_service
from project.views.auth.user import auth_required
from project.setup.db.movie import MovieSchema
from project.setup.api.parsers import page_parser

favorites_ns = Namespace('favorites/movies')

favorites_schema = MovieSchema(many=True)


@favorites_ns.route('/')
class FavoritesView(Resource):
    @auth_required
    def get(self, email=None):
        user = user_service.get_by_email(email)
        favorites_list = favorites_service.get_all_by_user(user.id)
        favorites_ids: list | [] = [item.movie_id for item in favorites_list]
        return favorites_schema.dump(
            movie_service.get_all_by_list(favorites_ids, **page_parser.parse_args())
        ), 200


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
