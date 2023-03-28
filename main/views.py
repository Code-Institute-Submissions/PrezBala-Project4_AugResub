from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except Post.DoesNotExist:
        last_post = []

    context = {
        "forums": forums,
        "num_posts": num_posts,
        "num_users": num_users,
        "num_categories": num_categories,
        "last_post": last_post,
        "title": "ASTRO forum app"
    }

    return render(request, "index.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)

    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(
            user=author,
            content=comment
        )
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        comment_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(
            user=author,
            content=reply
        )
        comment_obj.replies.add(new_reply.id)

    context = {
        "post": post,
        "title": "ASTRO: "+post.title,
    }
    update_views(request, post)

    return render(request, "detail.html", context)


def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "forum": category,
        "title": "ASTRO: Posts"
    }
    return render(request, "posts.html", context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "ASTRO: Create New Post"
    })
    return render(request, "create_post.html", context)


def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts": posts,
        "title": "ASTRO: Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context)


def search_result(request):

    return render(request, "search.html")


@staff_member_required
def custom_admin_page(request):
    users = User.objects.all()
    return render(request, 'verify.html', {'users': users})


def admin_dashboard(request):
    posts = Post.objects.all()
    return render(request, 'admin_dashboard.html', {'posts': posts})


class EditPost(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def get_success_url(self):
        return reverse_lazy('admin_dashboard')


class DeletePost(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('admin_dashboard')


def approve_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.approved = True
    post.save()
    return redirect('admin_dashboard')


def unapproved_posts(request):
    posts = Post.objects.filter(approved=False)
    return render(request, 'admin_dashboard.html', {'posts': posts})


def toggle_close_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.closed = not post.closed
    post.save()
    return redirect('admin_dashboard')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    print("Request User:", request.user)
    print("Comment User:", comment.user)
    print("Is Superuser?", request.user.is_superuser)
    if request.user == comment.user.user or request.user.is_staff:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    print("Request User:", request.user)
    print("Reply User:", reply.user)
    print("Is Superuser?", request.user.is_superuser)
    if request.user == reply.user.user or request.user.is_staff:
        reply.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))