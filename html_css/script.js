function exibirDados() {
  var nome = document.getElementById("nome").value;
  var dataNascimento = document.getElementById("data-nascimento").value;
  var email = document.getElementById("email").value;
  var nomeBike = document.getElementById("nome-bike").value;

  var dados = "Nome: " + nome + "<br>" +
              "Data de Nascimento: " + dataNascimento + "<br>" +
              "Email: " + email + "<br>" +
              "Nome da Bike: " + nomeBike;

  var dadosExibidos = document.getElementById("dados-exibidos");
  dadosExibidos.innerHTML = dados;
}
