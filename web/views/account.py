from io import BytesIO

from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render, HttpResponse, redirect


from web import models
from utils.encrypt import md5
from utils.helper import generate_verification_code_image


# Example usage

def img_code(request):
    image_object, code_str = generate_verification_code_image()

    # return the image
    stream = BytesIO()
    image_object.save(stream, "png")
    # save code to session. expire in 60s
    request.session['image_code'] = code_str
    request.session.set_expiry(60)

    return HttpResponse(stream.getvalue())

# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"输入用户名"})
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"输入密码"}, render_value=True)
    )

    code = forms.CharField(
        label="security code",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"输入验证码"})
    )

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form":form})
    
    # else if request method is POST
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, "login.html", {"form":form})

    # else if check security code
    image_code = request.session.get("image_code")
    if not image_code:
        form.add_error("code","The security code has expired.")
        return render(request, "login.html", {"form":form}) 
    if image_code.upper() != form.cleaned_data['code'].upper():
        form.add_error("code","The security code is wrong.")
        return render(request, "login.html", {"form":form})
    
    # check username and password
    user=form.cleaned_data["username"]
    pwd=form.cleaned_data["password"]

    encrypt_pwd =md5(pwd)
    print(encrypt_pwd)
    admin_object = models.Admin.objects.filter(username=user, 
                                               password=encrypt_pwd).first()
    if not admin_object:
        return render(request, "login.html", {"form":form, "error": "The username or password is wrong."})
    request.session['info'] = {"id":admin_object.id, "name":admin_object.username}
    request.session.set_expiry(60 * 60 * 24 * 7)

    return redirect("/home/")

def logout(request):
    request.session.clear()
    return redirect("/login/")

def home(request):
    return render(request, "home.html")

def layout(request):
    return render(request, "layout.html")