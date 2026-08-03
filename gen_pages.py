#!/usr/bin/env python3
"""Generate one 'about' page per condition for the clinic site."""
import os

OUT = "/Users/marcusm/vascular-clinic-site"

HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#0a2440" />
  <meta name="description" content="{meta}" />
  <title>{title} — Victorian Vascular and Vein Institute</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Victorian Vascular and Vein Institute home">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 40 40" width="40" height="40">
            <circle cx="20" cy="20" r="18.5" fill="none" stroke="#b0894a" stroke-width="1.3"/>
            <path d="M17 5 C 13.5 5, 12.5 10, 14 16 C 15.5 22, 14.5 26, 13.5 30.5 C 13 33.5, 13.5 35, 15.5 35.5 L 26 35.5 C 28 35.5, 28 33, 26 32.6 L 19.5 31.3 C 18 27.5, 19 23, 20 18 C 21 12, 21.5 8, 20 5.5 C 19 3.7, 18 3.7, 17 5 Z" fill="#103a63"/>
            <path d="M17.5 9 C 19 13, 16.5 16, 18 20 C 19.3 24, 16.8 27, 17.6 31" fill="none" stroke="#cba95f" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M17.9 15 l-2.4 1.2 M18.4 22 l2.3 1.2" fill="none" stroke="#cba95f" stroke-width="1.2" stroke-linecap="round"/>
          </svg>
        </span>
        <span class="brand-text">
          <span class="brand-name">Victorian Vascular <span class="amp">&amp;</span> Vein</span>
          <span class="brand-inst">Institute</span>
          <span class="brand-sub">Dr Joy Wong</span>
        </span>
      </a>
      <nav class="nav" aria-label="Primary">
        <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
          <span class="sr-only">Menu</span>
          <span class="nav-bars" aria-hidden="true"></span>
        </button>
        <ul id="nav-menu" class="nav-menu">
          <li><a href="index.html">Home</a></li>
          <li class="has-dropdown">
            <a href="index.html#services" class="nav-drop-toggle" aria-haspopup="true">Conditions <span class="caret" aria-hidden="true">&#9662;</span></a>
            <div class="dropdown-panel">
              <div class="container dropdown-row">
                <a href="varicose-veins.html">Varicose &amp; Spider Veins</a>
                <a href="peripheral-artery-disease.html">Peripheral Artery Disease</a>
                <a href="aortic-aneurysm.html">Aortic Aneurysm Care</a>
                <a href="carotid-artery-disease.html">Carotid Artery Disease</a>
                <a href="deep-vein-thrombosis.html">Deep Vein Thrombosis</a>
                <a href="dialysis-access.html">Dialysis Access</a>
              </div>
            </div>
          </li>
          <li><a href="about.html">About</a></li>
          <li><a href="index.html#faq">FAQ</a></li>
          <li><a href="index.html#contact">Contact</a></li>
          <li><a class="nav-cta" href="#book">Book a consultation</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span aria-hidden="true">/</span>
          <a href="index.html#services">Conditions</a>
          <span aria-hidden="true">/</span>
          <span aria-current="page">{title}</span>
        </nav>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="page-lead">{lead}</p>
      </div>
    </section>

    <section class="section">
      <div class="container condition-layout">
        <article class="condition-content">
          <img class="condition-hero-img" src="images/conditions/{slug}.svg" alt="{img_alt}" width="400" height="240" />
{body}
          <p class="disclaimer">This information is general and is not a substitute for medical advice. Please see Dr Wong for advice about your individual situation.</p>
        </article>

        <aside class="booking-aside">
{form}
        </aside>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <p class="footer-brand">Victorian Vascular <span class="amp">&amp;</span> Vein Institute</p>
        <p class="footer-note">
          Specialist vascular and vein care with Dr Joy Wong, Richmond, Melbourne.
        </p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <a href="index.html#services">Conditions</a>
        <a href="about.html">About</a>
        <a href="index.html#contact">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Visit</h4>
        <a href="tel:+61394295955">(03) 9429 5955</a>
        <a href="mailto:secretaryvvvi@gmail.com">secretaryvvvi@gmail.com</a>
        <a href="https://maps.google.com/?q=158+Lennox+Street,+Richmond+VIC+3121" target="_blank" rel="noopener">158 Lennox Street,<br />Richmond VIC 3121</a>
      </div>
    </div>
    <div class="container footer-base">
      <p>© <span id="year"></span> Victorian Vascular and Vein Institute.</p>
      <p>For information only — not a substitute for medical advice.</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""


