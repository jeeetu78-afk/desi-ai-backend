async function send() {
  let text = document.getElementById("text").value;

  document.getElementById("reply").innerText = "🤖 Desi AI soch raha hai...";

  try {
    const response = await fetch("https://YOUR_RENDER_URL.onrender.com/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt: text })
    });

    const data = await response.json();
    document.getElementById("reply").innerText = "😂 Desi AI: " + data.reply;

  } catch (error) {
    document.getElementById("reply").innerText =
      "❌ Error: Backend connect nahi ho raha";
  }
}
