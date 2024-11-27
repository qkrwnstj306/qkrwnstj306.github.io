---
layout: post
title:  "StyleBoost: A Study of Personalizing Text-to-Image Generation in Any Style using DreamBooth"
summary: "International Conference on Information and Communication Technology Convergence (ICTC), 2023"
author: Junseo Park
contributors: "Junseo Park, Beomseok Ko, and Hyeryung Jang"
date: '2023-09-11 14:35:23 +0530'
category: paper
thumbnail: /assets/img/posts/styleboost_1.png
keywords: diffusion model, style training, dreambooth
permalink: /blog/styleboost
usemathjax: true
paper_link: "https://ieeexplore.ieee.org/document/10392676"
image: "/assets/img/posts/styleboost_1.png"
---

## Adding Multiple Categories in Posts

To add categories in blog posts all you have to do is add a **category** key with category values in frontmatter of the post :

```yml
---
category: ['jekyll', 'guides', 'sample_category']
---
```

Then to render this category using link and pages. All we need to do is,

1. Create a new file with [your_category_name].md inside categories folder.

2. Copy categories/sample_category.md file and replace the content in [your_category_name].md in that. (Please don't copy the code below its just sample, since it renders the jekyll syntax dynamically)

```jsx
---
layout: page
title: Guides
permalink: /blog/categories/your_category_name/
---

<h5> Posts by Category : {{ page.title }} </h5>

<div class="card">
{% for post in site.categories.your_category_name %}
 <li class="category-posts"><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</div>
```

Using the category, all the posts associated with the category will be listed on
`http://localhost:4000/blog/categories/your_category_name`