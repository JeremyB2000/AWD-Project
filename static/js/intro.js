
 var handleSearchFunction = false;
  function handleSearch() {
      if(window.innerWidth<=700){
          var title = document.getElementById('title');
          var select = document.getElementById('select');
            var searchInput = document.getElementById('search-input');
            var searchButton = document.getElementById('search-button');
            var loginButton = document.getElementById('login-button');
            var registerButton = document.getElementById('register-button');

        title.style.display = 'none';
        loginButton.style.display = 'none';
        registerButton.style.display = 'none';

        searchInput.style.display = 'block';
        searchButton.style.display = 'block';
        select.style.display = 'block';
        handleSearchFunction = true;
      }
  }

  function handleWindowResize() {
      var windowWidth = window.innerWidth;
    var loginButton = document.getElementById('login-button');
    var registerButton = document.getElementById('register-button');
    var title = document.getElementById('title');
    var select = document.getElementById('select');
    var searchInput = document.getElementById('search-input');
    if (windowWidth >= 700) {
        select.style.display='inline-block';
        searchInput.style.display='inline-block';
        title.style.display='inline-block';
        loginButton.style.display='inline-block';
        registerButton.style.display='inline-block';
    }
    else{
        select.style.display='none';
        searchInput.style.display='none'
    }
  }
  var previousWidth = window.innerWidth;
  function handleWindowinsize() {
    var loginButton = document.getElementById('login-button');

    var registerButton = document.getElementById('register-button');
    var title = document.getElementById('title');
     var select = document.getElementById('select');
    var searchInput = document.getElementById('search-input');
    var searchButton = document.getElementById('search-button');
    var currentWidth = window.innerWidth;
    if (handleSearchFunction&&currentWidth >previousWidth&&currentWidth<=700) {
        searchInput.style.display = 'block';
        searchButton.style.display = 'block';
        select.style.display = 'block';
    }else {
        title.style.display='inline-block';
        loginButton.style.display='inline-block';
        registerButton.style.display='inline-block';
        handleSearchFunction = false;
    }
    previousWidth = currentWidth; // 更新先前的窗口宽度
  }
  window.addEventListener('resize', handleWindowResize);
  window.addEventListener('resize', handleWindowinsize);