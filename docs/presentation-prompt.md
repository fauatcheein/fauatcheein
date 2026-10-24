# Prompt: "Fernando Auat Cheein in two minutes"

Use this prompt (with the CV and the Scopus export) to create or regenerate the auto-playing
presentation on the home page. It is written for a human designer or an AI assistant.

---

**Role.** You are a science communicator and information designer. Build a short, self-running
presentation that introduces Prof. Fernando Auat Cheein to a first-time visitor of his website.

**Audience.** Prospective PhD students and postdocs, industry partners, funders and fellow academics.
Most will give it under two minutes, often while scrolling. Many read in English as a second language.

**Goal.** After watching, the visitor should remember three things:
1. He builds robots and AI for agriculture that can be trusted in real fields (perception, autonomy,
   safety certification).
2. His research leaves the lab: patents cited by industry, and work cited in government and
   international policy.
3. He leads people and a global network, and they can join.

**Source of truth.** Use only facts in the CV, the Scopus export and the website. Do not invent
numbers, partners or outcomes. Earlier research lines (medical diagnosis, construction) may appear
only as the origin of patents, never as current research.

**Narrative (one message per slide, 10 slides, about two minutes):**
1. Who: name, role, photo; one-line promise ("Robots and AI that farmers can trust").
2. Why it matters: machines that perceive, decide and can be shown to be safe in real fields.
3. How: the three pillars of the Harper Institute of Technology (Digital Twinning, AI, Robotics).
4. Path: two decades, three countries (San Juan, Argentina → UTFSM, Chile → Heriot-Watt → Harper Adams).
5. Now: four current research lines (legged-robot SLAM in orchards, laser weeding, spectral sensing of
   crop water stress and food quality, safety certification ISO 18497/25119).
6. Invention: 24 patent publications across the US, Europe and Latin America, with two or three
   granted examples; five IEEE Chile national innovation awards.
7. Industry uptake: 11 patents filed by companies and universities cite this research
   (Honda, Sony, Stiga, Agreenculture; University of California, Florida A&M, three Chinese universities).
8. Policy: cited in 22 policy documents worldwide (UK Government, European Parliamentary Research
   Service, FAO, EU-OSHA, Publications Office of the EU, EMBRAPA, Italian Ministry of Environment);
   name the two most-cited works (human–robot interaction in future farming; 5G for agricultural robots).
9. Scale and people: 200+ papers, 4,200+ citations, h-index 35 (Scopus) / 42 (Google Scholar),
   Stanford/Elsevier Top 2% 2023–2026, 13 PhD graduates, 73 partner institutions in 21 countries.
10. Invitation: PhD, postdoc, fellowship and industry collaboration, with a clear button.

**Cognitive rules (non-negotiable):**
- One idea per slide. The title states the message as a short sentence (assertion), not a topic label.
- At most 30 words of running text per slide, and at most 4 list items or 4 numbers.
- Evidence under the title: a big number, a short list or a picture. No paragraphs.
- Show each slide long enough to read it: about 3.5 s plus 0.3 s per word (minimum 6 s, maximum 14 s).
- Always show where the viewer is (e.g. "4 / 10"), and let them pause, go back, go forward and swipe.
- Pause while the pointer or keyboard focus is on the presentation. Do not autoplay when the visitor
  has asked for reduced motion.
- Dark text on a light, neutral background; a single accent colour for what the eye must catch first
  (numbers, the title kicker, buttons). Body text contrast of at least 7:1; accent and secondary text at least 4.5:1.
- Keep positions stable: title, evidence and controls appear in the same place on every slide.
- Gentle cross-fade only; no sliding, zooming or decorative animation.

**Visual system.** White background, graphite text (#1F2629), deep green accent (#1E7A4C); Archivo for
titles and numbers, Newsreader for text. One full-bleed photo at most (the mission slide). Big numbers
in the accent colour; organisation names as plain text chips, never as logos.

**Output.** One YAML list (`_data/slides.yml`), one entry per slide, with fields: style, kicker, title,
text, points, numbers, steps, chips, big, image, link, link_text. Timing is computed from the words.

**Check before publishing.** Every number traced to the CV, Scopus or the website; word count and
timing per slide; contrast; desktop and phone screenshots; keyboard and reduced-motion behaviour.
