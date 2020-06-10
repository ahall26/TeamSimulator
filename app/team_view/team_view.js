'use strict';

angular.module('myApp.team_view', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/team_view', {
            templateUrl: 'team_view/team_view.html',
            controller: 'TeamViewCtrl'
        });
    }])
    //
    // .controller('TeamViewCtrl', function ($scope, $http) {
    //     $http({
    //         method: "GET",
    //         url: "http://localhost:8080"
    //     }).then(function (response) {
    //         $scope.myData = JSON.parse(response.data);
    //     }).then(
    //         $http({
    //             method: "GET",
    //             url: "http://localhost:8080/roles"
    //         }).then(function (response) {
    //             console.log($scope.roles)
    //             $scope.roles = JSON.parse(response.data);
    //         }));
    // });

    .controller('TeamViewCtrl', function ($scope, $http) {
        $http({url: "http://localhost:8080/?team_size=6", method: "GET"}).then(function (response) {
            $scope.myData = JSON.parse(response.data);
        }).then(function () {
            console.log($scope.myData);
        }).then(function () {
            $http({url: "http://localhost:8080/roles", method: "GET"}).then(function (response) {
                $scope.roles = response.data;
            }).then(function () {
                console.log($scope.roles);
            })
        })
    });
