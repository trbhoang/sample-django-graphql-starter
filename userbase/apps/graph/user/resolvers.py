from django.core.paginator import Paginator
from django.core.validators import URLValidator
from django.utils import timezone
from ariadne import convert_kwargs_to_snake_case

from ...user import UserStatus, models


@convert_kwargs_to_snake_case
def resolve_user(*_, id):
    return models.User.objects.get(pk=id)


@convert_kwargs_to_snake_case
def resolve_users(*_, page, limit, filter=None):
    users = models.User.objects.all()
    if filter:
        if "name" in filter:
            users = users.filter(name=filter["name"])
        if "email" in filter:
            users = users.filter(email=filter["email"])
        if "created_at" in filter:
            gte = filter["created_at"]["gte"]
            lte = filter["created_at"]["lte"]
            users = users.filter(created_at__date__gte=gte,
                                 created_at__date__lte=lte)
        if "status" in filter:
            users = users.filter(status__in=filter["status"])

    paginator = Paginator(users, limit)
    page_obj = paginator.get_page(page)

    return {
        "items": page_obj,
        "paginator": {
            "page": page,
            "limit": limit,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
            "has_next_page": page_obj.has_next(),
            "has_previous_page": page_obj.has_previous(),
        }
    }


@convert_kwargs_to_snake_case
def resolve_create_user(_, info, input):
    user_data = {
        "name": input["name"],
        "email": input["email"],
    }

    try:
        user = models.User.objects.create(**user_data)
        return {
            "status": True,
            "user": user,
        }
    except Exception as err:
        return {
            "status": False,
            "error": err,
        }
