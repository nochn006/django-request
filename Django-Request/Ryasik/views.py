from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.META["REMOTE_ADDR"]
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>IP: {path}</p>
    <p>User-agent: {user_agent}</p>
""")


def error(request):
    return HttpResponse("При ошибке обратиться: tg @rryasik", status=404, reason="Incorrect data")


def user(request, login="Moroz", password=249):
    return HttpResponse(f"<h2>Логин: {login}   Пароль: {password}</h2>")
