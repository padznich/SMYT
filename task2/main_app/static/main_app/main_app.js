(function() {
    'use strict';

    angular.module('main_app.demo', [])

    .controller('Main_appController', ['$scope', '$http', Main_appController]);

    function Main_appController($scope, $http) {

        $scope.add = function (list, name) {
            var product = {
                name: name
            };

            $http.post('/main_app/products/', product)
              .then(function (response) {
                list.products.push(response.data);
              },
              function() {
                  alert('Could not create the product.');
              });
        };

        $scope.data = [];
        $http.get('/main_app/categories/').then(function(response) {
            $scope.data = response.data;
        });
    };
} )();