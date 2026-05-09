// Modals
function openModal(id) {
  const overlay = document.getElementById(id);
  if (!overlay) return;

  overlay.classList.add("open");
  document.body.style.overflow = "hidden";

  setTimeout(function () {
    const first = overlay.querySelector("input, textarea, select");
    if (first) first.focus();
  }, 180);
}

function openEditModal(Id, button = null) {
  const overlay = document.getElementById(Id);
  const form = overlay.querySelector("form");
  if (!overlay) return;

  if (button) {
    form.action = button.dataset.url;
    const name = button.dataset.name;
    if (name == "education") {
      form.querySelector("#ee_institution").value = button.dataset.institution;
      form.querySelector("#ee_degree").value = button.dataset.degree;
      form.querySelector("#ee_field").value = button.dataset.field;
      form.querySelector("#ee_start").value = button.dataset.startyear;
      form.querySelector("#ee_end").value = button.dataset.endyear;
      form.querySelector("#ee_grade").value = button.dataset.grade;
      form.querySelector("#ee_location").value = button.dataset.location;
      form.querySelector("#ee_website").value = button.dataset.website;
    } else if (name == "project") {
      form.querySelector("#pe_title").value = button.dataset.title;
      form.querySelector("#pe_github").value = button.dataset.github;
      form.querySelector("#pe_live").value = button.dataset.live;
    } else if (name == "achievement") {
      form.querySelector("#ace_title").value = button.dataset.title;
      form.querySelector("#ace_org").value = button.dataset.org;
      form.querySelector("#ace_year").value = button.dataset.year;
      form.querySelector("#ace_cert").value = button.dataset.certificate;
    } else if (name == "certificate") {
      form.querySelector("#ce_title").value = button.dataset.title;
      form.querySelector("#ce_org").value = button.dataset.org;
      form.querySelector("#ce_issued").value = button.dataset.issuedate;
      form.querySelector("#ce_expires").value = button.dataset.expirydate;
      form.querySelector("#ce_url").value = button.dataset.certificate;
    } else if (name == "experience") {
      form.querySelector("#exe_role").value = button.dataset.role;
      form.querySelector("#exe_org").value = button.dataset.org;
      form.querySelector("#exe_start").value = button.dataset.startdate;
      form.querySelector("#exe_end").value = button.dataset.enddate;
      form.querySelector("#exe_cert").value = button.dataset.certificate;
    } else {
      return;
    }
  }

  overlay.classList.add("open");
  document.body.style.overflow = "hidden";

  setTimeout(function () {
    const first = overlay.querySelector("input, textarea, select");
    if (first) first.focus();
  }, 180);
}

function openKeyModal(button) {
  const overlay = document.getElementById("modal-key-points");
  const form = overlay.querySelector("form");
  const url = button.getAttribute("data-url");
  if (!overlay) return;
  if (url) {
    form.action = url;
  }
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";

  setTimeout(function () {
    const first = overlay.querySelector("input, textarea, select");
    if (first) first.focus();
  }, 180);
}

function openTechModal(button) {
  const overlay = document.getElementById("modal-project-tech-stack");
  const form = overlay.querySelector("form");
  const url = button.getAttribute("data-url");
  if (!overlay) return;
  if (url) {
    form.action = url;
  }
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";

  setTimeout(function () {
    const first = overlay.querySelector("input, textarea, select");
    if (first) first.focus();
  }, 180);
}

function openSkillModal(button) {
  const overlay = document.getElementById("modal-skill-name");
  const form = overlay.querySelector("form");
  const url = button.getAttribute("data-url");
  if (!overlay) return;
  if (url) {
    form.action = url;
  }
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";

  setTimeout(function () {
    const first = overlay.querySelector("input, textarea, select");
    if (first) first.focus();
  }, 180);
}

function closeModal(id) {
  const overlay = document.getElementById(id);
  if (!overlay) return;
  overlay.classList.remove("open");
  document.body.style.overflow = "";
}

