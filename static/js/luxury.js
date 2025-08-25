// Luxury Real Estate Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all luxury components
    initLuxuryLoader();
    initLuxuryNavbar();
    initLuxuryTheme();
    initLuxuryScrollTop();
    initLuxuryAnimations();
    initLuxuryCards();
    initLuxuryForms();
    initLuxuryParallax();
});

// Luxury Loader
function initLuxuryLoader() {
    const loader = document.getElementById('luxury-loader');
    
    // Hide loader after page load
    window.addEventListener('load', function() {
        setTimeout(() => {
            loader.classList.add('hidden');
            document.body.style.overflow = 'visible';
        }, 1500);
    });
    
    // Hide loader if taking too long
    setTimeout(() => {
        loader.classList.add('hidden');
        document.body.style.overflow = 'visible';
    }, 3000);
}

// Luxury Navbar
function initLuxuryNavbar() {
    const navbar = document.querySelector('.luxury-navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add scrolled class
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Luxury Theme Toggle
function initLuxuryTheme() {
    const themeToggle = document.querySelector('.luxury-theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const body = document.body;
    
    // Load saved theme
    const savedTheme = localStorage.getItem('luxury-theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        if (themeIcon) themeIcon.className = 'fas fa-sun';
    }
    
    // Theme toggle event
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            toggleLuxuryTheme();
        });
    }
}

function toggleLuxuryTheme() {
    const body = document.body;
    const themeIcon = document.getElementById('theme-icon');
    
    body.classList.toggle('dark-mode');
    
    if (body.classList.contains('dark-mode')) {
        if (themeIcon) themeIcon.className = 'fas fa-sun';
        localStorage.setItem('luxury-theme', 'dark');
        showLuxuryNotification('تم تفعيل الوضع المظلم الفاخر', 'success');
    } else {
        if (themeIcon) themeIcon.className = 'fas fa-moon';
        localStorage.setItem('luxury-theme', 'light');
        showLuxuryNotification('تم تفعيل الوضع المضيء الفاخر', 'success');
    }
}

// Luxury Scroll to Top
function initLuxuryScrollTop() {
    const scrollTopBtn = document.getElementById('scrollTop');
    
    if (!scrollTopBtn) {
        // Create scroll to top button if it doesn't exist
        const btn = document.createElement('button');
        btn.id = 'scrollTop';
        btn.className = 'luxury-scroll-top';
        btn.innerHTML = '<i class="fas fa-chevron-up"></i>';
        btn.setAttribute('aria-label', 'العودة للأعلى');
        document.body.appendChild(btn);
    }
    
    const scrollBtn = document.getElementById('scrollTop');
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.classList.add('show');
        } else {
            scrollBtn.classList.remove('show');
        }
    });
    
    // Smooth scroll to top
    scrollBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Luxury Animations
function initLuxuryAnimations() {
    // Initialize AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            easing: 'ease-out-cubic',
            once: true,
            offset: 100
        });
    }
    
    // Custom intersection observer for luxury animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                
                // Add luxury glow effect
                if (entry.target.classList.contains('luxury-glow')) {
                    entry.target.style.boxShadow = 'var(--luxury-shadow-gold)';
                }
            }
        });
    }, observerOptions);
    
    // Observe luxury elements
    document.querySelectorAll('.luxury-animate, .luxury-card, .property-card-luxury').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        observer.observe(el);
    });
    
    // Stagger animations for luxury lists
    document.querySelectorAll('.luxury-stagger').forEach((container, containerIndex) => {
        const items = container.children;
        Array.from(items).forEach((item, index) => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(30px)';
            item.style.transition = `all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) ${index * 0.15}s`;
            observer.observe(item);
        });
    });
}

