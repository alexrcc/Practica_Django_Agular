var app = angular.module("app",['ngResource']);

function leer($scope,listado, listado2){
	$scope.lista=listado.get();
	$scope.lista2=listado2.get();
	$scope.mensaje="";
	$scope.usu=false;

	$scope.ingresar = function(){
		var ci=$scope.cedulaEntrada;
		var band=true;
		for (var i=0; i < $scope.lista.length; i++) {
			if(ci == $scope.lista[i].cedula){
				band=false;
				$scope.usu=true;
				break;
			}
		}
		if(band==false){
			window.location="repaso.html";
		}
		else{
			$scope.mensaje="No se encuentra el estudiante";
		}
	}
	$scope.mensaje = function(){
		alert("Matricula Solicitada Con Éxito");
	}
}

app.controller("controlador",leer);

app.factory('listado',function($resource){
	//$http es un servicio de http
	 //return $resource(url, paramDefaults, actions)
	 return $resource("http://localhost:8000/ws/alumnos/",{},{get:{method:"get",isArray:true}});
	
});
app.factory('listado2',function($resource){
	//$http es un servicio de http
	 //return $resource(url, paramDefaults, actions)
	 return $resource("http://localhost:8000/ws/materias/",{},{get:{method:"get",isArray:true}});
	
});
