
document.getElementById("login-form").addEventListener("submit", function(e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const postmyrequest = async () => {
    const response = await axios.post("/login", {
      username: username,
      password: password,
    });
  };

  postmyrequest();
});
