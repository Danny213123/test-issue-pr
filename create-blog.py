import sys


def create_blog(blog_title, blog_release_date, blog_author, blog_tags, blog_category, blog_audience, blog_key_value_proposition, blog_keywords, blog_amd_technical_blog_type, blog_amd_product_type, blog_amd_developer_type, blog_amd_applications, blog_amd_industries):
    # grab metadata from bash input
    blog_template = """
---
blogpost: false
blog_title: "{blog_title}"
date: {blog_release_date}
author: '{blog_author}'
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
        blog_author=blog_author,
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
    # Read entire input from stdin
    data = sys.stdin.read().strip()
    print("Input from stdin:", data)

    # Split the input into a list
    data_list = data.split("\n")
    print("Split input into a list:", data_list)

    # Extract the metadata from the list
    create_blog(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7], data_list[8], data_list[9], data_list[10], data_list[11])