document.querySelectorAll(".modal-overlay").forEach(function (overlay) {
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) {
      closeModal(overlay.id);
    }
  });
});

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    document.querySelectorAll(".modal-overlay.open").forEach(function (o) {
      closeModal(o.id);
    });
    closeConfirm();
  }
});

// Confirm dialogue
function openConfirm(button) {
  const overlay = document.getElementById("confirmOverlay");
  const url = button.getAttribute("data-url");
  const title = button.getAttribute("data-title");
  const btn = document.getElementById("confirmDeleteBtn");
  const msg = document.getElementById("confirmMsg");
  btn.href = url;
  if (title) {
    msg.innerHTML = `${title}<br>This action cannot be undone.`;
  }
  if (!overlay) return;
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeConfirm() {
  const overlay = document.getElementById("confirmOverlay");
  if (!overlay) return;
  overlay.classList.remove("open");
  document.body.style.overflow = "";
}

// Confirm Logout
function openLogout() {
  const overlay = document.getElementById("confirmLogout");
  if (!overlay) return;
  overlay.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeLogout() {
  const overlay = document.getElementById("confirmLogout");
  if (!overlay) return;
  overlay.classList.remove("open");
  document.body.style.overflow = "";
}

const confirmCancelBtn = document.querySelector(".confirm-cancel-btn");
if (confirmCancelBtn) {
  confirmCancelBtn.addEventListener("click", closeConfirm);
}

const confirmOverlay = document.getElementById("confirmOverlay");
if (confirmOverlay) {
  confirmOverlay.addEventListener("click", function (e) {
    if (e.target === confirmOverlay) closeConfirm();
  });
}

// Navbar
const bar = document.querySelector("#bar");
const navbar = document.querySelector("#navbar");
const close = document.querySelector("#close");
const overlay = document.querySelector("#drawerOverlay");

function openNav() {
  navbar.classList.add("active");
  overlay.classList.add("active");
  bar.className = "fa-solid fa-xmark";
}
function closeNav() {
  navbar.classList.remove("active");
  overlay.classList.remove("active");
  bar.className = "fa-solid fa-bars";
}

if (bar)
  bar.addEventListener("click", () =>
    navbar.classList.contains("active") ? closeNav() : openNav(),
  );
if (close) close.addEventListener("click", closeNav);
if (overlay) overlay.addEventListener("click", closeNav);

document
  .querySelectorAll("#navbar li a")
  .forEach((l) => l.addEventListener("click", closeNav));

document.addEventListener("click", (e) => {
  if (
    navbar.classList.contains("active") &&
    !bar.contains(e.target) &&
    !navbar.contains(e.target)
  )
    closeNav();
});

// Active link on scroll
const sections = document.querySelectorAll("section[id], main section[id]");
const navLinks = document.querySelectorAll("#navbar li a");
window.addEventListener("scroll", () => {
  let cur = "";
  sections.forEach((s) => {
    if (window.scrollY >= s.offsetTop - 90) cur = s.id;
  });
  navLinks.forEach((a) => {
    a.classList.toggle("active", a.getAttribute("href") === "#" + cur);
  });
});

// Scroll reveal
const ro = new IntersectionObserver(
  (entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting) {
        e.target.style.transitionDelay = (i % 3) * 0.08 + "s";
        e.target.classList.add("visible");
        ro.unobserve(e.target);
      }
    });
  },
  { threshold: 0.08 },
);
document.querySelectorAll(".reveal").forEach((el) => ro.observe(el));

