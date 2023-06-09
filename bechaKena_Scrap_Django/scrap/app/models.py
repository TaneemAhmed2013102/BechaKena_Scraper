from django.db import models


class BookShelf(models.Model): 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    rokomari_id = models.CharField(max_length=255)
    boibitan_name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, default='')
    company_logo = models.CharField(max_length=255, default='')

    def _str_(self):
        return self.title

# FOR MORE SCRAPING PURPOSES I HAVE WRITTEN THE MODELS THAT ARE WRITTEN IN THE LOWER PART!

# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     author = models.CharField(max_length=255)
#     rokomari_id = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.title

# class ANESTHESIOLOGY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class CARDIOLOGY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class CARDIAC_SURGERY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class DERMATOLOGY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class ENT(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class NEUROLOGY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class ORTHOPEDICS(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class UROLOGY(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.name


# class Book2(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     author = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.title
    
    
# class Doctor(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     degree = models.CharField(max_length=255)
#     specialist = models.CharField(max_length=255)
#     image_path = models.CharField(max_length=255, default='')
#     hospital = models.CharField(max_length=255, default='')

#     def _str_(self):
#         return self.title
