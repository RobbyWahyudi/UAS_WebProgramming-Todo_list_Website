document.addEventListener("DOMContentLoaded", function () {
  var deleteButtons = document.querySelectorAll(".delete-task");

  deleteButtons.forEach(function (button) {
    button.addEventListener("click", function (event) {
      event.preventDefault();

      var taskId = button.getAttribute("data-task-id");
      var confirmation = confirm("Apakah kamu yakin ingin menghapus list ini?");

      if (confirmation) {
        window.location.href = "/delete_task/" + taskId + "/";
      }
    });
  });
});
