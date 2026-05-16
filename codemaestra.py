<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI &amp; You — CodeMaestra Academy | Merita Odera</title>
  <meta name="description" content="A 6-week customised Generative AI course by Merita Odera, CodeMaestra Academy Kenya. Free 45-min taster session. Cohort 2 starts June 2. KES 10,000." />
  <meta property="og:title" content="AI &amp; You — CodeMaestra Academy" />
  <meta property="og:description" content="6-week customised Generative AI course for professionals, business owners and educators. Free 45-min taster. New cohort every 2nd of the month." />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#0d0d1a" />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />

  <style>

    /* ── RESET ── */
    *, *::before, *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* ── DESIGN TOKENS ── */
    :root {
      --bg:           #0d0d1a;
      --bg3:          #1a1a35;
      --card:         #16162e;
      --border:       rgba(123, 94, 167, 0.25);
      --border-pink:  rgba(255, 45, 122, 0.2);
      --pink:         #ff2d7a;
      --pink-soft:    #ff6ba0;
      --pink-pale:    rgba(255, 45, 122, 0.1);
      --purple:       #7b5ea7;
      --purple-light: #a78bfa;
      --white:        #ffffff;
      --muted:        rgba(255, 255, 255, 0.5);
      --muted2:       rgba(255, 255, 255, 0.3);
    }

    /* ── BASE ── */
    html {
      scroll-behavior: smooth;
    }

    body {
      background: var(--bg);
      font-family: 'Inter', sans-serif;
      color: var(--white);
      max-width: 480px;
      margin: 0 auto;
      overflow-x: hidden;
    }

    /* ── ANIMATIONS ── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(22px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulseDot {
      0%, 100% { box-shadow: 0 0 6px var(--pink); }
      50%       { box-shadow: 0 0 18px var(--pink); }
    }

    @keyframes pulseBadge {
      0%, 100% { box-shadow: 0 0 0 0 rgba(255, 45, 122, 0.5); }
      50%       { box-shadow: 0 0 0 6px rgba(255, 45, 122, 0); }
    }

    /* ── HERO ── */
    .hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 48px 28px 52px;
      overflow: hidden;
      background: var(--bg);
    }

    .hero-glow {
      position: absolute;
      inset: 0;
      pointer-events: none;
      background:
        radial-gradient(ellipse 70% 50% at 80% 10%, rgba(255, 45, 122, 0.15) 0%, transparent 60%),
        radial-gradient(ellipse 50% 60% at 5% 70%,  rgba(123, 94, 167, 0.2)  0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 50% 100%, rgba(167, 139, 250, 0.08) 0%, transparent 60%);
    }

    .hero-brand {
      position: absolute;
      top: 28px;
      left: 28px;
      font-family: 'Syne', sans-serif;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--purple-light);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .hero-brand-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--pink);
      box-shadow: 0 0 10px var(--pink);
      animation: pulseDot 2s ease-in-out infinite;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--pink-pale);
      border: 1px solid var(--border-pink);
      color: var(--pink-soft);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 20px;
      margin-bottom: 22px;
      width: fit-content;
      animation: pulseBadge 2.5s ease-in-out infinite;
    }

    .hero-badge-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--pink);
      display: inline-block;
    }

    .hero-eyebrow {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--purple-light);
      margin-bottom: 16px;
    }

    .hero-eyebrow-line {
      width: 20px;
      height: 1px;
      background: var(--purple-light);
    }

    .hero-title {
      font-family: 'Syne', sans-serif;
      font-size: 44px;
      line-height: 1.05;
      font-weight: 800;
      color: var(--white);
      margin-bottom: 16px;
      animation: fadeUp 0.7s ease both;
    }

    .hero-title .accent {
      color: var(--pink);
      text-shadow: 0 0 30px rgba(255, 45, 122, 0.4);
    }

    .hero-sub {
      font-size: 14px;
      line-height: 1.7;
      color: var(--muted);
      margin-bottom: 36px;
      max-width: 360px;
      animation: fadeUp 0.7s 0.15s ease both;
    }

    .hero-sub strong {
      color: var(--white);
    }

    .hero-stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      animation: fadeUp 0.7s 0.3s ease both;
    }

    .stat {
      background: var(--bg3);
      border: 0.5px solid var(--border);
      border-radius: 12px;
      padding: 12px 6px;
      text-align: center;
    }

    .stat-val {
      display: block;
      font-family: 'Syne', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--pink-soft);
      margin-bottom: 3px;
    }

    .stat-lbl {
      font-size: 9px;
      color: var(--muted2);
      letter-spacing: 0.03em;
      line-height: 1.3;
    }

    /* ── FREE TASTER ── */
    .free-section {
      margin: 0 16px;
      background: linear-gradient(135deg, #1f0a2e, #2a0d3a);
      border: 1px solid rgba(255, 45, 122, 0.35);
      border-radius: 20px;
      padding: 24px 22px;
      position: relative;
      overflow: hidden;
      transform: translateY(-20px);
      box-shadow: 0 8px 40px rgba(255, 45, 122, 0.12);
    }

    .free-section-glow {
      position: absolute;
      top: -30px;
      right: -30px;
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255, 45, 122, 0.2), transparent 70%);
      pointer-events: none;
    }

    .free-label {
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--pink);
      margin-bottom: 6px;
    }

    .free-title {
      font-family: 'Syne', sans-serif;
      font-size: 22px;
      font-weight: 800;
      color: var(--white);
      margin-bottom: 4px;
    }

    .free-date {
      font-size: 11px;
      font-weight: 600;
      color: var(--purple-light);
      letter-spacing: 0.04em;
      margin-bottom: 12px;
    }

    .free-desc {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.65;
      margin-bottom: 16px;
    }

    .free-bullets {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 20px;
    }

    .free-bullet {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12.5px;
      color: rgba(255, 255, 255, 0.75);
      line-height: 1.5;
    }

    .bullet-dot {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--pink);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
      font-size: 8px;
      color: #fff;
      font-weight: 700;
    }

    .free-cta {
      display: block;
      text-align: center;
      background: var(--pink);
      color: var(--white);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.04em;
      padding: 13px 22px;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 20px rgba(255, 45, 122, 0.35);
      transition: transform 0.15s;
      margin-bottom: 10px;
    }

    .free-cta:hover {
      transform: translateY(-2px);
    }

    .free-whatsapp {
      display: block;
      text-align: center;
      font-size: 12px;
      color: rgba(255, 255, 255, 0.45);
      text-decoration: none;
    }

    /* ── SHARED SECTION ── */
    .section {
      padding: 32px 24px;
    }

    .sec-label {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--purple-light);
      margin-bottom: 8px;
    }

    .sec-label::after {
      content: '';
      flex: 1;
      height: 0.5px;
      background: rgba(167, 139, 250, 0.2);
    }

    .section-title {
      font-family: 'Syne', sans-serif;
      font-size: 28px;
      line-height: 1.15;
      font-weight: 800;
      color: var(--white);
      margin-bottom: 20px;
    }

    .section-title .accent {
      color: var(--pink);
    }

    /* ── COURSE CARDS ── */
    .course-grid {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .course-card {
      background: var(--card);
      border: 0.5px solid var(--border);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
      transition: border-color 0.2s, background 0.2s;
    }

    .course-card:hover {
      border-color: rgba(255, 45, 122, 0.3);
      background: var(--bg3);
    }

    .course-icon {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: var(--pink-pale);
      border: 0.5px solid var(--border-pink);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      flex-shrink: 0;
    }

    .course-week {
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--pink);
      margin-bottom: 4px;
    }

    .course-card h3 {
      font-size: 13.5px;
      font-weight: 600;
      color: var(--white);
      margin-bottom: 4px;
    }

    .course-card p {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.6;
    }

    /* ── DIVIDER ── */
    .divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(123, 94, 167, 0.2), transparent);
      margin: 0 24px;
    }

    /* ── PRICING ── */
    .pricing-section {
      padding: 32px 24px 0;
    }

    .pricing-box {
      border: 1px solid rgba(255, 45, 122, 0.25);
      border-radius: 20px;
      overflow: hidden;
      background: var(--card);
      box-shadow: 0 0 40px rgba(255, 45, 122, 0.06);
    }

    .price-head {
      background: linear-gradient(135deg, rgba(255, 45, 122, 0.1), rgba(123, 94, 167, 0.1));
      padding: 22px 22px 18px;
      border-bottom: 0.5px solid rgba(255, 45, 122, 0.15);
    }

    .price-label {
      font-size: 10px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--pink);
      margin-bottom: 6px;
    }

    .price-amount {
      font-family: 'Syne', sans-serif;
      font-size: 46px;
      font-weight: 800;
      color: var(--white);
      line-height: 1;
    }

    .price-currency {
      font-size: 18px;
      color: var(--pink-soft);
      margin-right: 2px;
    }

    .price-sub {
      font-size: 12px;
      color: var(--muted);
      margin-top: 5px;
    }

    .price-body {
      padding: 20px 22px;
    }

    .price-feat {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: rgba(255, 255, 255, 0.7);
      padding: 7px 0;
      border-bottom: 0.5px solid rgba(255, 255, 255, 0.04);
    }

    .price-feat:last-child {
      border-bottom: none;
    }

    .price-feat::before {
      content: '';
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--pink);
      flex-shrink: 0;
    }

    .earlybird {
      margin: 12px 24px 0;
      background: linear-gradient(135deg, rgba(255, 45, 122, 0.08), rgba(123, 94, 167, 0.08));
      border: 0.5px solid rgba(255, 45, 122, 0.2);
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .eb-title {
      font-size: 12px;
      font-weight: 600;
      color: var(--pink-soft);
      margin-bottom: 2px;
    }

    .eb-sub {
      font-size: 11px;
      color: var(--muted2);
    }

    .eb-tag {
      background: var(--pink);
      color: var(--white);
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      white-space: nowrap;
      box-shadow: 0 2px 12px rgba(255, 45, 122, 0.4);
    }

    .spacer {
      height: 32px;
    }

    /* ── FACILITATOR ── */
    .facilitator {
      padding: 28px 24px;
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }

    .fac-avatar {
      width: 54px;
      height: 54px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--pink), var(--purple));
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Syne', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--white);
      flex-shrink: 0;
      border: 2px solid rgba(255, 45, 122, 0.3);
    }

    .fac-name {
      font-family: 'Syne', sans-serif;
      font-size: 16px;
      font-weight: 800;
      color: var(--white);
      margin-bottom: 2px;
    }

    .fac-title {
      font-size: 11px;
      color: var(--pink-soft);
      margin-bottom: 6px;
      letter-spacing: 0.02em;
    }

    .fac-bio {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.65;
    }

    /* ── FINAL CTA ── */
    .cta-section {
      position: relative;
      background: linear-gradient(160deg, #1a0a28, #0d0d1a);
      border-top: 0.5px solid rgba(255, 45, 122, 0.15);
      padding: 36px 24px 48px;
      text-align: center;
      overflow: hidden;
    }

    .cta-glow {
      position: absolute;
      top: -60px;
      left: 50%;
      transform: translateX(-50%);
      width: 300px;
      height: 200px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(255, 45, 122, 0.12), transparent 70%);
      pointer-events: none;
    }

    .cta-title {
      font-family: 'Syne', sans-serif;
      font-size: 26px;
      font-weight: 800;
      color: var(--white);
      line-height: 1.2;
      margin-bottom: 8px;
    }

    .cta-title .accent {
      color: var(--pink);
    }

    .cta-sub {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.65;
      margin-bottom: 28px;
    }

    .cta-btn {
      display: inline-block;
      background: var(--pink);
      color: var(--white);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.04em;
      padding: 16px 38px;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 8px 30px rgba(255, 45, 122, 0.4);
      transition: transform 0.15s, box-shadow 0.15s;
      margin-bottom: 12px;
    }

    .cta-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 40px rgba(255, 45, 122, 0.5);
    }

    .cta-note {
      font-size: 11px;
      color: var(--muted2);
      margin-bottom: 10px;
    }

    .cta-whatsapp {
      display: block;
      font-size: 12px;
      color: rgba(255, 255, 255, 0.35);
      text-decoration: none;
      margin-top: 8px;
    }

    /* ── FOOTER ── */
    footer {
      padding: 20px 24px;
      text-align: center;
      border-top: 0.5px solid rgba(255, 255, 255, 0.05);
    }

    .footer-brand {
      font-family: 'Syne', sans-serif;
      font-size: 14px;
      color: var(--pink-soft);
      display: block;
      margin-bottom: 4px;
      letter-spacing: 0.05em;
    }

    .footer-contact {
      font-size: 11px;
      color: var(--muted2);
      margin-top: 2px;
    }

  </style>
