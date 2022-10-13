from django.forms import ModelForm
from blog.models import Post

class PostForm(ModelForm):
    
    class Meta:
        #Creating the meta data for the PostForm which will parse just the Title, body and image into the html
        model = Post
        fields = ['title', 'body', 'header_image']

        #Defining function if form is valid
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

