
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts) != 1 else ""})'

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],

        }
