---
layout: page
title: Publications
permalink: /publications/
---
<p class="lead">Selected publications. For the complete list see
{% if site.links.scholar %}<a href="{{ site.links.scholar }}">Google Scholar</a>{% endif %}{% if site.links.orcid %} or <a href="{{ site.links.orcid }}">ORCID</a>{% endif %}.</p>

{% assign years = site.data.publications | group_by: "year" | sort: "name" | reverse %}
{% for y in years %}
<h2 class="year">{{ y.name }}</h2>
<ol class="pubs">
  {% for p in y.items %}
  <li>
    <span class="pub-title">{% if p.url %}<a href="{{ p.url }}">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>
    <span class="pub-authors">{{ p.authors }}</span>
    <span class="pub-venue"><em>{{ p.venue }}</em>{% if p.note %} · {{ p.note }}{% endif %}</span>
    {% if p.doi or p.pdf or p.code %}
    <span class="pub-links">
      {% if p.doi %}<a href="https://doi.org/{{ p.doi }}">DOI</a>{% endif %}
      {% if p.pdf %}<a href="{{ p.pdf | relative_url }}">PDF</a>{% endif %}
      {% if p.code %}<a href="{{ p.code }}">Code</a>{% endif %}
    </span>
    {% endif %}
  </li>
  {% endfor %}
</ol>
{% endfor %}
