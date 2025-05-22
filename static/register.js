const feedbackmessage = document.getElementById("feedbackmessage");
const login_return = document.getElementById("return-login");

document.getElementById("register").addEventListener("submit", function(e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;

  const postmyrequest = async () => {
    const response = await axios.post("/register/register_user", {
      username: username,
      password: password,
      email: email,
    });
    if (response) {
      feedbackmessage.textContent = response.data.message;
      if (response.status == 201) {
        login_return.innerHTML = `
          <a href="/login" class="btn expand-on-hover">Login
          </a> 
        `;
      }
    }
  };

  postmyrequest();
});
