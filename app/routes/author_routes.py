from flask import Blueprint, abort, make_response, request, Response
from app.models.author import Author
from app.models.book import Book
from ..db import db
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@bp.post("")
def create_author():
    request_body = request.get_json()

    return create_model(Author, request_body)

@bp.get("")
def get_all_authors():
    return get_models_with_filters(Author, request.args)

@bp.post("/<author_id>/books")
def create_book_with_author(author_id):

    author = validate_model(Author, author_id)
    
    request_body = request.get_json()
    request_body["author_id"] = author.id
    return create_model(Book, request_body)


@bp.get("/<author_id>/books")
def get_books_by_author(author_id):
    author = validate_model(Author, author_id)
    response = [book.to_dict() for book in author.books]
    return response

@bp.get("/<author_id>")
def get_one_author(author_id):
    author = validate_model(Author, author_id)
    return author.to_dict(), 200