def booking_form(title, condition=None):
    regarding = ""
    hidden = ""
    if condition:
        hidden = f'          <input type="hidden" name="condition" value="{condition}" />\n'
        regarding = f'          <p class="booking-regarding">Regarding <strong>{condition}</strong></p>\n'
    return f"""          <form class="booking-form" id="book" novalidate>
            <h2 class="booking-title">{title}</h2>
            <p class="booking-sub">Request an appointment with Dr Wong. We'll confirm your time by phone.</p>
{hidden}{regarding}            <div class="field-row">
              <div class="field">
                <label for="bf-first">First name</label>
                <input id="bf-first" name="first_name" type="text" autocomplete="given-name" required />
              </div>
              <div class="field">
                <label for="bf-last">Last name</label>
                <input id="bf-last" name="last_name" type="text" autocomplete="family-name" required />
              </div>
            </div>
            <div class="field">
              <label for="bf-phone">Phone</label>
              <input id="bf-phone" name="phone" type="tel" autocomplete="tel" required />
            </div>
            <div class="field">
              <label for="bf-email">Email</label>
              <input id="bf-email" name="email" type="email" autocomplete="email" required />
            </div>
            <div class="field">
              <label for="bf-date">Preferred date</label>
              <input id="bf-date" name="preferred_date" type="date" />
            </div>
            <button class="btn btn-primary btn-block" type="submit">Request booking</button>
            <p class="booking-alt">Prefer to call? <a href="tel:+61394295955">(03) 9429 5955</a></p>
            <p class="booking-status" role="status" aria-live="polite" hidden></p>
          </form>"""


def render_sections(sections):
    out = []
    for s in sections:
        out.append(f'          <h2>{s["h"]}</h2>')
        for p in s.get("paras", []):
            out.append(f'          <p>{p}</p>')
        bullets = s.get("bullets", [])
        if bullets:
            out.append('          <ul class="cond-list">')
            for b in bullets:
                out.append(f'            <li>{b}</li>')
            out.append('          </ul>')
        if s.get("html"):
            out.append(s["html"])
    return "\n".join(out)


BA_FIGURE = """          <figure class="ba-figure">
            <img src="images/varicose-before-after.png" alt="A patient's lower leg before and after varicose vein treatment: prominent bulging veins on the left, smooth skin on the right" width="1446" height="1424" loading="lazy" />
            <figcaption>Left: before treatment. Right: after treatment. Results shown are for one patient and are not a guarantee — individual outcomes vary.</figcaption>
          </figure>"""


