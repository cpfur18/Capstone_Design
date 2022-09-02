from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# 노트북 기본 정보
class Prod(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    prod_company = models.CharField(max_length=30)
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_reg_date = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, through='Prod_Tag')

class Prod_Tag(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='related_item')
    name = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 노트북 옵션
class Prod_property(models.Model):
    prod_id = models.ForeignKey(Prod, db_column="prod_id", on_delete=models.CASCADE)
    option_id = models.IntegerField()
    option_title = models.CharField(max_length=10, null=True)
    option_Content = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.prod_id

# 노트북 이미지
class Prod_img(models.Model):
    prod_id = models.OneToOneField(Prod, db_column="prod_id", on_delete=models.CASCADE)
    prod_img_src = models.CharField(max_length=1000, null=True)

# 노트북 평가 수치
class Prod_ratings(models.Model):
    prod_id = models.OneToOneField(Prod, primary_key=True, db_column="prod_id", on_delete=models.CASCADE)
    cpu = models.FloatField()
    gpu = models.FloatField()
    ram = models.FloatField()
    stg = models.FloatField()
    disp = models.FloatField()
    disp_size = models.FloatField()
    carry = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.prod_id

# CPU 벤치마크 자료
class Passmark_cpu_info(models.Model):
    cpu_name = models.CharField(primary_key=True, max_length=30)
    cpu_mark = models.IntegerField()

    def __str__(self):
        return self.cpu_name

# GPU 벤치마크 자료
class Passmark_gpu_info(models.Model):
    gpu_name = models.CharField(primary_key=True, max_length=30)
    gpu_mark = models.IntegerField()

    def __str__(self):
        return self.gpu_name