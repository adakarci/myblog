from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from comment.forms import CommentForm
from comment.models import Comment


class PostIndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.published_objects.all()


class PostView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(
            post=self.get_object(), is_published=True)
        return context


def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {
        "posts": posts, "tag": tag}, context_instance=RequestContext(request))
