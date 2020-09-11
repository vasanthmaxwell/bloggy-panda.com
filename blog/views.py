from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Categories
from urllib.parse import quote_plus
from .forms import CommentForm
# Create your views here.

def home(request):
    post = Blog.objects.order_by('-timestamp')[:5]
    return render(request,'index.html',{'blog':post})

def articles(request):
    post = Blog.objects.all()
    paginator = Paginator(post,9)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_query_set = paginator.page(page)
    except PageNotAnInteger:
        paginated_query_set = paginator.page(1)
    except EmptyPage:
        paginated_query_set = paginator.page(paginator.num_pages)
    return render(request,'blog.html',{'blog':paginated_query_set,'page_request_var':page_request_var})

def team(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request,slug):
    post = get_object_or_404(Blog,slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('blog-full',slug=slug)
    else:
        form = CommentForm()
    share = quote_plus(post.title)
    recent = Blog.objects.order_by('-timestamp')[:3]
    return render(request,'blog-single.html',{'post':post,'recent':recent,'share':share,'form':form})

