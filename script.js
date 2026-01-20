async function send() {
  let text = document.getElementById("text").value;
  document.getElementById("reply").innerText = "🤖 Desi AI soch raha hai...";

  try {
    const res = await fetch("https://YOUR_RENDER_URL.onrender.com/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
    });

    const data = await res.json();
    document.getElementById("reply").innerText =
      "😂 Desi AI: " + data.reply;

  } catch (err) {
    document.getElementById("reply").innerText =
      "❌ Backend se connect nahi ho raha";
  }
}