// Slideshow
function slideMove(id, dir) {
  const w = document.getElementById(id),
    imgs = w.querySelectorAll("img"),
    dotsW = document.getElementById(id.replace("Slide", "Dots"));
  let cur = [...imgs].findIndex((i) => i.classList.contains("act"));
  imgs[cur].classList.remove("act");
  cur = (cur + dir + imgs.length) % imgs.length;
  imgs[cur].classList.add("act");
  if (dotsW)
    dotsW
      .querySelectorAll(".sdot")
      .forEach((d, i) => d.classList.toggle("act", i === cur));
}
document.querySelectorAll(".sshow").forEach((sw) => {
  const id = sw.id,
    dw = document.getElementById(id.replace("Slide", "Dots")),
    imgs = sw.querySelectorAll("img");
  imgs.forEach((_, i) => {
    const d = document.createElement("div");
    d.className = "sdot" + (i === 0 ? " act" : "");
    d.onclick = () => {
      imgs.forEach((img) => img.classList.remove("act"));
      imgs[i].classList.add("act");
      dw &&
        dw
          .querySelectorAll(".sdot")
          .forEach((dd, j) => dd.classList.toggle("act", j === i));
    };
    dw && dw.appendChild(d);
  });
});
setInterval(() => slideMove("eduSlide", 1), 3800);

// Contact Form

const form = document.getElementById("contactForm");

if (form) {
  const error = document.querySelectorAll(".ferr");
  error.forEach((e) => {
    e.textContent = "";
  });

  const fname = document.querySelector(".fname");
  const femail = document.querySelector(".femail");
  const fsubj = document.querySelector(".fsubj");
  const fmsg = document.querySelector(".fmsg");

  const fne = document.querySelector(".fne");
  const fee = document.querySelector(".fee");
  const fse = document.querySelector(".fse");
  const fme = document.querySelector(".fme");

  let valid_name = true;
  let valid_email = true;
  let valid_subject = true;
  let valid_message = true;

  fname.addEventListener("input", (e) => {
    const name = fname.value.trim();
    if (!name) {
      fne.textContent = "Name is required!";
      valid_name = false;
    } else if (name.length < 3) {
      fne.textContent = "Name must contain at least 3 characters";
      valid_name = false;
    } else {
      fne.textContent = "";
      valid_name = true;
    }
  });

  femail.addEventListener("input", (e) => {
    const email = femail.value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
      fee.textContent = "Email is required!";
      valid_email = false;
    } else if (!emailPattern.test(email)) {
      fee.textContent = "Enter a valid email address!";
      valid_email = false;
    } else {
      fee.textContent = "";
      valid_email = true;
    }
  });

  fsubj.addEventListener("input", (e) => {
    const subject = fsubj.value.trim();
    if (!subject) {
      fse.textContent = "Subject is required!";
      valid_subject = false;
    } else {
      fse.textContent = "";
      valid_subject = true;
    }
  });

  fmsg.addEventListener("input", (e) => {
    const message = fmsg.value.trim();
    if (!message) {
      fme.textContent = "Message is required!";
      valid_message = false;
    } else {
      fme.textContent = "";
      valid_message = true;
    }
  });

  form.addEventListener("submit", (e) => {
    const isValid = valid_name && valid_email && valid_subject && valid_message;
    const ffin = document.querySelector(".ffin");
    if (!isValid) {
      e.preventDefault();
      ffin.textContent = "Fix the error to send message!";
    }
  });
}

// Download Resume
function downloadResume() {
  const element = document.getElementById("cover");
  const isMobile = window.innerWidth < 768;

  element.style.display = "block";

  setTimeout(() => {

    const opt = {
      margin: [20, 18, 18, 18],

      filename: "my_resume.pdf",

      image: {
        type: "jpeg",
        quality: 0.95,
      },

      html2canvas: {
        scale: isMobile ? 1.5 : 2,
        useCORS: true,
        backgroundColor: "#ffffff",
      },

      jsPDF: {
        unit: "mm",
        format: "a4",
        orientation: "portrait",
      },

      pagebreak: {
        mode: ["css"],
      },
    };

    html2pdf()
      .set(opt)
      .from(element)
      .toPdf()
      .get('pdf')
      .then(function (pdf) {

        const totalPages = pdf.internal.getNumberOfPages();

        for (let i = 1; i <= totalPages; i++) {

          pdf.setPage(i);

          pdf.setFontSize(10);

          pdf.text(
            `Page ${i} of ${totalPages}`,
            180,
            10
          );
        }
      })
      .save()
      .then(() => {
        element.style.display = "none";
      });
  }, 500);
}