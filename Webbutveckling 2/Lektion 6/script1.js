const question = document.getElementById('question');
const answerInput = document.getElementById('answer');
const submitButton = document.getElementById('submit-answer');

submitButton.addEventListener('click', () => {
    const userAnswer = answerInput.value.trim().toLowerCase();
    if (userAnswer === 'stockholm') {
        alert('Korrekt svar!');
    } else {
        alert('Fel svar. Försök igen!');
    }
});
