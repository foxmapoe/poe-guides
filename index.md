---
layout: default
title:
---

Find community-written route and layout guides for the Path of Exile campaign.
Choose an act to browse its areas. Guides are written in Markdown and can be
improved by anyone through a GitHub pull request.

{% for act in site.data.acts %}
## {{ act.name }}

{% assign guides = site.guides | where: "act", act.number | sort: "order" %}
{% if guides.size > 0 %}
{% for guide in guides %}
- [{{ guide.title }}]({{ guide.url | relative_url }}){% if guide.game_version %} — {{ guide.game_version }}{% endif %}
{% endfor %}
{% else %}
No guides yet. [Help write the first one]({{ '/CONTRIBUTING/' | relative_url }}).
{% endif %}

{% endfor %}

## Contribute

Found a better route, a missing landmark, or an outdated screenshot? [Suggest a change on GitHub](https://github.com/foxmapoe/poe-guides/issues/new/choose), or follow the [contribution guide]({{ '/CONTRIBUTING/' | relative_url }}) to edit a guide.
