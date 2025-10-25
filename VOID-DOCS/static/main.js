document.addEventListener('DOMContentLoaded', (event) => {
            
            const sideMenu = document.getElementById("side");
            const howButton = document.getElementById("how");
            const menuIcon = document.getElementById("menu-icon");
            const closeIcon = document.getElementById("close-icon");

            function side_slide() {
                sideMenu.classList.toggle("active");

                if (sideMenu.classList.contains("active")) {
                    menuIcon.style.display = 'none';
                    closeIcon.style.display = 'block';
                } else {
                    menuIcon.style.display = 'block';
                    closeIcon.style.display = 'none';
                }
            }

            if (howButton) {
                howButton.addEventListener("click", side_slide);
            }
            
            const uploadModal = document.getElementById("upload-modal");
            const showModalButton = document.getElementById("show-upload-modal");
            const closeModalButton = document.getElementById("modal-close");
            
            function showModal(e) {
                e.preventDefault();
                uploadModal.classList.add("active");
            }
            
            function hideModal() {
                uploadModal.classList.remove("active");
            }
            
            if (showModalButton) {
                showModalButton.addEventListener("click", showModal);
            }
            
            if (closeModalButton) {
                closeModalButton.addEventListener("click", hideModal);
            }
            
            if (uploadModal) {
                uploadModal.addEventListener("click", function(e) {
                    if (e.target === uploadModal) {
                        hideModal();
                    }
                });
            }

        });