import pathlib
import traceback

from litestar import Litestar, Request, delete, get, post, put
from litestar.contrib.htmx.response import ClientRedirect
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException
from litestar.response import Response, Template
from litestar.static_files import StaticFilesConfig
from litestar.status_codes import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from litestar.template import TemplateConfig

from app.database import PyObjectId, collection
from app.models import Item


async def exception_handler(request: Request, exc: Exception) -> Response:
    if isinstance(exc, HTTPException):
        return Response(content={"error": str(exc)}, status_code=exc.status_code)
    else:
        error_msg = f"Unhandled exception: {exc}\n{traceback.format_exc()}"
        print(error_msg)
        return Response(
            content={"error": "An unexpected error occurred", "details": str(exc)},
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        )


@get("/")
async def index() -> Template:
    items = await collection.find().to_list(length=None)
    return Template(template_name="index.html", context={"items": items})


@get("/items")
async def list_items() -> Template:
    items = await collection.find().to_list(length=None)
    return Template(template_name="items.html", context={"items": items})


@get("/items/new")
async def new_item_form() -> Template:
    return Template(template_name="item_form.html")


@post("/items")
async def create_item(request: Request) -> Response:
    try:
        form_data = await request.form()
        name = form_data.get("name")
        description = form_data.get("description")

        if not name:
            raise HTTPException(HTTP_400_BAD_REQUEST, "Name is required")

        new_item = Item(
            name=name,
            description=description,
        )
        result = await collection.insert_one(
            new_item.dict(by_alias=True, exclude={"id"})
        )

        if not result.inserted_id:
            raise HTTPException(
                HTTP_500_INTERNAL_SERVER_ERROR, "Failed to insert item into database"
            )

        return ClientRedirect(redirect_to="/items")
    except HTTPException as _:
        raise
    except Exception as e:
        print(f"Error in create_item: {str(e)}")
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "An unexpected error occurred"
        )


@get("/items/{item_id:str}")
async def get_item(item_id: str) -> Template:
    item = await collection.find_one({"_id": PyObjectId(item_id)})
    if item:
        return Template(template_name="item_detail.html", context={"item": item})
    return Template(template_name="404.html"), 404


@get("/items/{item_id:str}/edit")
async def edit_item_form(item_id: str) -> Template:
    item = await collection.find_one({"_id": PyObjectId(item_id)})
    if item:
        return Template(template_name="item_form.html", context={"item": item})
    return Template(template_name="404.html"), 404


@put("/items/{item_id:str}")
async def update_item(item_id: str, request: Request) -> Response:
    form_data = await request.form()
    updated_item = {
        "name": form_data.get("name"),
        "description": form_data.get("description"),
    }
    result = await collection.update_one(
        {"_id": PyObjectId(item_id)}, {"$set": updated_item}
    )
    if result.modified_count:
        return ClientRedirect(redirect_to="/items")
    return Response(content="Item not found", status_code=HTTP_404_NOT_FOUND)


@delete("/items/{item_id:str}", status_code=200)
async def delete_item(item_id: str) -> Response:
    result = await collection.delete_one({"_id": PyObjectId(item_id)})
    if result.deleted_count:
        return Response(status_code=200, content="")
    return Response(status_code=404, content="Item not found")


app = Litestar(
    route_handlers=[
        index,
        list_items,
        new_item_form,
        create_item,
        get_item,
        edit_item_form,
        update_item,
        delete_item,
    ],
    template_config=TemplateConfig(
        directory=pathlib.Path("app/templates"),
        engine=JinjaTemplateEngine,
    ),
    exception_handlers={Exception: exception_handler},
    static_files_config=[
        StaticFilesConfig(
            directories=["static"],
            path="/static",
        )
    ],
)