// Luxury Cards
function initLuxuryCards() {
    // Add hover effects to luxury cards
    document.querySelectorAll('.luxury-card, .property-card-luxury').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Property card image overlay effects
    document.querySelectorAll('.property-card-luxury').forEach(card => {
        const img = card.querySelector('.card-img-top');
        if (img) {
            card.addEventListener('mouseenter', function() {
                img.style.transform = 'scale(1.1)';
                img.style.filter = 'brightness(1.1)';
            });
            
            card.addEventListener('mouseleave', function() {
                img.style.transform = 'scale(1)';
                img.style.filter = 'brightness(1)';
            });
        }
    });
}

// Luxury Forms
function initLuxuryForms() {
    // Add floating label effects
    document.querySelectorAll('.luxury-form-control').forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
            this.style.borderColor = 'var(--luxury-gold)';
            this.style.boxShadow = '0 0 0 0.2rem rgba(212, 175, 55, 0.25)';
        });
        
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
            this.style.borderColor = 'var(--luxury-light-gray)';
            this.style.boxShadow = 'none';
        });
        
        // Check if input has value on load
        if (input.value) {
            input.parentElement.classList.add('focused');
        }
    });
    
    // Form validation with luxury styling
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('.luxury-form-control[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'var(--luxury-burgundy)';
                    input.style.boxShadow = '0 0 0 0.2rem rgba(139, 0, 0, 0.25)';
                    isValid = false;
                } else {
                    input.style.borderColor = 'var(--luxury-emerald)';
                    input.style.boxShadow = '0 0 0 0.2rem rgba(80, 200, 120, 0.25)';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showLuxuryNotification('يرجى ملء جميع الحقول المطلوبة', 'error');
            }
        });
    });
}

// Luxury Parallax Effect
function initLuxuryParallax() {
    const parallaxElements = document.querySelectorAll('.luxury-parallax');
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        
        parallaxElements.forEach(element => {
            const rate = scrolled * -0.5;
            element.style.transform = `translateY(${rate}px)`;
        });
    });
}

// Luxury Notification System
function showLuxuryNotification(message, type = 'info', duration = 5000) {
    // Create notification container if it doesn't exist
    let container = document.querySelector('.luxury-messages');
    if (!container) {
        container = document.createElement('div');
        container.className = 'luxury-messages';
        document.body.appendChild(container);
    }
    
    const notification = document.createElement('div');
    notification.className = `luxury-alert luxury-alert-${type}`;
    
    let icon = 'fas fa-info-circle';
    if (type === 'success') icon = 'fas fa-check-circle';
    if (type === 'error') icon = 'fas fa-exclamation-circle';
    if (type === 'warning') icon = 'fas fa-exclamation-triangle';
    
    notification.innerHTML = `
        <div class="alert-content">
            <i class="${icon}"></i>
            <span>${message}</span>
            <button type="button" class="luxury-close" onclick="this.parentElement.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    // Add entrance animation
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(100%)';
    container.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transition = 'all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after duration
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.opacity = '0';
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                notification.remove();
            }, 500);
        }
    }, duration);
}

// Luxury Image Lazy Loading
function initLuxuryImageLazyLoading() {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Utility Functions
function luxuryDebounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function luxuryThrottle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Copy to Clipboard with Luxury Style
function luxuryCopyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showLuxuryNotification('تم نسخ النص بنجاح', 'success');
    }).catch(() => {
        showLuxuryNotification('فشل في نسخ النص', 'error');
    });
}

// Share Content with Luxury Style
function luxuryShareContent(title, text, url) {
    if (navigator.share) {
        navigator.share({
            title: title,
            text: text,
            url: url
        }).then(() => {
            showLuxuryNotification('تم مشاركة المحتوى بنجاح', 'success');
        });
    } else {
        luxuryCopyToClipboard(url);
    }
}

// Export functions for global use
window.showLuxuryNotification = showLuxuryNotification;
window.toggleLuxuryTheme = toggleLuxuryTheme;
window.luxuryCopyToClipboard = luxuryCopyToClipboard;
window.luxuryShareContent = luxuryShareContent;
