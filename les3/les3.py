<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>page1</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
<a href="page2.html" target="_blank">Ссылка на страницу 2</a>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab alias animi at commodi consectetur delectus dolor, facilis
illo illum iusto necessitatibus non nostrum obcaecati pariatur quae, quasi suscipit vero voluptas.
</p>
<form action="">
    <label for="field1" class="lead">Введите ваше имя:</label>
    <input type="text" id="field1" class="form-control form-control-lg"><br>
    <label for="field2">Чек-бокс:</label>
    <input type="checkbox" id="field2" class="form-check-input"><br>
    <label for="field3">Введите ваш пароль:</label>
    <input type="password" id="field3" class="form-control form-control-sm"><br>
    <textarea></textarea><br>
    <input type="button" class="btn btn-danger" value="Отправить форму">
</form>
</body>
</html>