CONDITIONS = [
    {
        "slug": "varicose-veins",
        "title": "Varicose &amp; Spider Veins",
        "eyebrow": "Vein condition",
        "meta": "Varicose and spider vein treatment in Richmond, Melbourne with Dr Joy Wong — sclerotherapy, endovenous laser and more.",
        "img_alt": "Illustration of varicose and spider veins in a leg",
        "lead": "Enlarged, twisted veins that show through the skin — usually in the legs. Most can be treated with modern, minimally invasive, walk-in walk-out procedures.",
        "sections": [
            {"h": "Overview", "paras": [
                "Varicose veins are swollen, rope-like veins that bulge beneath the skin, most often in the legs. They develop when the tiny one-way valves inside the veins weaken, allowing blood to pool instead of flowing back to the heart. Spider veins are the same problem on a smaller scale — fine red, blue or purple threads visible at the skin's surface.",
                "As well as their appearance, varicose veins can cause real discomfort and, left untreated, may lead to skin changes or ulcers over time."]},
            {"h": "Symptoms", "bullets": [
                "Aching, heavy or tired legs, especially after standing",
                "Swelling around the ankles",
                "Throbbing, burning or itching over a vein",
                "Night cramps or restless legs",
                "Visible bulging, rope-like or thread-like veins",
                "Skin discolouration or ulcers near the ankle in longstanding cases"]},
            {"h": "Causes &amp; risk factors", "bullets": [
                "Weakened or damaged vein valves",
                "Family history of varicose veins",
                "Pregnancy and hormonal changes",
                "Prolonged standing or sitting",
                "Increasing age",
                "Being overweight"]},
            {"h": "Treatment options",
                "paras": ["Vein stripping surgery is largely a thing of the past. Today most varicose veins are treated with minimally invasive techniques, usually in the clinic and without a general anaesthetic:"],
                "bullets": [
                    "Duplex ultrasound mapping — a painless scan to map the veins and plan treatment",
                    "Endovenous laser ablation (EVLA) — heat closes the faulty vein from the inside",
                    "Ultrasound-guided sclerotherapy — a solution is injected to close larger, deeper veins",
                    "Microsclerotherapy — fine injections for smaller spider veins",
                    "Compression stockings and lifestyle measures to support treatment"],
                "html": BA_FIGURE},
            {"h": "What to expect", "paras": [
                "Your visit begins with a consultation and a duplex ultrasound so Dr Wong can see exactly which veins are involved. She'll then explain your options and recommend a plan. Most treatments are minimally invasive with little downtime — many patients walk in and walk out the same day."]},
        ],
    },
    {
        "slug": "peripheral-artery-disease",
        "title": "Peripheral Artery Disease",
        "eyebrow": "Arterial condition",
        "meta": "Diagnosis and treatment of peripheral artery disease (PAD) in Richmond, Melbourne with vascular surgeon Dr Joy Wong.",
        "img_alt": "Illustration of an artery narrowed by plaque",
        "lead": "Narrowing of the arteries — usually in the legs — that reduces blood flow and can cause pain when walking. Early treatment protects your mobility and your limbs.",
        "sections": [
            {"h": "Overview", "paras": [
                "Peripheral artery disease (PAD) develops when fatty deposits (plaque) build up inside the arteries that carry blood to your limbs, most commonly the legs. As the arteries narrow, less oxygen-rich blood reaches the muscles and tissues.",
                "PAD is often a sign of more widespread artery disease, so diagnosing it is also an opportunity to protect your heart and overall health."]},
            {"h": "Symptoms", "bullets": [
                "Cramping or pain in the calf, thigh or buttock when walking, relieved by rest (claudication)",
                "Coldness or numbness in the lower leg or foot",
                "Weak or absent pulses in the legs",
                "Slow-healing sores or wounds on the feet or toes",
                "Colour changes or shiny skin on the legs"]},
            {"h": "Causes &amp; risk factors", "bullets": [
                "Smoking", "Diabetes", "High blood pressure", "High cholesterol",
                "Increasing age", "Family history of artery disease"]},
            {"h": "Treatment options",
                "paras": ["Treatment aims to relieve symptoms, improve circulation and reduce the risk of complications:"],
                "bullets": [
                    "Managing risk factors — stopping smoking and controlling diabetes, blood pressure and cholesterol",
                    "A structured walking and exercise program",
                    "Medications to improve blood flow and protect the arteries",
                    "Angioplasty and stenting — opening a narrowed artery from the inside",
                    "Bypass surgery for more advanced disease"]},
            {"h": "What to expect", "paras": [
                "Assessment usually includes checking your pulses, an ankle-brachial index (comparing blood pressure at the ankle and arm) and imaging of the arteries. Dr Wong will explain the findings and tailor a plan to protect your circulation and mobility."]},
        ],
    },
    {
        "slug": "aortic-aneurysm",
        "title": "Aortic Aneurysm",
        "eyebrow": "Arterial condition",
        "meta": "Screening, monitoring and repair of abdominal and thoracic aortic aneurysms with Dr Joy Wong, Richmond, Melbourne.",
        "img_alt": "Illustration of an aortic aneurysm bulge",
        "lead": "A bulge in the wall of the aorta — the body's main artery. Often silent, but important to monitor and, when needed, repair before it becomes dangerous.",
        "sections": [
            {"h": "Overview", "paras": [
                "The aorta is the large artery that carries blood from the heart to the rest of the body. An aneurysm is a weakened, bulging section of its wall. Aneurysms can occur in the abdomen (abdominal aortic aneurysm) or the chest (thoracic aortic aneurysm).",
                "Most aneurysms grow slowly and cause no symptoms, but a large or rapidly growing aneurysm can be at risk of rupture, which is a medical emergency. This is why screening and monitoring matter."]},
            {"h": "Symptoms", "bullets": [
                "Often none — many aneurysms are found incidentally",
                "A pulsing sensation in the abdomen",
                "Deep, constant abdominal or back pain",
                "Sudden, severe pain — a possible rupture, requiring emergency care"]},
            {"h": "Causes &amp; risk factors", "bullets": [
                "Smoking", "High blood pressure", "Atherosclerosis (hardening of the arteries)",
                "Increasing age", "Being male", "Family history of aneurysm"]},
            {"h": "Treatment options",
                "paras": ["The right approach depends on the size, location and growth of the aneurysm:"],
                "bullets": [
                    "Surveillance — regular ultrasound or CT scans to monitor small aneurysms",
                    "Managing blood pressure and stopping smoking to slow growth",
                    "Endovascular repair (EVAR) — a stent-graft placed from inside the artery",
                    "Open surgical repair for selected aneurysms"]},
            {"h": "What to expect", "paras": [
                "If an aneurysm is found, Dr Wong will assess its size and risk and recommend either careful monitoring or repair. Many aneurysms simply need regular scans; repair is advised when the benefits outweigh the risks."]},
        ],
    },
    {
        "slug": "carotid-artery-disease",
        "title": "Carotid Artery Disease",
        "eyebrow": "Arterial condition",
        "meta": "Assessment and treatment of carotid artery disease to reduce stroke risk, with Dr Joy Wong, Richmond, Melbourne.",
        "img_alt": "Illustration of a carotid artery narrowed by plaque",
        "lead": "Narrowing of the carotid arteries in the neck, which supply blood to the brain. Treating it lowers the risk of stroke.",
        "sections": [
            {"h": "Overview", "paras": [
                "The carotid arteries run up either side of the neck and carry blood to the brain. Carotid artery disease occurs when plaque narrows these arteries. Pieces of plaque or clot can break away and travel to the brain, causing a stroke or a 'mini-stroke' (TIA).",
                "Because carotid disease often has no symptoms until a stroke or warning event, identifying and managing it early is important."]},
            {"h": "Symptoms", "bullets": [
                "Often none until a warning event occurs",
                "Sudden weakness or numbness of the face, arm or leg — usually on one side",
                "Sudden trouble speaking or understanding speech",
                "Sudden loss of vision in one eye",
                "These are stroke warning signs — call 000 immediately"]},
            {"h": "Causes &amp; risk factors", "bullets": [
                "Atherosclerosis (plaque build-up)", "Smoking", "High blood pressure",
                "High cholesterol", "Diabetes", "Increasing age"]},
            {"h": "Treatment options",
                "paras": ["Treatment focuses on preventing stroke by controlling risk factors and, where narrowing is significant, restoring safe blood flow:"],
                "bullets": [
                    "Medications — blood-thinning and cholesterol-lowering therapy",
                    "Managing blood pressure and diabetes, and stopping smoking",
                    "Carotid endarterectomy — surgery to remove the plaque",
                    "Carotid stenting in selected cases"]},
            {"h": "What to expect", "paras": [
                "Assessment usually starts with a carotid duplex ultrasound to measure any narrowing. Dr Wong will weigh your stroke risk against the benefits of treatment and recommend the safest approach for you."]},
        ],
    },
    {
        "slug": "deep-vein-thrombosis",
        "title": "Deep Vein Thrombosis",
        "eyebrow": "Vein condition · urgent",
        "meta": "Rapid assessment and treatment of deep vein thrombosis (DVT) with Dr Joy Wong, Richmond, Melbourne.",
        "img_alt": "Illustration of a deep vein blocked by a blood clot",
        "lead": "A blood clot in a deep vein, usually in the leg. It needs prompt attention to relieve symptoms and prevent serious complications.",
        "sections": [
            {"h": "Overview", "paras": [
                "Deep vein thrombosis (DVT) is a blood clot that forms in one of the deep veins, most often in the calf or thigh. It can cause pain and swelling, and if part of the clot breaks free it can travel to the lungs — a pulmonary embolism — which is potentially life-threatening.",
                "Prompt diagnosis and treatment relieve symptoms and greatly reduce the risk of complications."]},
            {"h": "Symptoms", "bullets": [
                "Swelling in one leg (or arm)",
                "Pain or tenderness, often in the calf",
                "Warmth and redness over the area",
                "Sudden breathlessness or chest pain — a possible clot on the lung, requiring emergency care"]},
            {"h": "Causes &amp; risk factors", "bullets": [
                "Long periods of immobility (long-haul travel, bed rest)",
                "Recent surgery or injury",
                "Inherited or acquired clotting disorders",
                "Cancer and some of its treatments",
                "Pregnancy and hormonal medications"]},
            {"h": "Treatment options",
                "paras": ["DVT is usually managed medically, with more active treatment in selected cases:"],
                "bullets": [
                    "Anticoagulation (blood-thinning medication) to stop the clot growing and prevent new clots",
                    "Compression stockings to reduce swelling",
                    "Clot-dissolving treatment (thrombolysis) or clot removal in severe cases",
                    "Investigating and treating the underlying cause"]},
            {"h": "What to expect", "paras": [
                "If a DVT is suspected, an urgent ultrasound confirms the diagnosis. Treatment usually begins quickly to protect you from complications, followed by a plan to prevent further clots. If you have sudden breathlessness or chest pain, call 000."]},
        ],
    },
    {
        "slug": "dialysis-access",
        "title": "Dialysis Access",
        "eyebrow": "Vascular access",
        "meta": "Creation and maintenance of dialysis access (AV fistula and graft) with Dr Joy Wong, Richmond, Melbourne.",
        "img_alt": "Illustration of an arteriovenous fistula for dialysis access",
        "lead": "Reliable, long-lasting access to the bloodstream for patients who need haemodialysis — created and maintained with careful surgical planning.",
        "sections": [
            {"h": "Overview", "paras": [
                "People receiving haemodialysis need a way to connect to the dialysis machine that allows a high flow of blood. The best long-term solution is usually an arteriovenous (AV) fistula — a connection made surgically between an artery and a nearby vein, which strengthens the vein over time so it can be used for dialysis.",
                "Good access is central to effective dialysis, so planning, creating and maintaining it well makes a real difference to patients' lives."]},
            {"h": "Types of access", "bullets": [
                "AV fistula — the preferred, longest-lasting option, made from your own artery and vein",
                "AV graft — a soft tube used when your veins aren't suitable for a fistula",
                "Central venous catheter — for urgent or temporary access"]},
            {"h": "What's involved", "paras": [
                "Creating a fistula is usually a day procedure. Over the following weeks the vein 'matures' — enlarging and strengthening — until it's ready to use for dialysis."]},
            {"h": "Keeping your access healthy", "bullets": [
                "Regular checks to make sure the access is flowing well",
                "Treating any narrowing or blockage early, often with a minimally invasive procedure",
                "Protecting the access arm as advised"]},
            {"h": "What to expect", "paras": [
                "Dr Wong will assess your veins (often with ultrasound mapping) and plan the type of access best suited to you, then care for it over time to keep your dialysis running smoothly."]},
        ],
    },
]


def main():
    for c in CONDITIONS:
        body = render_sections(c["sections"])
        form = booking_form("Book a consultation", condition=c["title"])
        html = HEAD.format(
            meta=c["meta"], title=c["title"], eyebrow=c["eyebrow"],
            lead=c["lead"], slug=c["slug"], img_alt=c["img_alt"],
            body=body, form=form,
        )
        path = os.path.join(OUT, c["slug"] + ".html")
        with open(path, "w") as f:
            f.write(html)
        print("wrote", path)


if __name__ == "__main__":
    main()
