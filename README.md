# Victorian Vascular and Vein Institute — Website

A responsive, mobile-first one-page website for the Victorian Vascular and Vein
Institute (Dr Joy Wong), built with plain HTML, CSS, and a small amount of
JavaScript. Navy-and-white theme with a brass accent, Fraunces + Inter type.
Booking is by phone: every "book" button is a click-to-call link.

**Clinic details**

- Surgeon: Dr Joy Wong
- Phone: (03) 9429 5955
- Address: 158 Lennox Street, Richmond VIC 3121

## Files

| File | Purpose |
|------|---------|
| `index.html` | Home page (hero, conditions, booking) |
| `about.html` | About Us — Dr Joy Wong bio, experience, approach |
| `varicose-veins.html` etc. | One "about" page per condition, with a booking form |
| `styles.css` | Navy & white theme and responsive layout |
| `script.js` | Mobile menu, footer year, booking-form handler |
| `images/dr-joy-wong.png` | Portrait of Dr Joy Wong |
| `images/varicose-before-after.png` | Before/after photo (varicose page) |
| `images/conditions/` | SVG diagrams, one per condition |

The condition pages are generated from `gen_pages.py` (`python3 gen_pages.py`);
edit the content there and re-run it, or edit the HTML files directly.

## Booking form

Every "Book a consultation" button leads to a form asking for first name, last
name, phone, email and preferred date. On submit it opens the patient's email
app with their details pre-filled, addressed to the clinic secretary
(`secretaryvvvi@gmail.com`). The inbox is set in `script.js`:

```js
const CLINIC_EMAIL = 'secretaryvvvi@gmail.com';
```

For a more automated option (no email-app step — submissions arrive without the
patient needing to press send), a service like Formspree can be wired in instead.

## Contact details

- Phone: (03) 9429 5955 · Fax: (03) 9923 6920
- Bookings/enquiries: secretaryvvvi@gmail.com · Rooms: wongvascular@icloud.com
- 158 Lennox Street, Richmond VIC 3121

## View locally

Just open `index.html` in your browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Live site

This site is deployed with **GitHub Pages** from the `main` branch. Once Pages
finishes building, it will be available at the URL shown in the repository's
**Settings → Pages** section.

## Things you may still want to add / check

- Opening hours (not currently listed)
- **Review the FAQ answers** in `index.html` (`id="faq"`) — the Medicare/costs
  and location/parking wording is general; adjust it to your clinic's specifics.
