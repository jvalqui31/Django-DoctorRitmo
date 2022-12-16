
function relog(){
    var nombres_dias = new Array("Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
    var nombres_meses = new Array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()

    horaImprimible = hora + ":" + minuto + ":" + segundo

    dia = momentoActual.getDate() //dia del mes
    dia_semana = momentoActual.getDay() //dia de la semana
    mes = momentoActual.getMonth() + 1
    anio = momentoActual.getFullYear()

    fecha_actual  = nombres_dias[dia_semana] +", "+ dia +" de "+ nombres_meses[mes -1] +" de "+anio

    //document.form_reloj.reloj.value = horaImprimible
    document.getElementById('relog').innerHTML = fecha_actual +" | "+horaImprimible;
    setTimeout("relog()",1000)
} 

// Selecciono el cuerpo del documento HTML (body) 
var cuerpoweb = document.body; 

// Obtengo el valor actual de la key 'modo' en localStorage 
var modocolor = localStorage.getItem("modo"); 

// Esta función carga el modo Oscuro o Claro, según el usuario haya configurado 
function cargarModo() {    

    if (modocolor === "oscuro") {               
        cuerpoweb.classList.add("oscuro");
    } else {
        cuerpoweb.classList.add("claro");
    }

}

// Cuando el usuario presiona el botón, llama a la función que corresponde
// ya sea para activar el modo claro o el modo oscuro
var btnpresionado = false;

function cambiarModo() {

    if (btnpresionado) { // Si No es presionado el botón 
        cuerpoweb.classList.remove("oscuro");
        localStorage.setItem("modo", "claro");
        cuerpoweb.classList.add("claro");
        btnpresionado = false;
    } else { // Si es presionado el botón 

        if (modocolor === "oscuro") {
            resetear(); 
            btnpresionado = true;           
        } else {

            cuerpoweb.classList.remove("claro");
            localStorage.setItem("modo", "oscuro");
            cuerpoweb.classList.add("oscuro");        
            btnpresionado = true;

        }        
    }
}

// Reseteamos la configuración realizada y refrescamos la página (Esto es opcional, tu decides usarlo o no)
function resetear() {

    localStorage.removeItem('modo');
    location.reload();

}


  function convertir(){
      var valor=parseFloat(document.getElementById("cantidad").value);
      document.getElementById("valor").innerHTML="<b>"+valor+"</b>";
      var de=document.getElementById("de").value;
      var a=document.getElementById("a").value;
      var dolar=720;
      var euro=872;
      var resultado=0;

      //peso a dolar
      if(de==1 && a==2){
          resultado=valor/dolar;
      }
      //peso a euro
      else if(de==1 && a==3){
          resultado=valor/euro;
      }
      //dolar a peso
      else if(de==2 && a==1){
        resultado=valor*dolar;
    }
    //dolar a euro
    else if(de==2 && a==3){
        resultado=valor*(dolar/euro);
    }
    //euro a peso
    else if(de==3 && a==1){
        resultado=valor*euro
    }
    //euro a dolar
    else if(de==3 && a==2){
        resultado=valor*(euro/dolar);
    }
    //en los dos lo mismo
    else{
        resultado=valor;
    }
    document.getElementById("resultado").innerHTML="Conversión: $"+resultado.toFixed(2);

  }

  function textCounter(field, field2, maxlimit) {
    var countfield = document.getElementById(field2);
    if (field.value.length > maxlimit) {
        field.value = field.value.substring(0, maxlimit);
        return false;
    } else {
        countfield.value = maxlimit - field.value.length;
    }

    document.nombreDelFormulario.addEventListener('submit', validarFormulario);
}

// Now come to the validation part


function validation(){
    let userName = document.getElementById("user").value;
    let userMobile = document.getElementById("mob").value;
    let userEmail = document.getElementById("mail").value;
    let userPass = document.getElementById("pass").value;
    let userCnfPass = document.getElementById("cnf-pass").value;

    //regx expression for all fields

    let checkUserName = /^[A-Za-z. ]{3,25}$/;
    let checkUserPassword = /^(?=.*[0-9])(?=.*[!@#%$^&*.,-_])[A-Za-z0-9!@#%$^&*.,-_]{8,15}$/
    let checkUserMobile = /^[0123456789]{1}[0-9]{8}$/
    let checkUserEmail = /^[A-Za-z0-9]{3,}@[a-zA-Z]{3,}[.]{1}[a-zA-Z.]{2,6}$/

    //check all expressions

    if(checkUserName.test(userName)){
        document.getElementById("name-error").innerHTML = "";
        document.getElementById("user").style.border = "1px solid rgb(148,214,173)"
    }
    else{
        document.getElementById("name-error").innerHTML = "Ingrese solo letras";
        document.getElementById("user").style.border = "1px solid red";
        return false;
    }

    if(checkUserMobile.test(userMobile)){
        document.getElementById("mob-error").innerHTML = "";
        document.getElementById("mob").style.border = "1px solid rgb(148,214,173)"
    }
    else{
        document.getElementById("mob-error").innerHTML = "Ingresar sin puntos ni guíon";
        document.getElementById("mob").style.border = "1px solid red";
        return false;
    }

    if(checkUserEmail.test(userEmail)){
        document.getElementById("mail-error").innerHTML = "";
        document.getElementById("mail").style.border = "1px solid rgb(148,214,173)"
    }
    else{
        document.getElementById("mail-error").innerHTML = "Email invalido";
        document.getElementById("mail").style.border = "1px solid red";
        return false;
    }

    if(checkUserPassword.test(userPass)){
        document.getElementById("pass-error").innerHTML = "";
        document.getElementById("pass").style.border = "1px solid rgb(148,214,173)"
    }
    else{
        document.getElementById("pass-error").innerHTML = "Min 9 Max 16 ";
        document.getElementById("pass").style.border = "1px solid red";
        return false;
    }

    if(userCnfPass.match(userPass)){
        document.getElementById("cnfpass-error").innerHTML = "";
        document.getElementById("cnf-pass").style.border = "1px solid rgb(148,214,173)"
    }
    else{
        document.getElementById("cnfpass-error").innerHTML = "Pass no son iguales";
        document.getElementById("cnf-pass").style.border = "1px solid red";
        return false;
    }
}

//filtrado automático de tabla
$(document).ready(function(){
    $("#texto_buscado").on("keyup",function(){
        var texto = $(this).val().toLowerCase();
        $("#datos_tabla tr").filter (function(){
            $(this).toggle($(this).text().toLowerCase().indexOf(texto) > -1)
        });
    });
});