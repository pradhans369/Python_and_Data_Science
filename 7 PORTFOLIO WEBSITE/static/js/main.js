/**
 * Biswajeet Pradhan - Portfolio Scripts
 * Clean, lightweight, professional interactions.
 */

document.addEventListener("DOMContentLoaded", () => {
  initProjectFilters();
  initMobileNav();
  initSmoothScroll();
  initContactForm();
  initBackToTop();
  initResumeDownload();
});

// -------------------------------------------------------------
// 1. Project Category Filtering
// -------------------------------------------------------------
function initProjectFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectItems = document.querySelectorAll(".project-item");

  if (!filterBtns.length || !projectItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filterValue = btn.dataset.filter;

      projectItems.forEach(item => {
        const category = item.dataset.category || "";
        if (filterValue === "all" || category.includes(filterValue)) {
          item.style.display = "grid";
          item.style.opacity = "1";
        } else {
          item.style.display = "none";
          item.style.opacity = "0";
        }
      });
    });
  });
}

// -------------------------------------------------------------
// 2. Mobile Navigation Toggle
// -------------------------------------------------------------
function initMobileNav() {
  const toggleBtn = document.getElementById("mobile-menu-toggle");
  const navMenu = document.getElementById("nav-links");
  const navLinks = document.querySelectorAll(".nav-link");

  if (!toggleBtn || !navMenu) return;

  toggleBtn.addEventListener("click", () => {
    navMenu.classList.toggle("open");
    toggleBtn.setAttribute("aria-expanded", navMenu.classList.contains("open"));
  });

  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("open");
    });
  });
}

// -------------------------------------------------------------
// 3. Smooth Scroll & Active Nav Indicator
// -------------------------------------------------------------
function initSmoothScroll() {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-link");

  window.addEventListener("scroll", () => {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 100;
      const sectionId = current.getAttribute("id");

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${sectionId}`) {
            link.classList.add("active");
          }
        });
      }
    });
  });
}

// -------------------------------------------------------------
// 4. Contact Form Submission Handling
// -------------------------------------------------------------
function initContactForm() {
  const form = document.getElementById("contact-form");
  const statusMsg = document.getElementById("form-status");

  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const submitBtn = form.querySelector("button[type='submit']");
    const originalText = submitBtn.innerHTML;

    submitBtn.disabled = true;
    submitBtn.innerHTML = `Sending...`;

    const formData = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      subject: form.subject.value.trim(),
      message: form.message.value.trim()
    };

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      const result = await response.json();

      if (response.ok && result.success) {
        showStatus("success", result.message || "Message delivered successfully.");
        form.reset();
      } else {
        showStatus("error", result.error || "Failed to send message. Please reach out via email or LinkedIn.");
      }
    } catch (err) {
      console.warn("API request fallback:", err);
      showStatus("error", "Could not reach server. Please email directly or connect on LinkedIn.");
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }
  });

  function showStatus(type, text) {
    if (!statusMsg) return;
    statusMsg.className = `form-status ${type}`;
    statusMsg.textContent = text;
    statusMsg.style.display = "block";

    setTimeout(() => {
      statusMsg.style.display = "none";
    }, 6000);
  }
}

// -------------------------------------------------------------
// 5. Back to Top Button
// -------------------------------------------------------------
function initBackToTop() {
  const backBtn = document.getElementById("back-to-top");
  if (!backBtn) return;

  window.addEventListener("scroll", () => {
    if (window.scrollY > 350) {
      backBtn.classList.add("visible");
    } else {
      backBtn.classList.remove("visible");
    }
  });

  backBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

// -------------------------------------------------------------
// 6. Resume Handling: New Tab on Desktop, Auto-Download on Mobile
// -------------------------------------------------------------
function initResumeDownload() {
  const resumeBtn = document.getElementById("resume-btn");
  if (!resumeBtn) return;

  const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
  if (isMobile) {
    // On phones/tablets, trigger direct automatic download
    resumeBtn.setAttribute("download", "Biswajeet_Pradhan_Resume.pdf");
    resumeBtn.removeAttribute("target");
  } else {
    // On desktop, open in the browser's built-in PDF viewer tab
    resumeBtn.setAttribute("target", "_blank");
    resumeBtn.setAttribute("rel", "noopener noreferrer");
    resumeBtn.removeAttribute("download");
  }
}
