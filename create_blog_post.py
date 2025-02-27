from datetime import datetime
import os
import re
import sys
from numpy import remainder as rem

def gather_args():
    args = sys.argv[1:]
    if len(args) < 13:
        print("Not enough arguments provided.")
        sys.exit(1)
    
    return args

def truncate_string(input_string: str) -> str:

    cleaned_string = re.sub(r"[!@#$%^&*?/|]", "", input_string)

    transformed_string = re.sub(r"\s+", "-", cleaned_string)

    return transformed_string.lower()

def create_blog_post_from_args():

    args = gather_args()
    blog_title = args[0]
    blog_authors = args[1]
    blog_tags = args[2]
    blog_category = args[3]
    blog_audience = args[4]
    blog_key_value_proposition = args[5]
    blog_keywords = args[6]
    blog_amd_technical_blog_type = args[7]
    blog_amd_product_type = args[8]
    blog_amd_developer_type = args[9]
    blog_amd_applications = args[10]
    blog_amd_industries = args[11]
    blog_description = args[12]

    # check all of the date formats

    # amd blog release date format Day-of-week Month Day, 12:00:00 PST Year
    # calculate the day of week based on the date

    today = datetime.today().strftime("%b %d %Y")
    weekday = datetime.today().weekday()
    day, month, year = today.split(" ")

    blog_template = """---
blogpost: false
blog_title: "{blog_title}"
date: {today}
author: '{blog_authors}'
thumbnail: ''
tags: {blog_tags}
category: {blog_category}
target_audience: {blog_audience}
key_value_propositions: {blog_key_value_proposition}
language: English
myst:
    html_meta:
        "author": "{blog_authors}"
        "description lang=en": "{blog_description}"
        "keywords": "{blog_keywords}"
        "property=og:locale": "en_US"
        "amd_category": "Developer Resources"
        "amd_asset_type": "Blogs"
        "amd_blog_type": "Technical Articles & Blogs"
        "amd_technical_blog_type": "{blog_amd_technical_blog_type}"
        "amd_developer_type": "{blog_amd_developer_type}"
        "amd_deployment": "Servers"
        "amd_product_type": "{blog_amd_product_type}"
        "amd_developer_tool": "ROCm Software, Open-Source Tools"
        "amd_applications": "{blog_amd_applications}"
        "amd_industries": "{blog_amd_industries}"
        "amd_blog_releasedate": {weekday} {month} {day}, 12:00:00 PST {year}
---
"""
    blog_template = blog_template.format(
        blog_title=blog_title,
        today=today,
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
        weekday=weekday,
        month=month,
        day=day,
        year=year,
        blog_description=blog_description,
    )

    directory_name = truncate_string(blog_title)

    os.makedirs(f"blogs/{directory_name}", exist_ok=True)

    # create README.md
    with open(f"blogs/{directory_name}/README.md", "w") as f:
        f.write(blog_template)

    return None

if __name__ == "__main__":
    create_blog_post_from_args()
