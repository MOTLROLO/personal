function calcular1() {
  let promedio = parseInt(document.getElementById("promedio").value),
    categoria;

  if (promedio < 0 || promedio > 20 || isNaN(promedio)) {
    document.getElementById("resultado").value =
      "Ingrese un número válido entre 0 y 20";
  } else {
    if (promedio >= 17) {
      categoria = "A";
    } else if (promedio >= 14) {
      categoria = "B";
    } else if (promedio >= 12) {
      categoria = "C";
    } else {
      categoria = "D";
    }
    document.getElementById("resultado").value = categoria;
  }
}

function calcular2() {
  let ventas = parseFloat(document.getElementById("ventas").value),
    hijos = parseInt(document.getElementById("hijos").value);
  let bon, comi, desc, sBruto, sNeto;

  if (ventas < 0 || hijos < 0 || (isNaN(ventas) && isNaN(hijos))) {
    document.getElementById("comi").value = "Ingresar los datos solicitados";
    document.getElementById("bon").value = "Ingresar los datos solicitados";
    document.getElementById("sBruto").value = "Ingresar los datos solicitados";
    document.getElementById("desc").value = "Ingresar los datos solicitados";
    document.getElementById("sNeto").value = "Ingresar los datos solicitados";
  } else {
    bon = hijos * 50;
    comi = ventas * 0.075;
    sBruto = 600 + comi + bon;
    desc = sBruto * 0.11;
    sNeto = sBruto - desc;

    document.getElementById("comi").value = comi.toFixed(2);
    document.getElementById("bon").value = bon.toFixed(2);
    document.getElementById("sBruto").value = sBruto.toFixed(2);
    document.getElementById("desc").value = desc.toFixed(2);
    document.getElementById("sNeto").value = sNeto.toFixed(2);
  }
}

function calcular3() {
  let edad = parseInt(document.getElementById("edad").value),
    peso;

  if (edad < 0 || edad > 12 || isNaN(edad)) {
    document.getElementById("resultado").value = "Ingresar edad válida";
  } else {
    peso = 3 * edad + 7;
    document.getElementById("resultado").value = peso;
  }
}

function calcular4() {
  let c = parseFloat(document.getElementById("c").value);
  let k, r, f;

  if (isNaN(c)) {
    document.getElementById("f").value = "Ingresar la temperatura";
    document.getElementById("k").value = "Ingresar la temperatura";
    document.getElementById("r").value = "Ingresar la temperatura";
  } else {
    r = c + 460;
    k = r - 187;
    f = (9 * c) / 5 + 32;
    document.getElementById("f").value = f.toFixed(2);
    document.getElementById("k").value = k.toFixed(2);
    document.getElementById("r").value = r.toFixed(2);
  }
}
