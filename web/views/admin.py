from django import forms
from django.shortcuts import render, redirect

from web import models
from utils.encrypt import md5

def admin_list(request):
    """User management"""

    queryset = models.Admin.objects.all().order_by("-id")
    # for row in queryset:
    #     print(row.username, row.password)
    return render(request, "admin_list.html", {"queryset": queryset})

class AdminModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ["username", "password", "age", "gender", "depart"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # customized operation
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": "form-control"}

class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = "__all__"

def admin_add(request):
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "admin_add.html", {"form":form})

    form = AdminModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, "admin_add.html", {"form":form})

    # encrypt the password before saving to database
    form.instance.password = md5(form.instance.password)
    print(form.instance.password)
    form.save()
    return redirect("/admin/list/")

def admin_add_depart(request):
    if request.method == "GET":
        form = DepartModelForm()
        return render(request, "admin_add_depart.html", {"form": form})
    
    form = DepartModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, "admin_add_depart.html", {"form":form})
    
    form.save()
    return redirect("/admin/list/")