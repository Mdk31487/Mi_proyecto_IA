console.log("Script cargado correctamente.");
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            const username = document.getElementById("username").value;

            try {
                const response = await fetch("/generate_token/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ username })
                });

                if (!response.ok) throw new Error("Error al generar el token");

                const result = await response.json();
                localStorage.setItem("access_token", result.access_token);
                alert("Token generado correctamente.");
                window.location.href = "/dashboard.html";
            } catch (error) {
                alert("Error: " + error.message);
            }
        });
    }
});
