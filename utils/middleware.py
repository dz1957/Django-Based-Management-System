from django.middleware.security import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 1. 不用登陆就可以访问
        if request.path_info in ["/login/", "/img/code/", "/layout/"]:
            return
        
        # 2. 获取 session
        info_dict = request.session.get("info")

        # 未登录
        if not info_dict:
            return redirect("/login/")
        
        # 已登录
        request.info_dict = info_dict
        return