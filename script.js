// This file contains the JavaScript code that handles the API call to the backend when the "Translate" button is clicked. It fetches the translation and updates the UI with the result.

const translateButton = document.getElementById('translate-button');
const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');

translateButton.addEventListener('click', async () => {
    const hindiText = inputText.value;

    if (hindiText.trim() === '') {
        outputText.innerText = 'Please enter text to translate.';
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: hindiText }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        outputText.innerText = data.translated_text;
    } catch (error) {
        outputText.innerText = 'Error: ' + error.message;
    }
});