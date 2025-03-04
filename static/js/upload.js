document.addEventListener('DOMContentLoaded', function () {
  const dropArea = document.getElementById('drop-area');
  const fileInput = document.querySelector('#drop-area>input[type="file"]');

  dropArea.addEventListener('click', () => {
    if (!fileInput.disabled) {
      fileInput.click();
    }
  });

  fileInput.addEventListener('change', () => {
    change(fileInput, dropArea);
  });

  dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('bg-gray-100');
  });

  dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('bg-gray-100');
  });

  dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('bg-gray-100');

    const file = event.dataTransfer.files[0];
    fileInput.files = event.dataTransfer.files;

    change(fileInput, dropArea)
  });
});

const change = (fileInput, dropArea) => {
    const file = fileInput.files[0];
    if (file) {
      dropArea.classList.add("pointer-events-none");
      dropArea.classList.remove("hover:bg-gray-50");
      dropArea.querySelector('label').innerHTML = `Image: ${file.name} was added`;
    }
}
