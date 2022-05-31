from django.db import models

# 노트북 기본 정보
class Prod(models.Model):
    prod_num = models.AutoField(primary_key=True, verbose_name='노트북_번호')
    prod_company = models.CharField(max_length=30, verbose_name='노트북_제조사')
    prod_name = models.CharField(max_length=100, verbose_name='노트북_이름')
    prod_price = models.CharField(max_length=100, verbose_name='노트북_가격')
    prod_reg_date = models.CharField(max_length=100, verbose_name='노트북_등록일')
    prod_review_count = models.IntegerField(verbose_name='노트북_리뷰수')

    def __str__(self):
        return self.prod_name

# 노트북 옵션
class Prod_property(models.Model):
    prod_num = models.ForeignKey(Prod, on_delete=models.CASCADE, verbose_name='노트북_번호')
    prod_property = models.CharField(max_length=30, verbose_name='노트북_옵션')

# 노트북 평가 수치
class Prod_ratings(models.Model):
    prod_num = models.ForeignKey(Prod, on_delete=models.CASCADE, verbose_name='노트북_번호')
    prod_spec = models.IntegerField(verbose_name='노트북_성능_수치')
    prod_price = models.IntegerField(verbose_name='노트북_가격_수치')
    prod_portability = models.IntegerField(verbose_name='노트북_휴대성_수치')
    prod_screen = models.IntegerField(verbose_name='노트북_화면_수치')
    prod_as = models.IntegerField(verbose_name='노트북_as_수치')

# CPU 벤치마크 자료
class Passmark_cpu_info(models.Model):
    cpu_num = models.AutoField(primary_key=True, verbose_name='cpu_번호')
    cpu_name = models.CharField(max_length=30, verbose_name='cpu_이름')
    cpu_mark = models.IntegerField(verbose_name='cpu_벤치마크')

    def __str__(self):
        return self.cpu_name

# GPU 벤치마크 자료
class Passmark_gpu_info(models.Model):
    gpu_num = models.AutoField(primary_key=True, verbose_name='gpu_번호')
    gpu_name = models.CharField(max_length=30, verbose_name='gpu_ㅇ름')
    gpu_mark = models.IntegerField(verbose_name='gpu_벤치마크')

    def __str__(self):
        return self.gpu_name