document.addEventListener("DOMContentLoaded", function () {
    let modal = document.getElementById('postModal');
    let openPostModal = document.getElementById('openPostModal');
    let closeModalBtn = document.getElementById('closeModal');

    if (!modal || !openPostModal || !closeModalBtn) {
        console.error("Modal elements not found! Check IDs in your HTML.");
        return;
    }

    function openCreateModal() {
        document.getElementById('postId').value = "";
        document.getElementById('postDescription').value = "";
        document.getElementById('modalTitle').innerText = "Create post";
        document.getElementById('submitButton').innerText = "Post";

        modal.classList.remove('hidden');
        modal.style.display = "flex"; 
    }

    function closeModal() {
        modal.classList.add('hidden');
        modal.style.display = "none"; 
    }

    // Attach event listeners
    openPostModal.addEventListener("click", openCreateModal);
    closeModalBtn.addEventListener("click", closeModal);
});
