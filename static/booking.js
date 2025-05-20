const flights = document.getElementById("available-flights");

const getmyrequest = async () => {
  const response = await axios.get("/booking/get_flights", {});
  if (response) {
    flights.textContent = "";
    for (let i in response.data.message) {
      console.log(i);
      let node = document.createElement("option");
      node.textContent = `${response.data.message[i]["depart"]} ${"\u2192"} ${response.data.message[i]["destination"]}`;
      node.value = i;
      flights.appendChild(node);
    }
    console.log(response.data.message);
  }
};

document.addEventListener("DOMContentLoaded", function () {
  getmyrequest();
});
