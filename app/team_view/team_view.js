'use strict';

angular.module('myApp.team_view', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/team_view', {
            templateUrl: 'team_view/team_view.html',
            controller: 'TeamViewCtrl'
        });
    }])

    .controller('TeamViewCtrl', function ($scope, $http) {
        $scope.loading = $http;
        $scope.comps = [];
        $http({url: "http://localhost:8080/", method: "GET"}).then(function (response) {
            $scope.myData = JSON.parse(response.data);
            $scope.members = JSON.parse(response.data).team.team_members;
            $scope.team_percentage = JSON.parse(response.data).team.team_percentage;
            $scope.team_compatibility_color = JSON.parse(response.data).team.team_compatibility_color;
            console.log($scope.members);
        }).then(function () {
            $http({url: "http://localhost:8080/roles", method: "GET"}).then(function (response) {
                $scope.roles = response.data;
            }).then(function () {
                $http({url: "http://localhost:8080/personalities", method: "GET"}).then(function (response) {
                    $scope.team_personalities = response.data;
                }).then(function () {
                    $http({url: "http://localhost:8080/compatibilities", method: "GET"}).then(function (response) {
                        $scope.compatibilities = response.data;
                    })
                })
            })
        })

        $scope.updateTeam = function (team_size, team_name, team_role, team_company) {
            let fullURL = encodeURI(`http://localhost:8080/?team_size=${team_size}&team_name=${team_name}&team_role=${team_role}&team_company=${team_company}`)
            $http({url: fullURL, method: "GET"}).then(function (response) {
                $scope.myData = JSON.parse(response.data);
                $scope.members = JSON.parse(response.data).team.team_members;
                $scope.team_percentage = JSON.parse(response.data).team.team_percentage;
                $scope.team_compatibility_color = JSON.parse(response.data).team.team_compatibility_color;
            })
        }

        $scope.randomTeam = function () {
            let fullURL = encodeURI(`http://localhost:8080/?team_size=${Math.floor(Math.random() * (15 - 3 + 1)) + 3}`)
            $http({url: fullURL, method: "GET"}).then(function (response) {
                $scope.myData = JSON.parse(response.data);
                $scope.members = JSON.parse(response.data).team.team_members;
                $scope.team_percentage = JSON.parse(response.data).team.team_percentage;
                $scope.team_compatibility_color = JSON.parse(response.data).team.team_compatibility_color;
            })
        }

        $scope.updateTeamMember = function (id, pid) {
            $scope.members.find(m => m.id === id).mbti = $scope.team_personalities[pid];
            $scope.calculateTotal($scope);
        }

        $scope.calculateTotal = function ($scope) {
            $scope.comps = [];
            $scope.team_total = 0;
            console.log("MEMBERS", $scope.members)

            for (let mem in $scope.members) {
                for (let mem2 in $scope.members) {
                    if (!($scope.members[mem].id === $scope.members[mem2].id) && (mem2 > mem)) {
                        let key = ([$scope.members[mem].personality, $scope.members[mem2].personality].sort()[0] + ":" +
                            [$scope.members[mem].personality, $scope.members[mem2].personality].sort()[1]
                        );
                        let ac = $scope.compatibilities[key];
                        $scope.team_total += ac;
                        $scope.comps.push(key);
                        console.log([$scope.members[mem].name, $scope.members[mem2].name].sort())
                        console.log($scope.members[mem].personality, $scope.members[mem2].personality, ac);
                        console.log("team_total", $scope.team_total)
                    }
                }
            }
            console.log("total", $scope.team_total, "possible", (5 * $scope.comps.length), "percent", ($scope.team_total / ($scope.comps.length * 5)));
            var tp = ($scope.team_total / ($scope.comps.length * 5));
            console.log(Math.floor(tp * 100));
            $scope.team_percentage = Math.floor(tp * 100);
            if ($scope.team_percentage >= 0 && $scope.team_percentage <= 33) {
                $scope.team_compatibility_color = {"color": "#f44336"};
            } else if ($scope.team_percentage >= 34 && $scope.team_percentage <= 66) {
                $scope.team_compatibility_color = {"color": "#ffeb3b"};
            } else {
                $scope.team_compatibility_color = {"color": "#8BC34A"};
            }
            console.log("team_compatibility_color", $scope.team_compatibility_color);
        }
    }
        )


