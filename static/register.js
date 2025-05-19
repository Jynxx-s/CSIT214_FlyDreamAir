const feedbackmessage = document.getElementById("feedbackmessage");
document.getElementById("register").addEventListener("submit", function (e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;

  const postmyrequest = async () => {
    const response = await axios.post("/register/register_user", {
      username: username,
      password: password,
      email: email
    });
    if (response){
      feedbackmessage.textContent = response.data.message;
    }
  };

  postmyrequest();

});
