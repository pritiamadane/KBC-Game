// Display an alert message when the user clicks the "Submit Answer" button
document.addEventListener('DOMContentLoaded', function () {
  const submitButtons = document.querySelectorAll('button[type="submit"]');
  
  submitButtons.forEach(button => {
      button.addEventListener('click', function () {
          alert('Your answer has been submitted!');
      });
  });
});
