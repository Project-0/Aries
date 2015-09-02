var ariesApp = angular.module('ariesApp', []);

ariesApp.controller('', function($scope) {
	$scope.application = {
		'name': 'Aries',
		'version': '0.1',
		'journal_path': '/',
	};
});