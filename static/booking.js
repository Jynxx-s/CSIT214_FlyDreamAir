const flights = document.getElementById("available-flights");
const seatdiv = document.getElementById("seats-div");
let seats;
const selectedSeats = [];
let bflight_id;

const getmyrequest = async () => {
  const response = await axios.get("/booking/get_flights", {});
  if (response) {
    flights.textContent = "";
    flights.innerHTML =
      "<option value='' disabled selected>Please select a flight</option>";
    for (let i in response.data.message) {
      console.log(i);
      let node = document.createElement("option");
      node.textContent = `${response.data.message[i]["depart"]} ${"\u2192"} ${response.data.message[i]["destination"]}`;
      node.value = response.data.message[i]["flight_id"];
      flights.appendChild(node);
    }
    console.log(response.data.message);
  }
};

document
  .getElementById("available-flights")
  .addEventListener("change", async function() {
    const flight_id = this.value;

    bflight_id = flight_id;
    console.log(flight_id);
    const response = await axios.post("/booking/get_seats", {
      flight_id: flight_id,
    });
    seats = response.data.message;
    seatdiv.innerHTML = "";
    for (let i in seats) {
      let node = document.createElement("div");
      for (let j in seats[i]) {
        let innernode = document.createElement("div");
        innernode.innerText = j.charAt(0).toUpperCase() + j.slice(1);
        innernode.dataset.value = j;
        if (seats[i][j] == "a") {
          innernode.classList.add("available");
          innernode.addEventListener("click", function() {
            innernode.classList.toggle("clicked");
            get_selected_seat();
          });
          innernode.classList.add("expand-on-hover");
          innernode.classList.add("cool-button");
        } else {
          innernode.classList.add("unavailable");
        }
        innernode.classList.add("seatbtn");
        node.classList.add("row-div");
        node.appendChild(innernode);
      }
      seatdiv.appendChild(node);
    }
  });
function get_selected_seat() {
  selectedSeats.length = 0;
  const clickedSeats = seatdiv.querySelectorAll(".clicked");
  for (let i = 0; i < clickedSeats.length; i++) {
    selectedSeats.push(clickedSeats[i].dataset.value);
  }
}



document.getElementById("book_flight").addEventListener("click", function(e) {
  e.preventDefault();

  const postmyrequest = async () => {
    const response = await axios.post("/booking/create_booking", {

      seats : selectedSeats,
      flight_id : bflight_id,
    });
  };

  postmyrequest();
});
document.addEventListener("DOMContentLoaded", function() {
  getmyrequest();
});
