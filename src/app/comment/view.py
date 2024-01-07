from sanic import Blueprint, Request

bp = Blueprint("comment", url_prefix="/comment")


@bp.get("/{post_id}")
def read_comments_by_post_id(request: Request):
    pass


@bp.post("/")
def create_comment(request: Request):
    pass


@bp.delete("/{comment_id}")
def delete_comment(request: Request):
    pass
