'use strict';

angular.module('myApp.team_view', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/team_view', {
            templateUrl: 'team_view/team_view.html',
            controller: 'TeamViewCtrl'
        });
    }])

    .controller('TeamViewCtrl', function ($scope, $http) {
        $http({
            method: "GET",
            url: "http://localhost:8080"
        }).then(function (response) {
            $scope.myData = response.data;
            console.log(response.data);
        });
    });
