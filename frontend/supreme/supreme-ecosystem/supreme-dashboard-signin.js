"use strict";
const API = "https://supremesetuhub-3v4e.onrender.com";
const form = document.getElementById("signInForm");
const button = document.getElementById("submitButton");
const message = document.getElementById("message");
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  button.disabled = true;
  button.textContent = "SIGNING IN...";
  message.textContent = "VERIFYING SUPREME OWNER ACCESS...";
  try {
    const response = await fetch(API + "/auth/signin", {
      method: "POST",
      headers: {"Content-Type": "application/json", "Accept": "application/json"},
      body: JSON.stringify({
        username: document.getElementById("username").value.trim(),
        password: document.getElementById("password").value
      })
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || data.message || "SIGN IN FAILED.");
    const token = data.token || data.access_token;
    if (!token) throw new Error("AUTHENTICATION TOKEN WAS NOT RETURNED.");
    const check = await fetch(API + "/supreme/status", {headers: {Authorization: "Bearer " + token, Accept: "application/json"}});
    if (!check.ok) throw new Error(check.status === 403 ? "SUPREME IS PRIVATE. OWNER ACCESS ONLY." : "OWNER SESSION COULD NOT BE VERIFIED.");
    localStorage.setItem("supreme_token", token);
    message.textContent = "SIGN IN SUCCESSFUL. OPENING SUPREME...";
    window.location.replace("supreme-dashboard.html");
  } catch (error) {
    message.textContent = error.message || "SIGN IN FAILED. PLEASE TRY AGAIN.";
    button.disabled = false;
    button.textContent = "SIGN IN TO SUPREME";
  }
});
