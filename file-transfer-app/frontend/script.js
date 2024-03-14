function uploadFiles() {
  var files = document.getElementById('fileInput').files;
  var fileList = document.getElementById('fileList');

  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var listItem = document.createElement('li');
    listItem.textContent = file.name;
    fileList.appendChild(listItem);
  }
}
