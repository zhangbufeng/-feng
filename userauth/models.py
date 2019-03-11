from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    tel=models.CharField(max_length=11,validators=[
        RegexValidator(regex="^137|182|183|155",message="手机号不符合规范")
    ])
    img=models.ImageField(upload_to="uploads/userimg")
    c=models.IntegerField(default=0,
        choices=(
            (0,"普通用户"),
            (1,"高级用户")
        )
    )

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "博客管理"
        verbose_name_plural = "博客用户管理"
