function showProfileDropdown() {
    document.getElementById("profileDropdown").classList.toggle("show");
  }

function showQuestion(){
  var user_question = document.getElementById("question").value;
  document.getElementById("printedquestion").innerHTML=user_question;
}

function clearForm() {
  var input = document.getElementById("question").value
  input.reset()
}
