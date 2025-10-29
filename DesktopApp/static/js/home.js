document.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('blockchain-bg');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            let width = window.innerWidth;
            let height = window.innerHeight;
            canvas.width = width;
            canvas.height = height;

            let particles = [];
            let particleCount = Math.floor((width * height) / 10000);
            let connectDistance = Math.min(width, height) / 8;

            class Particle {
                constructor() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.vx = (Math.random() - 0.5) * 0.5;
                    this.vy = (Math.random() - 0.5) * 0.5;
                    this.radius = Math.random() * 2 + 1.5;
                }

                draw() {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(244, 244, 244, 0.7)';
                    ctx.fill();
                }

                update() {
                    this.x += this.vx;
                    this.y += this.vy;
                    if (this.x < 0 || this.x > width) this.vx *= -1;
                    if (this.y < 0 || this.y > height) this.vy *= -1;
                }
            }

            function init() {
                particles = [];
                for (let i = 0; i < particleCount; i++) {
                    particles.push(new Particle());
                }
            }

            function connect() {
                for (let i = 0; i < particles.length; i++) {
                    for (let j = i + 1; j < particles.length; j++) {
                        const dx = particles[i].x - particles[j].x;
                        const dy = particles[i].y - particles[j].y;
                        const distance = Math.sqrt(dx * dx + dy * dy);

                        if (distance < connectDistance) {
                            ctx.beginPath();
                            ctx.moveTo(particles[i].x, particles[i].y);
                            ctx.lineTo(particles[j].x, particles[j].y);
                            ctx.strokeStyle = `rgba(220, 220, 220, ${1 - distance / connectDistance})`;
                            ctx.lineWidth = 1;
                            ctx.stroke();
                        }
                    }
                }
            }

            function animate() {
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => {
                    p.update();
                    p.draw();
                });
                connect();
                requestAnimationFrame(animate);
            }

            window.addEventListener('resize', () => {
                width = window.innerWidth;
                height = window.innerHeight;
                canvas.width = width;
                canvas.height = height;
                
                particleCount = Math.floor((width * height) / 10000);
                particles = [];
                for (let i = 0; i < particleCount; i++) {
                    particles.push(new Particle());
                }
                connectDistance = Math.min(width, height) / 8;
            });

            init();
            animate();
            
            // Modal Handling
            const overlay = document.getElementById('modal-overlay');
            const uploadBtn = document.getElementById('open-upload-btn');
            const createBtn = document.getElementById('open-create-btn');
            const uploadModal = document.getElementById('upload-modal');
            const createModal = document.getElementById('create-modal');
            const closeBtns = document.querySelectorAll('.modal-close');
            const dropArea = document.querySelector('.drag-drop-area');
            const fileInput = document.getElementById('file-input');

            const openModal = (modal) => {
                if (modal == null) return;
                overlay.classList.add('active');
                modal.classList.add('active');
            };

            const closeModal = (modal) => {
                if (modal == null) return;
                overlay.classList.remove('active');
                modal.classList.remove('active');
            };

            if (uploadBtn) {
                uploadBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    openModal(uploadModal);
                });
            }

            if (createBtn) {
                createBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    openModal(createModal);
                });
            }

            if (overlay) {
                overlay.addEventListener('click', () => {
                    closeModal(uploadModal);
                    closeModal(createModal);
                });
            }

            closeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const modalId = btn.getAttribute('data-modal');
                    const modal = document.getElementById(modalId);
                    closeModal(modal);
                });
            });
            
            // Drag and Drop Handling
            if (dropArea) {
                // Add click listener to trigger file input
                dropArea.addEventListener('click', () => {
                    fileInput.click();
                });

                fileInput.addEventListener('change', (e) => {
                    handleFiles(e.target.files);
                });

                // Prevent default drag behaviors
                ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                    dropArea.addEventListener(eventName, preventDefaults, false);
                    document.body.addEventListener(eventName, preventDefaults, false); // Prevent browser from opening file
                });

                function preventDefaults(e) {
                    e.preventDefault();
                    e.stopPropagation();
                }

                // Highlight drop area when item is dragged over it
                ['dragenter', 'dragover'].forEach(eventName => {
                    dropArea.addEventListener(eventName, highlight, false);
                });

                ['dragleave', 'drop'].forEach(eventName => {
                    dropArea.addEventListener(eventName, unhighlight, false);
                });

                function highlight(e) {
                    dropArea.classList.add('drag-over');
                }

                function unhighlight(e) {
                    dropArea.classList.remove('drag-over');
                }

                // Handle dropped files
                dropArea.addEventListener('drop', handleDrop, false);

                function handleDrop(e) {
                    let dt = e.dataTransfer;
                    let files = dt.files;

                    handleFiles(files);
                }

                function handleFiles(files) {
                    files = [...files];
                    if (files.length > 0) {
                        const p = dropArea.querySelector('p');
                        p.innerHTML = `<strong>File selected:</strong> ${files[0].name}`;
                        
                        console.log('File(s) dropped:', files);
                        
                        // Optional: close modal after 2s and reset text
                        setTimeout(() => {
                            closeModal(uploadModal);
                            // Reset text after modal is closed
                            setTimeout(() => {
                                p.innerHTML = `Drag & drop files here or <strong>click to select</strong>`;
                                fileInput.value = ''; // Clear the file input
                            }, 300); // 300ms matches CSS transition
                        }, 2000);
                    }
                }
            }
        });