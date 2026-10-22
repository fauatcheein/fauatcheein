---
layout: page
title: Team
permalink: /team/
intro: Researchers working with the group across Harper Adams University and Heriot-Watt University. To date the group has graduated 13 PhDs and supervised 30+ MSc, 10+ MEng and 40+ Bachelor theses.
---
{% for group in site.data.team %}
<h2>{{ group.group }}</h2>
<div class="people">
  {% for m in group.members %}
  <div class="person">
    <strong>{% if m.url %}<a href="{{ m.url }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}</strong>
    <span>{{ m.role }}</span>
    {% if m.topic %}<span class="meta">{{ m.topic }}</span>{% endif %}
    {% if m.email or m.linkedin or m.scholar or m.researchgate or m.orcid %}<span class="person-links">{% if m.email %}<a href="mailto:{{ m.email }}">Email</a>{% endif %}{% if m.linkedin %}<a href="{{ m.linkedin }}">LinkedIn</a>{% endif %}{% if m.scholar %}<a href="{{ m.scholar }}">Google Scholar</a>{% endif %}{% if m.researchgate %}<a href="{{ m.researchgate }}">ResearchGate</a>{% endif %}{% if m.orcid %}<a href="{{ m.orcid }}">ORCID</a>{% endif %}</span>{% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}

## Join us
Interested in a PhD, postdoc or visiting position? [Get in touch]({{ '/#contact' | relative_url }}).
