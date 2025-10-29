document.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('blockchain-bg');
            const ctx = canvas.getContext('2d');

            let width = window.innerWidth;
            let height = window.innerHeight;
            canvas.width = width;
            canvas.height = height;

            let particles = [];
            // Responsive particle count
            const particleCount = Math.floor((width * height) / 20000);
            const connectDistance = Math.min(width, height) / 8;

            class Particle {
                constructor() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.vx = (Math.random() - 0.5) * 0.5;
                    this.vy = (Math.random() - 0.5) * 0.5;
                    this.radius = Math.random() * 1.5 + 1;
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
                            ctx.strokeStyle = `rgba(204, 204, 204, ${1 - distance / connectDistance})`;
                            ctx.lineWidth = 0.5;
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
                // Recalculate particle count and distance on resize
                const newParticleCount = Math.floor((width * height) / 20000);
                particles = [];
                for (let i = 0; i < newParticleCount; i++) {
                    particles.push(new Particle());
                }
                connectDistance = Math.min(width, height) / 8;
            });

            init();
            animate();
        });