from django.db import models


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
    max_length=100, help_text='Entre o nome')
    idade = models.IntegerField(help_text='Entre a idade')
    salario = models.DecimalField(
    help_text='Entre o salário',
    decimal_places=2, max_digits=8)
    email = models.EmailField(
    help_text='Informe o email', max_length=254)
    telefone = models.CharField(
    help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(
    help_text='Nascimento no formato DD/MM/AAAA',
    verbose_name='Data de nascimento')

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length=100, help_text='Nome da rua')
    numero = models.CharField(max_length=10, help_text='Número da residência')
    bairro = models.CharField(max_length=50, help_text='Bairro')
    cidade = models.CharField(max_length=50, help_text='Cidade')
    estado = models.CharField(max_length=2, help_text='UF')
    cep = models.CharField(max_length=9, help_text='CEP no formato 00000-000')

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
    max_length=100, help_text='Entre o nome')
    idade = models.IntegerField(help_text='Entre a idade')
    salario = models.DecimalField(
    help_text='Entre o salário',
    decimal_places=2, max_digits=8)
    email = models.EmailField(
    help_text='Informe o email', max_length=254)
    telefone = models.CharField(
    help_text='Telefone com DDD e DDI', max_length=20)
    dtNasc = models.DateField(
    help_text='Nascimento no formato DD/MM/AAAA',
    verbose_name='Data de nascimento')

    def __str__(self):
        return self.nome