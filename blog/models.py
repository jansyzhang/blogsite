from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail

# Create your models here.
class BlogType(models.Model):
    '''
    Blog 类型
    '''
    type_name = models.CharField(max_length=50)

    def __str__(self):
        '''
        set display type
        '''
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    '''
    Blog
    '''
    title = models.CharField(max_length=50)  # 标题
    content = RichTextUploadingField()  # 内容
    # 将author与django内部用户关联起来
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者
    created_time = models.DateTimeField(auto_now_add=True)  # 发表时间
    read_details = GenericRelation(ReadDetail)  # 关联Readdetail模型
    last_updated_time = models.DateTimeField(auto_now=True)  # 最新更新时间
    # 将blog与blog type 关联起来（one blog -> one blog type）
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE) 

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        '''
        set display type (admin)
        '''
        return "<Blog: %s>" % self.title
    
    class Meta:
        ordering = ['-created_time']



