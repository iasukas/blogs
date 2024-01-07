from sanic import Blueprint, Request

bp = Blueprint("post", url_prefix="/post")


@bp.get("/")
def read_posts(request: Request):
    pass


@bp.get("/{post_id}")
def read_post_by_id(request: Request):
    pass


@bp.post("/")
def create_post(request: Request):
    pass


@bp.put("/{post_id}")
def update_post_by_id(request: Request):
    pass


@bp.delete("/{post_id}")
def delete_post_by_id(request: Request):
    pass
