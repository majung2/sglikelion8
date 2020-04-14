from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content
from .forms import ContentForm

# Create your views here.
def home(request):
    posts = Content.objects.all() # 또는 () 생략
    return render(request, 'mydiary/home.html',{'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
            form = ContentForm()

    return render(request, 'mydiary/new.html', {'form':form})
