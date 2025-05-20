const flights = document.getElementById("available-flights");

const postmyrequest = async () => {
  const response = await axios.get("/booking/get_flights", {});
  if (response) {
    flights.textContent = "";
    for (let i in response["flights"]) {

      let node = document.createElement("p");
      node.textContent = `destination: ${i["destination"]} departure: ${i["depart"]}`;
      flights.appendChild(node);
    }
  }
};

document.addEventListener("DOMContentLoaded", function () {
  postmyrequest();
});
