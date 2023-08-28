1.
admin.py:
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'user', 'price', 'auction', 'created_at', 'created_date', 'updated_date', 'image','show_mini_image']
    list_filter = ['auction', 'created_at']


models.py:
 @admin.display(description='мини изображение')
    def show_mini_image(self):
        if self.image:
            return format_html('<img src="{}" width=50 height=50>', self.image.url)

----------------------------------------------------------------------------------------------------------

2.
index.html:
{% extends 'base.html' %}
{% load static %}

{% block title %}
Главная
{% endblock %}

{% block content %}
<ul class="nav nav-pills sticky-top bg-white nav-fill">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="{% url 'main_page' %}">
      <span style="font-weight: bold;">Главная</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'top-sellers' %}"><span style="font-weight: bold;">Топ продавцов</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'adv-post' %}">
      <span style="font-weight: bold;">Разместить объявление</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="register.html">
      <span style="font-weight: bold;">Регистрация</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'login' %}">
      <span style="font-weight: bold;">Войти</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'profile' %}">
      <span style="font-weight: bold;">Профиль</span>
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'logout' %}">
      <span style="font-weight: bold;">Выйти</span>
    </a>
  </li>
</ul>

<div id="carouselExampleControls" class="carousel slide bg-primary" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{% static 'img/adv.png' %}" class="mx-auto d-block w-33" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{% static 'img/adv.png' %}" class="mx-auto d-block w-33" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{% static 'img/adv.png' %}" class="mx-auto d-block w-33" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Предыдущий</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Следующий</span>
  </button>
</div>
<div class="container" style="margin: 50px;">
  <div class="display-2">
    <span class="badge bg-primary">В центре внимания</span>
  </div>
</div>
<div class="container">
  <div class="row">
    <ul class="nav nav-tabs bg-white">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="#">Проверенные продавцы</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Новинки</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Избранное</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Еще что-нибудь</a>
      </li>
    </ul>
    <form class="row g-3">
      <div class="col-auto w-50">
        <input type="text" class="form-control">
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-success mb-3">Найти</button>
      </div>
    </form>
  </div>
  <div class="col">
    {% for adv in advertisements %}
    <div class="card mb-2" style="max-width: 1200px; margin-top: 20px;">
      <div class="row g-0">
        <div class="col-md-4">
          <a href="advertisement.html" class="nav-link">
            <img src="{% if adv.image %}{{ adv.image.url }}{% else %}{% static 'img/adv.png' %}{% endif %}" class="img-fluid rounded-start" alt="Card title">
          </a>
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">
              <a href="advertisement.html" class="nav-link"><strong>{{ adv.title }}</strong></a>
            </h5>
            <a href="advertisement.html" class="nav-link">
              <p class="card-text">
              {{ adv.description }}
              </p>
              <span>Автор: {{ adv.user }}</span>
              <p class="card-text"><small class="text-muted">Размещено: {{ adv.created_at }}</small></p>
              <p> Цена: {{ adv.price }}</p>
            </a>
          </div>
        </div>
      </div>
    </div>
    {% endfor %}

  </div>
</div>
<footer style="padding: 100px;" class="bg-primary">
  <nav class="navbar navbar-expand-sm navbar-dark">
    <a class="navbar-brand" href="#">Добавьте</a>
    <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapsibleNavId" aria-controls="collapsibleNavId" aria-expanded="false"
            aria-label="Toggle navigation"></button>
    <div class="collapse navbar-collapse" id="collapsibleNavId">
      <ul class="navbar-nav me-auto mt-2 mt-lg-0">
        <li class="nav-item">
          <a class="nav-link active" href="#" aria-current="page">сюда<span
                  class="visually-hidden">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">что</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="dropdownId" data-bs-toggle="dropdown" aria-haspopup="true"
             aria-expanded="false">хотите</a>
          <div class="dropdown-menu" aria-labelledby="dropdownId">
            <a class="dropdown-item" href="#">например</a>
            <a class="dropdown-item" href="#">ссылки на социальные сети</a>
          </div>
        </li>
      </ul>
      <form class="d-flex my-2 my-lg-0">
        <input class="form-control me-sm-2" type="text" placeholder="Search">
        <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</footer>
{% endblock %}