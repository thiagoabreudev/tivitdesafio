/**
 * Created by thiago on 13/07/16.
 */

angular.module('Comparador').controller('ComparadorController',
    function ($scope, $http) {
        $scope.pesquisar = function (filtro) {
            $http.get('/api/servidores/?format=json',
                {
                    'params': {
                        'quantidade_cpu': filtro.quantidade_cpu,
                        'quantidade_memoria': filtro.quantidade_memoria,
                        'preco': filtro.preco,
                        'sistema_operacional': filtro.sistema_operacional
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
                    'quantidade_cpu': [], 'quantidade_hd': [], 'quantidade_memoria': []
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
                });
            }
        )
    });