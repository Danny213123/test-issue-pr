import sys

def create_blog_post_from_args():
    # sys.argv[0] is the script name; the rest are your inputs
    args = sys.argv[1:]
    if len(args) < 13:
        print("Not enough arguments provided.")
        sys.exit(1)
    blog_title = args[0]
    blog_release_date = args[1]
    blog_authors = args[2]
    blog_tags = args[3]
    blog_category = args[4]
    blog_audience = args[5]
    blog_key_value_proposition = args[6]
    blog_keywords = args[7]
    blog_amd_technical_blog_type = args[8]
    blog_amd_product_type = args[9]
    blog_amd_developer_type = args[10]
    blog_amd_applications = args[11]
    blog_amd_industries = args[12]

    blog_template = """
---
blogpost: false
blog_title: "{blog_title}"
date: {blog_release_date}
author: '{blog_authors}'
thumbnail: ''
tags: {blog_tags}
category: {blog_category}
target_audience: {blog_audience}
key_value_propositions: {blog_key_value_proposition}
language: English
myst:
    html_meta:
        "author": "Danny Guan"
        "description lang=en": "Guide to ROCm Blogs Metadata"
        "keywords": "'{blog_keywords}'"
        "property=og:locale": "en_US"
        "amd_category": "Developer Resources"
        "amd_asset_type": "Blogs"
        "amd_blog_type": "Technical Articles & Blogs"
        "amd_technical_blog_type": "'{blog_amd_technical_blog_type}'"
        "amd_developer_type": "'{blog_amd_developer_type}'"
        "amd_deployment": "Servers"
        "amd_product_type": "'{blog_amd_product_type}'"
        "amd_developer_tool": "ROCm Software, Open-Source Tools"
        "amd_applications": "'{blog_amd_applications}'"
        "amd_industries": "'{blog_amd_industries}'"
        "amd_blog_releasedate": Tue April 16, 12:00:00 PST 2024
---
"""
    blog_template = blog_template.format(
        blog_title=blog_title,
        blog_release_date=blog_release_date,
        blog_authors=blog_authors,
        blog_tags=blog_tags,
        blog_category=blog_category,
        blog_audience=blog_audience,
        blog_key_value_proposition=blog_key_value_proposition,
        blog_keywords=blog_keywords,
        blog_amd_technical_blog_type=blog_amd_technical_blog_type,
        blog_amd_product_type=blog_amd_product_type,
        blog_amd_developer_type=blog_amd_developer_type,
        blog_amd_applications=blog_amd_applications,
        blog_amd_industries=blog_amd_industries,
    )

    print(blog_template)

if __name__ == "__main__":
    create_blog_post_from_args()
