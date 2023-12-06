from django.shortcuts import render, redirect

from apps.blogs.models import Blog


def index(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs,
    }

    return render(request, "index.html", context=context)


def create_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        Blog.objects.create(
            title=title,
            description=description,
            image=image,
        )
        return redirect('homepage')
    
    return render(request, 'create_blog.html')


def detail_blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        ...
    
    return render(request, 'detail.html', locals())


def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        ...
    
    if blog is not None:
        blog.delete()
        return redirect('homepage')
    else:
        return redirect('homepage')
    

def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == "POST":
        
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()

        return redirect('detail_blog', blog.id)
    
    return render(request, 'update_blog.html', locals())
