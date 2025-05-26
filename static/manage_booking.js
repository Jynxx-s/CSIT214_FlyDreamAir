booked_flights = document.getElementById("bookings");
const getbookings = async () => {
  const response = await axios.get("/booking/get_bookings", {});
  data = response.data.message;
  for (let i = 0; i < data.length; i++) {
    const booking = data[i];

    const bookingDiv = document.createElement("div");
    bookingDiv.classList.add("booking-div");

    const bookingInfo = document.createElement("div");
    bookingInfo.classList.add("booking-info");

    const destDiv = document.createElement("div");
    destDiv.classList.add("booking-item");
    destDiv.innerText = "Destination: " + booking.destinaton;

    const depDiv = document.createElement("div");
    depDiv.classList.add("booking-item");
    depDiv.innerText = "Departure: " + booking.departure;

    const seatsDiv = document.createElement("div");
    seatsDiv.classList.add("booking-item");
    seatsDiv.innerText = "Seats: " + booking.seats.join(", ");

    bookingInfo.appendChild(destDiv);
    bookingInfo.appendChild(depDiv);
    bookingInfo.appendChild(seatsDiv);

    const deleteButton = document.createElement("div");
    deleteButton.classList.add("delete");
    deleteButton.innerText = "Delete";
    deleteButton.onclick = () => {
      axios
        .post("/booking/delete_booking", { booking_id: booking.booking_id })
        .then(() => {
          location.reload();
        });
    };

    bookingDiv.appendChild(bookingInfo);
    bookingDiv.appendChild(deleteButton);

    booked_flights.appendChild(bookingDiv);
  }
};

document.addEventListener("DOMContentLoaded", function() {
  getbookings();
});
