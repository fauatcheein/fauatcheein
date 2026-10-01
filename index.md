---
layout: default
title: About
---
<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">{{ site.tagline }}</p>
    <h1>Robots, AI and digital twins for the farms of the future.</h1>
    <p class="lead">I lead the <strong>Harper Institute of Technology (HIT)</strong> at Harper Adams University, where my group develops perception, autonomy and safety assurance for agricultural and field robots.</p>
    <p class="actions">
      <a class="btn" href="{{ '/research/' | relative_url }}">Our research</a>
      <a class="btn ghost" href="#contact">Get in touch</a>
    </p>
  </div>
  <figure class="portrait">
    <img src="{{ '/assets/img/profile.svg' | relative_url }}" alt="Portrait of {{ site.author.name }}">
  </figure>
</section>

<section class="stats">
  <div><strong>200+</strong><span>peer-reviewed papers</span></div>
  <div><strong>~40</strong><span>h-index</span></div>
  <div><strong>22</strong><span>patents</span></div>
  <div><strong>Top 2%</strong><span>Stanford/Elsevier scientists, 2023–2025</span></div>
</section>

<section class="two-col">
  <div>
    <h2>About</h2>
    <p>I am Professor of Engineering and Director of the Harper Institute of Technology at Harper Adams University, UK, which I joined in October 2024 to build the research dimension of the Engineering Department. I also hold a post as Profesor Titular at Universidad Técnica Federico Santa María (UTFSM), Chile.</p>
    <p>Before Harper Adams I was Associate Professor at Heriot-Watt University and the National Robotarium (2022–2024). My career has taken me across Argentina, Chile, Spain, Brazil, Portugal and Poland, and I collaborate widely across Europe, the Americas and Australia.</p>
    <p>I am a Fellow of the Institution of Agricultural Engineers and of the Royal Society of Biology, and serve as Associate Editor for the <em>Journal of Field Robotics</em> and <em>IEEE/ASME Transactions on Mechatronics</em>.</p>
  </div>
  <div>
    <h2>Research interests</h2>
    <ul class="tags">
      <li>Agricultural robotics</li>
      <li>AI / ML perception</li>
      <li>Autonomous systems</li>
      <li>LiDAR-based SLAM</li>
      <li>Hyperspectral &amp; multispectral sensing</li>
      <li>Digital twins</li>
      <li>Safety certification (ISO 18497, ISO 25119)</li>
    </ul>
    <h2>Latest news</h2>
    <ul class="news-list">
      {% for post in site.posts limit:3 %}
      <li><span class="meta">{{ post.date | date: "%b %Y" }}</span> <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
</section>

<section id="contact" class="contact">
  <h2>Contact</h2>
  <p>Prospective PhD students, postdocs and industry partners are welcome to get in touch.</p>
  <p><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a><br>{{ site.author.affiliation }}</p>
</section>
