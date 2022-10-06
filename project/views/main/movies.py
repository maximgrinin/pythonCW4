from flask_restx import Namespace, Resource
from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_and_status_parser
from project.setup.db.movie import MovieSchema

movies_ns = Namespace('movies')

# Создаем экземпляры схем сериализации для одной и нескольких сущностей
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(page_and_status_parser)
    # @movies_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        # return movie_service.get_all(**page_and_status_parser.parse_args())
        return movies_schema.dump(movie_service.get_all(**page_and_status_parser.parse_args()))


@movies_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @movies_ns.response(404, 'Not Found')
    @movies_ns.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)
