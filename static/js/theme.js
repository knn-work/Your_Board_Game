document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("theme-toggle");
    const htmlElement = document.documentElement;
    const currentTheme = localStorage.getItem("theme") || "light";

    htmlElement.setAttribute("data-bs-theme", currentTheme);
    updateIcon(currentTheme);

    toggleButton.addEventListener("click", function () {
        const newTheme = htmlElement.getAttribute("data-bs-theme") === "light" ? "dark" : "light";
        htmlElement.setAttribute("data-bs-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        updateIcon(newTheme);
    });

    function updateIcon(theme) {
        toggleButton.innerHTML = theme === "dark" ? "☀️" : "🌙";
    }
});
