/**
 * Created by thiago on 13/07/16.
 */

angular.module('Comparador', ['ngRoute']).config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    //Por questao de compatibilidade com o template django
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);