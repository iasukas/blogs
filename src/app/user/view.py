from sanic import Blueprint, Request

bp = Blueprint("user", url_prefix="/user")


@bp.get("/")
def read_users(request: Request):
    pass


@bp.get("/me")
def read_user_me(request: Request):
    pass


@bp.get("/{user_id}")
def read_user_by_id(request: Request):
    pass


@bp.put("/me")
def update_user_me(request: Request):
    pass


@bp.put("/{user_id}")
def update_user(request: Request):
    pass


@bp.delete("/{user_id}")
def delete_user_by_id(request: Request):
    pass
