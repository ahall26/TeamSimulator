'use strict';

angular.module('myApp.team_view', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/team_view', {
            templateUrl: 'team_view/team_view.html',
            controller: 'TeamViewCtrl'
        });
    }])

    .controller('TeamViewCtrl', function ($scope, $http) {
            $http({url: "http://localhost:8080/", method: "GET"}).then(function (response) {
                $scope.myData = JSON.parse(response.data);
            }).then(function () {
                $http({url: "http://localhost:8080/roles", method: "GET"}).then(function (response) {
                    $scope.roles = response.data;
                })
            })

            $scope.updateTeam = function (team_size, team_name, team_role, team_company) {
                console.log(team_size, team_name, team_role, team_company);
                var fullURL = encodeURI(`http://localhost:8080/?team_size=${team_size}&team_name=${team_name}&team_role=${team_role}&team_company=${team_company}`)
                $http({url: fullURL, method: "GET"}).then(function (response) {
                    $scope.myData = JSON.parse(response.data);
                })
            };
        }
    )


