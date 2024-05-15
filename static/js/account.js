// code will run when loaded
document.addEventListener('DOMContentLoaded', function() {
    // gets the username and email elements.
    var usernameElement = document.getElementById('username');
    var emailElement = document.getElementById('email');

    // gets the recipe requests element.
    var recipeRequestsElement = document.getElementById('recipeRequests');

    // add logic to request user data (email/password/username) --> sending a request to server/getting data from a database tbd
    // leaving in random stuff so the iteration works

    usernameElement.textContent = 'ExampleUser';
    emailElement.textContent = 'exampleuser@example.com';

    var recipeRequests = ['Recipe 1', 'Recipe 2', 'Recipe 3'];

    for (var i = 0; i < recipeRequests.length; i++) {
        var listItem = document.createElement('li');
        listItem.textContent = recipeRequests[i];
        recipeRequestsElement.appendChild(listItem);
    }
});
