from sanic import Blueprint, Request

bp = Blueprint("tag", url_prefix="/tag")


@bp.get("/")
def read_tags(request: Request):
    pass


@bp.get("/{tag_id}")
def read_tag_by_id(request: Request):
    pass


@bp.post("/")
def create_tag(request: Request):
    pass


@bp.put("/")
def update_tag(request: Request):
    pass


@bp.delete("/{tag_id}")
def delete_tag_by_id(request: Request):
    pass
