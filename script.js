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
  if (e.key !== 'Escape') return;
  document.querySelectorAll('.modal:not([hidden])').forEach(closeModal);
});

// Booking form
// TODO: add the clinic's booking email between the quotes to enable email
// delivery. While this is empty, the form asks patients to call instead.
const CLINIC_EMAIL = '';

function showBookingStatus(form, message, isError) {
  const status = form.querySelector('.booking-status');
  if (!status) return;
  status.hidden = false;
  status.textContent = message;
  status.classList.toggle('is-error', !!isError);
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
      const subject = encodeURIComponent('Consultation request — ' + fullName);
      const body = encodeURIComponent(lines.join('\n'));
      window.location.href = 'mailto:' + CLINIC_EMAIL + '?subject=' + subject + '&body=' + body;
      showBookingStatus(form, 'Opening your email app to send the request. If nothing happens, please call (03) 9429 5955.', false);
    } else {
      showBookingStatus(
        form,
        'Thanks ' + (first || 'for your interest') + '. Online booking isn’t connected yet — please call (03) 9429 5955 to confirm your appointment.',
        false
      );
    }
  });
});
