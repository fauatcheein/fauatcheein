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
    <img src="{{ '/assets/img/profile.jpg' | relative_url }}" alt="Portrait of {{ site.author.name }}" width="400" height="400">
  </figure>
</section>

<section class="stats">
  <div><strong>200+</strong><span>peer-reviewed papers</span></div>
  <div><strong>4,200+</strong><span>citations</span></div>
  <div><strong>£14M+</strong><span>external research funding</span></div>
  <div><strong>13</strong><span>PhD graduates</span></div>
  <div><strong>Top 2%</strong><span>Stanford/Elsevier scientists, 2023–2026</span></div>
</section>

<section class="two-col">
  <div>
    <h2>About</h2>
    <p>I am Professor of Engineering and Director of the Harper Institute of Technology at Harper Adams University, UK, which I joined in October 2024 to build the research dimension of the Engineering Department. The institute brings together the university's robotics, AI, mechatronics and digital-agriculture research and postgraduate training.</p>
    <p>I lead <strong>Transformative Farming</strong>, an awarded £5M Leverhulme Trust doctoral scholarships programme with responsible AI at its core, and I am Co-Lead of the £9.13M <strong>UKRI AI Centre for Doctoral Training in Dependable and Deployable AI for Robotics</strong>. I am also UK lead of the Horizon Europe doctoral network <strong>AIGreenbots</strong>.</p>
    <p>I trained as an electronics engineer at the National University of Tucumán and completed my MSc and PhD in Control Systems Engineering at the National University of San Juan, Argentina, with a thesis on mobile-robot SLAM. Before Harper Adams I was Associate Professor at Heriot-Watt University and the National Robotarium (2022–2024), and for over a decade a member of faculty at Universidad Técnica Federico Santa María (UTFSM), Chile, where I headed the PhD and MSc programmes. My career has taken me across Argentina, Chile, Spain, Brazil, Portugal and many other countries, and I collaborate widely across Europe, the Americas and Asia.</p>
    <p>I am a Fellow of the Institution of Agricultural Engineers and of the Royal Society of Biology, and a Senior Member of the IEEE. I serve as Associate Editor of the <em>Journal of Field Robotics</em>, <em>Computers and Electronics in Agriculture</em> and <em>Biosystems Engineering</em>, and Technical Editor of <em>IEEE/ASME Transactions on Mechatronics</em>.</p>
    <p><a href="{{ '/cv/' | relative_url }}">Read the full CV</a></p>
  </div>
  <div>
    <h2>Research interests</h2>
    <p class="meta">Select a topic to see related publications.</p>
    {% for area in site.data.topics %}{% if area.key != "cross" %}
    <div class="tag-area area-{{ area.key }}">
      <span class="area-name">{{ area.area }}</span>
      <ul class="tags">
        {% for t in area.topics %}{% assign n = site.data.publications | where_exp: "p", "p.topics contains t.slug" | size %}{% if n > 0 %}<li><a href="{{ '/publications/' | relative_url }}?topic={{ t.slug }}">{{ t.label }}</a></li>
        {% endif %}{% endfor %}
      </ul>
    </div>
    {% endif %}{% endfor %}
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
  <div class="contact-row">
    <p><span class="email">{{ site.author.email }}</span><br>{{ site.author.affiliation }}<br>
    <a href="{{ site.links.linkedin }}">Connect on LinkedIn</a></p>
    <figure class="qr">
      <a href="{{ site.links.linkedin }}"><img src="{{ '/assets/img/linkedin-qr.svg' | relative_url }}" alt="QR code linking to Fernando Auat Cheein's LinkedIn profile" width="132" height="132"></a>
      <figcaption>Scan for LinkedIn</figcaption>
    </figure>
  </div>
</section>
