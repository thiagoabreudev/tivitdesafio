/**
 * Created by thiago on 13/07/16.
 */

angular.module('Comparador').controller('ComparadorController',
    function ($scope, $http) {
        $scope.pesquisar = function (filtro) {
            $http.get('/servidores/?format=json',
                {
                    'params': {
                        'quantidade_cpu': filtro.quantidade_cpu,
                        'quantidade_memoria': filtro.quantidade_memoria
                    }
                }).success(
                function (data) {
                    $scope.filtroServidores = data;
                }
            )
        };
        $http.get('/servidores/?format=json').success(
            function (data) {
                $scope.servidores = data;
                $scope.filtroServidores = data;
            }
        )
    });