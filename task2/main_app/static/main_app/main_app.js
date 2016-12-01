(function() {
    'use strict';

    angular.module('main_app.demo', [])

    .controller('Main_appController', ['$scope', Main_appController]);

    function Main_appController($scope) {

        $scope.add = function (list, name) {
            var product = {
                name: name
            };

            list.products.push(product)
        };

        $scope.data = [
            {
                name: 'Furniture',
                products: [
                    {name: 'Table'},
                    {name: 'Chair'},
                    {name: 'Bed'},
                ]
            },
            {
                name: 'Fruit',
                products: [
                    {name: 'Lemon'},
                    {name: 'Apple'},
                ]
            },
        ]
    };
} )();