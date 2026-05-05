from pelican import signals


def add_category_tags(generator):
    category_tags = {}
    for category, articles in generator.categories:
        tag_counts = {}
        for article in articles:
            for tag in getattr(article, "tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        category_tags[category] = sorted(
            tag_counts.items(), key=lambda item: item[0].name
        )

    generator.context["category_tags"] = category_tags


def register():
    signals.article_generator_finalized.connect(add_category_tags)
