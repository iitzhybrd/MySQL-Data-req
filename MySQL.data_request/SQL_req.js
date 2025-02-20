document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const data = {
        username: username,
        password: password,
    };

    fetch("http://127.0.0.1:5000/submit_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((result) => {
        document.getElementById("result").innerHTML = result.message;

        // After submitting data, also retrieve and display data
        retrieveAndDisplayData();
    });
});

// Function to retrieve and display data
function retrieveAndDisplayData() {
    fetch("http://127.0.0.1:5000/get_data")
        .then((response) => response.json())
        .then((data) => {
            const dataTable = document.getElementById("data-table");
            let tableHTML = "";

            // Loop through the retrieved data and create table rows
            data.forEach((row) => {
                tableHTML += `<tr><td>${row.username}</td><td>${row.password}</td><td>${row.create_time}</td></tr>`;
            });

            dataTable.innerHTML = tableHTML;
        })
        .catch((error) => {
            console.error("Error fetching data:", error);
        });
}
