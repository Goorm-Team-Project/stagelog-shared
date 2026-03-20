import functools

from django.conf import settings
from django.http import HttpResponse, JsonResponse


def health_check(request):
    return HttpResponse("OK", status=200)


def common_response(success=True, data=None, message="", status=200):
    payload = {
        "success": success,
        "message": message,
        "data": data,
    }
    return JsonResponse(payload, status=status, json_dumps_params={"ensure_ascii": False})


def _auth_from_gateway(request):
    header_name = getattr(settings, "GATEWAY_USER_ID_HEADER", "X-User-Id")
    raw = request.headers.get(header_name)
    if raw is None:
        return None, None

    value = str(raw).strip()
    if not value:
        return None, "인증 사용자 정보가 비어 있습니다."

    try:
        return int(value), None
    except (TypeError, ValueError):
        return None, "인증 사용자 정보 형식이 잘못되었습니다."


def login_check(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        user_id, error = _auth_from_gateway(request)
        if error:
            return common_response(success=False, message=error, status=401)
        if user_id is None:
            return common_response(success=False, message="인증 정보가 없습니다.", status=401)

        request.user_id = user_id
        return func(request, *args, **kwargs)

    return wrapper


def get_optional_user_id(request):
    user_id, error = _auth_from_gateway(request)
    if error:
        return None, error
    return user_id, None


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")
