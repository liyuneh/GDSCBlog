import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
import django
django.setup()

from BlogApp.models import Post
from CommentApp.models import Comment


post1 = Post.objects.create(title="Post 1", content="Content 1", category="Category 1", image="image1.jpg", tags="tag1, tag2")
post2 = Post.objects.create(title="Post 2", content="Content 2", category="Category 2", image="image2.jpg", tags="tag3, tag4")
post3 = Post.objects.create(title="Post 3", content="Content 3", category="Category 1", image="image3.jpg", tags="tag5, tag6")

category_posts = Post.objects.filter(category="Category 1")
for post in category_posts:
    print(f"{post.title} - {post.content}")

post_to_update = Post.objects.get(title="Post 1")
post_to_update.content = "Updated Content 1"
post_to_update.save()

post_to_delete = Post.objects.get(title="Post 2")
post_to_delete.delete()

comment1 = Comment.objects.create(content="Comment 1 for Post 1", author="Author 1", post=post1)
comment2 = Comment.objects.create(content="Comment 2 for Post 2", author="Author 2", post=post2)
comment3 = Comment.objects.create(content="Comment 3 for Post 3", author="Author 3", post=post3)

post_comments = Comment.objects.filter(post=post1)
for comment in post_comments:
    print(f"{comment.author} - {comment.content}")

comment_to_update = Comment.objects.get(content="Comment 2 for Post 2")
comment_to_update.content = "Updated Comment 2"
comment_to_update.save()

comment_to_delete = Comment.objects.get(content="Comment 3 for Post 3")
comment_to_delete.delete()
