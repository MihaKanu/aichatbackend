document.getElementById('send-button').addEventListener('click', async () => {
    const prompt = document.getElementById('input-text').value;
    const responseContainer = document.getElementById('response-container');

    // Replace with your deployed backend URL
    const response = await fetch('https://your-backend-url.onrender.com/generate_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    responseContainer.textContent = data.response;
});
