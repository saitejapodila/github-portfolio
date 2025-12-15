<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>PODILA SAI TEJA — Data Science & GenAI Portfolio</title>
  <meta name="description" content="Portfolio of Podila Sai Teja — Data Science & GenAI Intern focused on Python, SQL, EDA, Power BI, and MLOps." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#fdfdfd; --bg-alt:#ffffff; --text:#2c2c2c; --muted:#6b6b6b;
      --acc:#a3c4f3; --acc-2:#b5ead7; --card:#ffffff; --border:#e0e0e0;
      --shadow:0 6px 20px rgba(0,0,0,0.08); --radius:14px; --maxw:1080px;
    }
    *{box-sizing:border-box}
    html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:"Inter",system-ui;}
    a{color:var(--acc);text-decoration:none}
    a:hover{text-decoration:underline}
    .wrap{max-width:var(--maxw);margin:0 auto;padding:28px}
    header{border-bottom:1px solid var(--border);background:#f9f9ff}
    .nav{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 28px;max-width:var(--maxw);margin:0 auto;}
    .brand{display:flex;align-items:center;gap:12px}
    .logo{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--acc),#7b5cff 40%,var(--acc-2));box-shadow:var(--shadow);}
    .brand h1{font-size:18px;margin:0}
    .brand span{display:block;font-size:12px;color:var(--muted)}
    .nav-actions{display:flex;gap:8px;flex-wrap:wrap}
    .btn{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--border);color:var(--text);background:var(--bg-alt);padding:10px 14px;border-radius:12px;font-weight:600;transition:transform .08s ease, box-shadow .2s ease;}
    .btn:hover{transform:translateY(-1px);box-shadow:var(--shadow);}
    .btn-primary{background:linear-gradient(180deg,#a3c4f3,#89abe3);border-color:#89abe3;color:#fff}
    .hero{display:grid;gap:18px;padding:38px;border:1px solid var(--border);border-radius:var(--radius);background:linear-gradient(135deg,#a3c4f3 20%, #b5ead7 80%);box-shadow:var(--shadow);}
    section{margin:26px 0;padding:26px;border:1px solid var(--border);border-radius:var(--radius);background:var(--card);box-shadow:var(--shadow);}
    section h3{margin:0 0 14px 0;font-size:22px}
    .item{display:grid;gap:8px;padding:14px;border:1px solid #d0d0d0;border-radius:12px;background:#f9f9ff}
    .meta{font-size:12px;color:var(--muted)}
    .list{display:grid;gap:8px;margin-top:8px}
    .list li{list-style:none;position:relative;padding-left:22px}
    .list li::before{content:"▹";position:absolute;left:0;color:var(--acc)}
    .pill span{font-size:12px;border:1px solid #d0d0d0;border-radius:999px;padding:6px 10px;background:#f9f9ff}
    .cards{display:grid;gap:12px}
    .card{border:1px solid #d0d0d0;border-radius:12px;background:#f9f9ff;padding:16px}
    footer{margin:30px 0;padding:24px;border-top:1px solid var(--border);color:var(--muted);text-align:center}
  </style>
</head>
<body>
<header>
  <nav class="nav">
    <div class="brand">
      <div class="logo"></div>
      <div>
        <h1>PODILA SAI TEJA</h1>
        <span>Data Science & GenAI Intern</span>
      </div>
    </div>
    <div class="nav-actions">
      <a class="btn" href="#projects">Projects</a>
      <a class="btn" href="#experience">Experience</a>
      <a class="btn" href="#contact">Contact</a>
    </div>
  </nav>
</header>

<main class="wrap">
  <section class="hero">
    <h2>Turning data into decisions, and ideas into intelligent systems.</h2>
    <p>Focused on Python, SQL, EDA, Power BI, and GenAI.</p>
  </section>

  <section id="projects">
    <h3>Projects</h3>
    <div class="cards">
      <div class="card">
        <h4>Movies Analysis Dashboard — Power BI</h4>
        <ul class="list"><li>Interactive dashboard with filters</li></ul>
      </div>
      <div class="card">
        <h4>Library Management System — MySQL</h4>
        <ul class="list"><li>Designed relational DB & SQL queries</li></ul>
      </div>
    </div>
  </section>

  <section id="contact">
    <h3>Contact</h3>
    <ul class="list">
      <li>Email: <a href="mailto:saitejapodila2003@gmail.com">saitejapodila2003@gmail.com</a></li>
      <li>GitHub: <a href="https://github.com/saitejapodila" target="_blank">github.com/saitejapodila</a></li>
      <li>LinkedIn: <a href="https://linkedin.com/in/podila-saiteja-50276136b" target="_blank">LinkedIn Profile</a></li>
    </ul>
  </section>
</main>

<footer>
  © 2025 Podila Sai Teja · Built with HTML & CSS
</footer>
</body>
</html>
