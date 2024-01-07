from sanic import Blueprint, Request

bp = Blueprint("permission", url_prefix="/permission")


@bp.get("/")
def read_permissions(request: Request):
    pass


@bp.get("/{permission_id}")
def read_permission_by_id(request: Request):
    pass


@bp.post("/")
def create_permission(request: Request):
    pass


@bp.put("/{permission_id}")
def update_permission_by_id(request: Request):
    pass


@bp.delete("/{permission_id}")
def delete_permission_by_id(request: Request):
    pass
