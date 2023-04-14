let form = document.getElementById("loginForm");

function login() {
  let email = document.getElementById("typeEmailX").value;
  let password = document.getElementById("typePasswordX").value;

  const usuarios = [
    { email: "1483380@senati.pe", password: "1483380" },
    { email: "1438673@senati.pe", password: "1438673" },
    { email: "1477082@senati.pe", password: "1477082" },
    { email: "webjuanjls@gmail.com", password: "juanleon" },
  ];

  // Verificar las credenciales
  let credencialesValidas = false;
  for (let i = 0; i < usuarios.length; i++) {
    if (usuarios[i].email === email && usuarios[i].password === password) {
      credencialesValidas = true;
      break;
    }
  }

  if (credencialesValidas) {
    // Redirigir a la página deseada
    window.location.href = "inicio.html";
  } else {
    alert(
      "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo."
    );
  }
}

document.addEventListener("keyup", function (event) {
  if (event.key === "Enter" && event.target.nodeName === "INPUT") {
    login();
  }
});
