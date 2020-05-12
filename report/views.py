from django.shortcuts import render, redirect
from .models import *
from .forms import *


def main(req):
    posts = Report.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(req, 'main.html', {'posts': posts})


def editor(req):
    if req.method == "POST":
        form = ReportForm(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = ReportForm()
    context = {'form': form}
    return render(req, 'editor.html', context)
