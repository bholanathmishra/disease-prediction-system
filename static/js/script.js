// Smooth scroll for nav links
document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// Placeholder form submit alert
document.getElementById("predictForm").addEventListener("submit", function(e){
    e.preventDefault();
    alert("Prediction functionality will be integrated here.");
});
