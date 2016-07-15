/**
 * Created by thiago on 13/07/16.
 */

angular.module('Comparador').controller('ComparadorController',
    function ($scope, $http) {
        $scope.sortBy = function(){
            if ($scope.reverse){
                $scope.reverse = false;
            }else{
                $scope.reverse = true;
            }
        };
        $scope.pesquisar = function (filtro) {
            $http.get('/api/servidores/?format=json',
                {
                    'params': {
                        'quantidade_cpu': filtro.quantidade_cpu,
                        'quantidade_memoria': filtro.quantidade_memoria,
                        'quantidade_hd': filtro.quantidade_hd,
                        'preco': filtro.preco,
                        'sistema_operacional': filtro.sistema_operacional,
                        'provedor': filtro.provedor
                    }
                }).success(
                function (data) {
                    $scope.filtroServidores = data;
                }
            )
        };
        $http.get('/api/servidores/?format=json').success(
            function (data) {
                $scope.parametros = {
                    'quantidade_cpu': [], 'quantidade_hd': [], 'quantidade_memoria': [],
                    'provedor': [], 'sistema_operacional': []
                };
                $scope.servidores = data;
                $scope.filtroServidores = data;
                angular.forEach($scope.servidores, function (value) {
                    console.log(value.quantidade_cpu, $scope.parametros.quantidade_cpu);
                    console.log($scope.parametros.quantidade_cpu.indexOf(value.quantidade_cpu));

                    if ($scope.parametros.quantidade_cpu.indexOf(value.quantidade_cpu) == -1) {
                        $scope.parametros.quantidade_cpu.push(value.quantidade_cpu)
                    }
                    if ($scope.parametros.quantidade_hd.indexOf(value.quantidade_hd) == -1) {
                        $scope.parametros.quantidade_hd.push(value.quantidade_hd)
                    }
                    if ($scope.parametros.quantidade_memoria.indexOf(
                            value.quantidade_memoria) == -1) {
                        $scope.parametros.quantidade_memoria.push(value.quantidade_memoria)
                    }
                    if ($scope.parametros.provedor.indexOf(
                            value.provedor.nome) == -1) {
                        $scope.parametros.provedor.push(value.provedor.nome)
                    }
                    if ($scope.parametros.sistema_operacional.indexOf(
                            value.sistema_operacional) == -1) {
                        $scope.parametros.sistema_operacional.push(value.sistema_operacional)
                    }
                });
            }
        )
    });