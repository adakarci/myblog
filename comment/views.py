from .forms import CommentForm
from django.http import HttpResponseRedirect
from post.models import Post
from django.contrib import messages


def create_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not comment.owner:
                comment.owner = "Anonymous"
            comment.post = post
            comment.save()
            return HttpResponseRedirect(
                comment.post.get_absolute_url())
        else:
            messages.error(
                request, 'email adresi olmadan yorum birakamazsiniz.')
            return HttpResponseRedirect(
                post.get_absolute_url())
    else:
        form = CommentForm()
        return HttpResponseRedirect("/")
