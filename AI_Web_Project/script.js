function sendMessage() {

    let input = document.getElementById("user-input");
    let userMessage = input.value;

    if (userMessage.trim() === "") {
        return;
    }

    let message = userMessage.toLowerCase();

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML +=
        "<div class='user'><b>You:</b> " +
        userMessage +
        "</div>";

    let reply = "";

    if (message.includes("volunteer")) {

        reply = "You can volunteer by registering with NayePankh Foundation and participating in events.";

    } else if (message.includes("donate")) {

        reply = "You can support NayePankh Foundation through donations and awareness campaigns.";

    } else if (message.includes("python")) {

        reply = "Start with Python basics, functions, OOP, SQLite, and Tkinter projects.";

    } else if (message.includes("data analytics")) {

        reply = "Learn Excel, SQL, Pandas, Matplotlib, Power BI, and Statistics.";

    } else if (message.includes("machine learning")) {

        reply = "Start with Python, Statistics, Pandas, Scikit-Learn, and ML projects.";

    } else if (message.includes("ai")) {

        reply = "AI can automate volunteer management, content creation, and awareness campaigns.";

    } else if (message.includes("internship")) {

        reply = "NayePankh Foundation offers internships in Python, AI, Data Analytics, Web Development and more.";

    } else {

        reply = "Thank you for your question. Please visit the NayePankh Foundation website for more information.";
    }

    chatBox.innerHTML +=
        "<div class='bot'><b>AI Assistant:</b> " +
        reply +
        "</div>";

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}