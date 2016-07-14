/**
 * Created by thiago on 13/07/16.
 */

angular.module('Comparador').controller('ComparadorController',
    function ($scope, $http) {
        $scope.pesquisa = function (filtro) {
            $scope.filtro = filtro;
            $http.get('http://127.0.0.1:8000/servidores/?format=json',
                {'params': {'cpu': $scope.filtro}}).success(
                function (data) {
                    $scope.servidores = data;
                }
            )
        };
        $http.get('http://127.0.0.1:8000/servidores/?format=json').success(
            function (data) {
                $scope.servidores = data;
                $scope.filtros = data;
            }
        )
    });