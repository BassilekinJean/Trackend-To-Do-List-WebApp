from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Champ optionnel pour l'avatar

    def _str_(self):
        return self.nom

class File(models.Model):
    date = models.DateField()
    users = models.ManyToManyField(User, through='Possede')

    def _str_(self):
        return f"File {self.id}"
    

class Possede(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    date_ajout = models.DateField()

    def _str_(self):
        return f"{self.user.nom} - {self.file.id}"





class Task(models.Model):
    idTask = models.AutoField(primary_key=True)
    statut = models.CharField(max_length=50)
    intitule = models.CharField(max_length=200)
    date_limite = models.DateField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def _str_(self):
        return self.intitule



class Tag(models.Model):
    idTag = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)

    def _str_(self):
        return self.nom

class Contenir(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)