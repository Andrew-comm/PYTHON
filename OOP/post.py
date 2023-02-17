import datetime
import uuid
class Post:
    def __init__(self,author,content,message,date=datetime.datetime.now(),id=None):
        self.author = author
        self.content = content
        self.message = message
        self.date = date
        self.id =  uuid.uuid4 if id is None else id 

post = Post("Andrew","Developer","python and JavaScript skilled")
print(post.author)
print(post.content)
print(post.message)
print(post.date)
print(post.id)


        