// Check login status when the page loads
document.addEventListener("DOMContentLoaded", function () {
  checkLoginStatus();
});

function checkLoginStatus() {
  // Assuming you have a function to get the login status
  const isLoggedIn = getLoginStatus(); // Replace with your actual login status check

  if (isLoggedIn) {
    document.getElementById("login-link").style.display = "none";
    document.getElementById("logout-link").style.display = "block";
  } else {
    document.getElementById("login-link").style.display = "block";
    document.getElementById("logout-link").style.display = "none";
  }
}

function getLoginStatus() {
  // This function should return true if the user is logged in, false otherwise
  // For example, you can check if a token is stored in localStorage
  return localStorage.getItem("userToken") !== null;
}

function logout() {
  // Clear the user token or perform any necessary logout actions
  localStorage.removeItem("userToken");
  // Redirect to login page or refresh to update the header
  window.location.href = "login.html";
}
