(function() {
    'use strict';

    angular.module('main_app.demo', [])

    .controller('Main_appController', ['$scope', '$http', Main_appController]);

    function Main_appController($scope, $http) {

        $scope.add = function (list, name) {
            var product = {
                name: name
            };

            list.products.push(product)
        };

        $scope.data = [];
        $http.get('/main_app/products').then(function(response) {
            $scope.data = response.data;
        });
    };
} )();