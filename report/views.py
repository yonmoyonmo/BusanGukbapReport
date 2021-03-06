from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required


def data(req):
    posts = Report3.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(req, 'data.html', {'posts': posts})


def main(req):
    return render(req, 'main.html')


def single(req, pk):
    post = get_object_or_404(Report3, pk=pk)
    return render(req, 'single.html', {'post': post})


@permission_required('auth.add_group', raise_exception=True)
def editor(req):
    ImageFormSet = modelformset_factory(ReportImages, form=ImageForm, extra=5)
    if req.method == "POST":
        reportForm = ReportForm(req.POST)
        gukmoolForm = GukmoolForm(req.POST)
        gf = GoguiForm(req.POST)
        kf = KimchiForm(req.POST)
        sf = ServiceForm(req.POST)
        wf = WeesaengForm(req.POST)
        ll = LatlngForm(req.POST)

        formset = ImageFormSet(
            req.POST,
            req.FILES,
            queryset=ReportImages.objects.none()
        )

        if reportForm.is_valid() and formset.is_valid() and gukmoolForm.is_valid() and gf.is_valid() and kf.is_valid() and sf.is_valid() and wf.is_valid() and ll.is_valid():
            post = reportForm.save(commit=False)
            post.pub_date = timezone.now()
            post.save()

            for f in formset.cleaned_data:
                image = f['image']
                photo = ReportImages(report=post, image=image)
                photo.save()

            gukmool = gukmoolForm.save(commit=False)
            gukmool.report = post
            gukmool.save()

            gg = gf.save(commit=False)
            gg.report = post
            gg.save()

            kk = kf.save(commit=False)
            kk.report = post
            kk.save()

            ss = sf.save(commit=False)
            ss.report = post
            ss.save()

            ww = wf.save(commit=False)
            ww.report = post
            ww.save()

            ltlt = ll.save(commit=False)
            ltlt.report = post
            ltlt.save()

            return redirect('/')
    else:
        reportForm = ReportForm()
        gukmoolForm = GukmoolForm()
        gf = GoguiForm()
        kf = KimchiForm()
        sf = ServiceForm()
        wf = WeesaengForm()
        ll = LatlngForm()
        formset = ImageFormSet(queryset=ReportImages.objects.none())
    return render(
        req, 'editor.html',
        {
            'reportForm': reportForm, 'formset': formset, 'gukmoolForm': gukmoolForm,
            'gf': gf, 'kf': kf, 'sf': sf, 'wf': wf, 'll': ll,
        })
