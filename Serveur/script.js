document.addEventListener("DOMContentLoaded", function() {
    const menuButton = document.getElementById("menuButton");
    const dropdown = document.querySelector(".dropdown");

    menuButton.addEventListener("click", function() {
        if (dropdown.style.display === "none" || dropdown.style.display === "") {
            dropdown.style.display = "flex";
        } else {
            dropdown.style.display = "none";
        }
    });
});