</head>
<body>

  <!-- ── HERO ── -->
  <section class="hero">
    <div class="hero-glow"></div>

    <div class="hero-brand">
      <div class="hero-brand-dot"></div>
      CodeMaestra Academy
    </div>

    <div class="hero-badge">
      <span class="hero-badge-dot"></span>
      Free 45-min taster · Cohort 2 closes June 2
    </div>

    <div class="hero-eyebrow">
      <div class="hero-eyebrow-line"></div>
      Generative AI · 6-Week Programme · Cohort 2
    </div>

    <h1 class="hero-title">
      AI is already<br>
      at your desk.<br>
      <span class="accent">Are you ready?</span>
    </h1>

    <p class="hero-sub">
      A customised generative AI course for professionals, business owners,
      and educators — built around <strong>your actual work</strong>, not a generic textbook.
    </p>

    <div class="hero-stats">
      <div class="stat">
        <span class="stat-val">6</span>
        <span class="stat-lbl">Weeks of training</span>
      </div>
      <div class="stat">
        <span class="stat-val">3+</span>
        <span class="stat-lbl">Specialisation tracks</span>
      </div>
      <div class="stat">
        <span class="stat-val">Live</span>
        <span class="stat-lbl">Hands-on sessions</span>
      </div>
      <div class="stat">
        <span class="stat-val">🏅</span>
        <span class="stat-lbl">Certificate included</span>
      </div>
    </div>
  </section>

  <!-- ── FREE TASTER ── -->
  <div class="free-section">
    <div class="free-section-glow"></div>

    <p class="free-label">⚡ Start here — completely free</p>
    <h2 class="free-title">Try a free taster first.</h2>
    <p class="free-date">45-minute session · New cohort every 2nd of the month · Cohort 2 deadline: June 2</p>
    <p class="free-desc">
      Not sure if this is for you? Join our free 45-minute taster and experience
      AI firsthand — no tech background needed, just bring your phone or laptop.
    </p>

    <div class="free-bullets">
      <div class="free-bullet">
        <div class="bullet-dot">✓</div>
        Discover what AI is — and what it is NOT — through live prompts across different models
      </div>
      <div class="free-bullet">
        <div class="bullet-dot">✓</div>
        Watch a real work problem get solved live in under 2 minutes
      </div>
      <div class="free-bullet">
        <div class="bullet-dot">✓</div>
        Try it yourself — hands on, no experience needed
      </div>
      <div class="free-bullet">
        <div class="bullet-dot">✓</div>
        Early bird discount when you enrol on the day
      </div>
    </div>

    <a class="free-cta" href="mailto:codemaestraacademy@gmail.com?subject=Free%20Taster%20Session%20Sign%20Up">
      Reserve your free spot →
    </a>
    <a class="free-whatsapp" href="https://wa.me/254759637006?text=Hi%20Merita%2C%20I%27d%20like%20to%20reserve%20a%20spot%20for%20the%20free%20AI%20taster%20session">
      or WhatsApp us → 0759 637 006
    </a>
  </div>

  <!-- ── COURSE OUTLINE ── -->
  <section class="section">
    <p class="sec-label">The 6-week programme</p>
    <h2 class="section-title">
      Built for your<br>
      <span class="accent">real world.</span>
    </h2>

    <div class="course-grid">
      <div class="course-card">
        <div class="course-icon">🧠</div>
        <div>
          <p class="course-week">Weeks 1 – 2 · Foundation for everyone</p>
          <h3>AI Fundamentals + Ethics + Prompt Engineering</h3>
          <p>What AI really is, how it works, where it fails, data privacy, plagiarism, bias — and the skill that unlocks everything: prompt engineering.</p>
        </div>
      </div>
      <div class="course-card">
        <div class="course-icon">💼</div>
        <div>
          <p class="course-week">Week 3 · Specialisation track</p>
          <h3>AI for Your Business</h3>
          <p>FAQ chatbots, content pipelines, automated reports, marketing copy, sales tools — turn AI into a real business growth engine.</p>
        </div>
      </div>
      <div class="course-card">
        <div class="course-icon">🎓</div>
        <div>
          <p class="course-week">Week 4 · Specialisation track</p>
          <h3>AI in the Classroom</h3>
          <p>For educators: stop fighting AI plagiarism and start using it as your most powerful teaching tool. Lesson plans, rubrics, AI-proof assignments.</p>
        </div>
      </div>
      <div class="course-card">
        <div class="course-icon">🛠️</div>
        <div>
          <p class="course-week">Week 5 · Specialisation track</p>
          <h3>Beyond ChatGPT — The Full Tool Landscape</h3>
          <p>Claude, Gemini, Perplexity, Canva AI, Notion AI, ElevenLabs, Runway and more. Know exactly which tool to reach for and when.</p>
        </div>
      </div>
      <div class="course-card">
        <div class="course-icon">🚀</div>
        <div>
          <p class="course-week">Week 6 · Project week</p>
          <h3>AI Project Showcase + Certificate</h3>
          <p>You present your own AI solution to the group — a chatbot, automation workflow, classroom plan, or business tool. Certificate awarded.</p>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ── PRICING ── -->
  <section class="pricing-section">
    <p class="sec-label">Investment</p>
    <h2 class="section-title">
      What's it<br>
      <span class="accent">worth to you?</span>
    </h2>

    <div class="pricing-box">
      <div class="price-head">
        <p class="price-label">Full programme · Cohort 2 starts June 2</p>
        <p class="price-amount">
          <span class="price-currency">KES</span>10,000
        </p>
        <p class="price-sub">6 weeks · 12 hours of live training · Certificate included</p>
      </div>
      <div class="price-body">
        <div class="price-feat">All 5 taught sessions — 2 hours each</div>
        <div class="price-feat">Week 6 project showcase + certificate ceremony</div>
        <div class="price-feat">Personal prompt library — yours to keep</div>
        <div class="price-feat">AI tool comparison matrix handout</div>
        <div class="price-feat">30-day personal AI action plan</div>
        <div class="price-feat">Curated resource pack — tools, newsletters, communities</div>
        <div class="price-feat">Access to course WhatsApp community</div>
      </div>
    </div>
  </section>

  <div class="earlybird">
    <div>
      <p class="eb-title">Early bird discount</p>
      <p class="eb-sub">Sign up at the free session · Limited spots</p>
    </div>
    <div class="eb-tag">Save 15%</div>
  </div>

  <div class="spacer"></div>
  <div class="divider"></div>

  <!-- ── FACILITATOR ── -->
  <div class="facilitator">
    <div class="fac-avatar">MO</div>
    <div>
      <p class="fac-name">Merita Odera</p>
      <p class="fac-title">MLOps Engineer in Training · AI Educator &amp; Trainer</p>
      <p class="fac-bio">
        Founder of CodeMaestra Academy, Kenya. Merita bridges the gap between technical AI
        knowledge and practical everyday use — helping professionals, educators, and business
        owners harness AI with confidence.
      </p>
    </div>
  </div>

  <div class="divider"></div>

  <!-- ── FINAL CTA ── -->
  <section class="cta-section">
    <div class="cta-glow"></div>

    <h2 class="cta-title">
      Don't wait until AI<br>
      replaces <span class="accent">what you do.</span>
    </h2>
    <p class="cta-sub">
      Join Cohort 2 starting June 2. Seats are kept small so every
      session stays personal and hands-on.
    </p>
    <a class="cta-btn" href="mailto:codemaestraacademy@gmail.com?subject=AI%20Course%20Enrolment">
      Enrol now →
    </a>
    <p class="cta-note">Or attend the free session first — no obligation</p>
    <a class="cta-whatsapp" href="https://wa.me/254759637006?text=Hi%20Merita%2C%20I%27d%20like%20to%20enrol%20in%20the%20CodeMaestra%20AI%20Course">
      💬 WhatsApp: 0759 637 006
    </a>
  </section>

  <!-- ── FOOTER ── -->
  <footer>
    <span class="footer-brand">CodeMaestra Academy</span>
    <p class="footer-contact">codemaestraacademy@gmail.com</p>
    <p class="footer-contact">0759 637 006 · Kenya</p>
  </footer>

</body>
</html>