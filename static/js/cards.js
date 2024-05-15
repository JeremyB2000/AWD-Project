//Changes the colour of each request status based on the text in the .status class field.
const request_status = document.querySelectorAll('.status'); 
request_status.forEach(request_status => {
  if (request_status.textContent.trim() === 'Complete') {
    request_status.classList.add('green');
  } else if (request_status.textContent.trim() === 'Incomplete') {
    request_status.classList.add('blue');
  }
})


function openComments(button) {
  const comSection = button.nextElementSibling;
  if (comSection.style.display == 'none' || comSection.style.display == '') {
    comSection.style.display = 'block';
} else {
    comSection.style.display = 'none';
}}

function newComment(recipeId) {
  const comment = document.getElementById(recipeId).value;

  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/auth/comment", true);
  xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4) {
      if (xhttp.status === 200) {
        const response = JSON.parse(xhttp.responseText); //create an object for the server response
        
        //Create a div with class and id. Isnide the div put the username and comment
        const commentContainer = document.createElement("div");
        commentContainer.classList.add("comment-card");
        commentContainer.setAttribute("id", "${response.comment_id}") //comment id id not used yet but might use in future.
        commentContainer.innerHTML = `<h6>${response.username}</h6><p>${response.comment}</p>`;

        //Get the form element by finding the parent node of the elemtn with the corresponding recipeId
        const parent = document.getElementById(recipeId).parentNode
        parent.insertAdjacentElement('beforebegin', commentContainer);//add the new comment before the form
        
      } else {
        console.error("Error:", xhttp.statusText);
      }
    }
  };
    xhttp.onerror = function() {
    console.error("Comment Failed");
  };
  
  const comment_data = "comment=" + encodeURIComponent(comment) + "&recipe_id=" + encodeURIComponent(recipeId);
  xhttp.send(comment_data);
}

