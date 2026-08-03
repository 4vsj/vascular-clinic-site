// Mobile navigation toggle
const toggle = document.querySelector('.nav-toggle');
const menu = document.getElementById('nav-menu');

if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  // Close the menu after choosing a link (mobile)
  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// Current year in footer
const yearEl = document.getElementById('year');
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}

// Modal (before/after)
let lastFocused = null;

function openModal(modal) {
  lastFocused = document.activeElement;
  modal.hidden = false;
  document.body.classList.add('modal-open');
  const closeBtn = modal.querySelector('.modal-close');
  if (closeBtn) closeBtn.focus();
}

function closeModal(modal) {
  modal.hidden = true;
  document.body.classList.remove('modal-open');
  if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
}

document.querySelectorAll('[data-modal]').forEach((trigger) => {
  trigger.addEventListener('click', () => {
    const modal = document.getElementById(trigger.getAttribute('data-modal'));
    if (modal) openModal(modal);
  });
});

document.querySelectorAll('.modal').forEach((modal) => {
  modal.querySelectorAll('[data-close]').forEach((el) => {
    el.addEventListener('click', () => closeModal(modal));
  });
});

document.addEventListener('keydown', (e) => {
  const openEl = document.querySelector('.modal:not([hidden])');
  if (!openEl) return;
  if (e.key === 'Escape') { closeModal(openEl); return; }
  if (e.key === 'Tab') {
    // Keep keyboard focus within the open dialog
    const focusables = openEl.querySelectorAll(
      'a[href], button:not([disabled]), input, textarea, select, [tabindex]:not([tabindex="-1"])'
    );
    if (!focusables.length) return;
    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
});

// Booking form: submissions open the patient's email app addressed to the
// clinic secretary with their details pre-filled. Change this to switch inbox.
const CLINIC_EMAIL = 'secretaryvvvi@gmail.com';

function showBookingStatus(form, message, isError) {
  const status = form.querySelector('.booking-status');
  if (!status) return;
  status.hidden = false;
  status.textContent = message;
  status.classList.toggle('is-error', !!isError);
}

// Header shadow on scroll
const header = document.querySelector('.site-header');
if (header) {
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

// Back-to-top button
const toTop = document.createElement('button');
toTop.className = 'to-top';
toTop.type = 'button';
toTop.setAttribute('aria-label', 'Back to top');
toTop.innerHTML = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
document.body.appendChild(toTop);
toTop.addEventListener('click', () => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
});
window.addEventListener('scroll', () => {
  toTop.classList.toggle('show', window.scrollY > 500);
}, { passive: true });

// Scroll reveal (progressive enhancement; content is visible without JS)
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduceMotion && 'IntersectionObserver' in window) {
  const selectors = [
    '.section-head', '.card', '.feature-list > li', '.exp-list > li',
    '.faq-item', '.about-lead', '.surgeon-photo', '.surgeon-bio',
    '.contact-info', '.booking-form', '.condition-content'
  ];
  const revealEls = [];
  selectors.forEach((sel) => document.querySelectorAll(sel).forEach((el) => revealEls.push(el)));
  revealEls.forEach((el) => el.classList.add('reveal'));

  // Gentle stagger within card / list groups
  document.querySelectorAll('.cards, .feature-list, .exp-list, .faq').forEach((group) => {
    Array.from(group.children).forEach((child, i) => {
      if (child.classList.contains('reveal')) child.style.transitionDelay = Math.min(i, 5) * 70 + 'ms';
    });
  });

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  revealEls.forEach((el) => io.observe(el));
}

document.querySelectorAll('.booking-form').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (typeof form.reportValidity === 'function' && !form.reportValidity()) return;

    const data = new FormData(form);
    const first = (data.get('first_name') || '').toString().trim();
    const last = (data.get('last_name') || '').toString().trim();
    const fullName = (first + ' ' + last).trim();

    if (CLINIC_EMAIL) {
      const lines = [
        'Name: ' + fullName,
        'Phone: ' + (data.get('phone') || ''),
        'Email: ' + (data.get('email') || ''),
        'Preferred date: ' + (data.get('preferred_date') || 'Not specified'),
      ];
      if (data.get('condition')) lines.push('Regarding: ' + data.get('condition'));
      const subject = encodeURIComponent('Consultation request from ' + fullName);
      const body = encodeURIComponent(lines.join('\n'));
      window.location.href = 'mailto:' + CLINIC_EMAIL + '?subject=' + subject + '&body=' + body;
      showBookingStatus(form, 'Opening your email app to send the request. If nothing happens, please call (03) 9429 5955.', false);
    } else {
      showBookingStatus(
        form,
        'Thanks ' + (first || 'for your interest') + '. Online booking isn’t connected yet. Please call (03) 9429 5955 to confirm your appointment.',
        false
      );
    }
  });
});
