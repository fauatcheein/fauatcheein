# Personal website — how to edit

| What | Where |
|---|---|
| Name, email, links (Scholar, ORCID…) | `_config.yml` |
| Home page text | `index.md` |
| Research page | `research.md` |
| Publications | `_data/publications.yml` (one block per paper) |
| Team | `_data/team.yml` |
| News item | new file in `_posts/` named `YYYY-MM-DD-title.md` |
| Photo | upload `assets/img/profile.jpg`, then in `index.md` change `profile.svg` to `profile.jpg` |
| Colours / fonts | `assets/css/style.css` (top of file) |

Every edit you commit on GitHub rebuilds the site automatically within ~1 minute.
