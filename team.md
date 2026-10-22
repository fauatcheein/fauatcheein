---
layout: page
title: Team
permalink: /team/
intro: Researchers working with the group across Harper Adams University, Heriot-Watt University, UTFSM (Chile) and STIIMA (Italy). To date the group has graduated 12 PhDs and supervised 30+ MSc, 10+ MEng and 40+ Bachelor theses.
---
{% for group in site.data.team %}
<h2>{{ group.group }}</h2>
<div class="people">
  {% for m in group.members %}
  <div class="person">
    <strong>{% if m.url %}<a href="{{ m.url }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}</strong>
    <span>{{ m.role }}</span>
    {% if m.topic %}<span class="meta">{{ m.topic }}</span>{% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}

## Join us
Interested in a PhD, postdoc or visiting position? [Get in touch]({{ '/#contact' | relative_url }}).
