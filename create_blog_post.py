from datetime import datetime
import os
import sys
from numpy import remainder as rem


def is_leap_year(year: int) -> bool:
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_day_of_week(y: int, m: int, d: int) -> str:
    """return day of week of given date as string, using Gauss's algorithm to find it"""

    if is_leap_year(y):
        month_offset = (0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)[m - 1]
    else:
        month_offset = (0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)[m - 1]
    y -= 1
    wd = int(
        rem(d + month_offset + 5 * rem(y, 4) + 4 * rem(y, 100) + 6 * rem(y, 400), 7)
    )

    return ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")[wd]

def gather_args():
    args = sys.argv[1:]
    if len(args) < 13:
        print("Not enough arguments provided.")
        sys.exit(1)
    
    return args

def create_blog_post_from_args():

    args = gather_args()
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

    date_formats = [
                "%d-%m-%Y",  # e.g. 8-08-2024
                "%d/%m/%Y",  # e.g. 8/08/2024
                "%d-%B-%Y",  # e.g. 8-August-2024
                "%d-%b-%Y",  # e.g. 8-Aug-2024
                "%d %B %Y",  # e.g. 8 August 2024
                "%d %b %Y",  # e.g. 8 Aug 2024
                "%d %B, %Y",  # e.g. 8 August, 2024
                "%d %b, %Y",  # e.g. 8 Aug, 2024
                "%B %d, %Y",  # e.g. August 8, 2024
                "%b %d, %Y",  # e.g. Aug 8, 2024
                "%B %d %Y",  # e.g. August 8 2024
                "%b %d %Y",  # e.g. Aug 8 2024
            ]

    for fmt in date_formats:
        try:
            date_string = datetime.strptime(blog_release_date, fmt).strftime(
                "%d %B %Y"
            )
            break
        except ValueError:
            continue

    # check all of the date formats

    # amd blog release date format Day-of-week Month Day, 12:00:00 PST Year
    # calculate the day of week based on the date

    day, month, year = date_string.split(" ")

    month = month[:3]

    date_formats = ["%b", "%B"]

    for fmt in date_formats:
        try:
            d_month = datetime.strptime(month, fmt).month
            break
        except ValueError:
            continue

    day = int(day)
    year = int(year)

    day_of_week = calculate_day_of_week(year, d_month, day)

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
        "amd_blog_releasedate": {dayweek} {month} {day}, 12:00:00 PST {year}
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
        dayweek=day_of_week,
        month=month[:3],
        day=day,
        year=year
    )

    os.makedirs(f"blogs/{blog_title}", exist_ok=True)

    # create README.md
    with open(f"blogs/{blog_title}/README.md", "w") as f:
        f.write(blog_template)

    return None

if __name__ == "__main__":
    create_blog_post_from_args()
