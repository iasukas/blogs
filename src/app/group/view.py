from sanic import Blueprint, Request

bp = Blueprint("group", url_prefix="/group")


@bp.get("/")
def read_groups(request: Request):
    pass


@bp.get("/{group_id}")
def read_group_by_id(request: Request):
    pass


@bp.post("/")
def create_group(request: Request):
    pass


@bp.put("/{group_id}")
def update_group_by_id(request: Request):
    pass


@bp.delete("/{group_id}")
def delete_group_by_id(request: Request):
    pass
