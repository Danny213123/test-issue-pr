from datetime import datetime
import os
import re
import sys
from numpy import remainder as rem

def gather_args():
    args = sys.argv[1:]
    if len(args) < 14:
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
    blog_amd_deployment = args[13]

    # check all of the date formats

    # amd blog release date format Day-of-week Month Day, 12:00:00 PST Year
    # calculate the day of week based on the date

    today = datetime.today().strftime("%b %d %Y")
    
    weekday_names = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    weekday = weekday_names[datetime.today().weekday()]
    
    day, month, year = today.split(" ")

    blog_template = """---
blogpost: true
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
        "amd_deployment": "{blog_amd_deployment}"
        "amd_product_type": "{blog_amd_product_type}"
        "amd_developer_tool": "ROCm Software, Open-Source Tools"
        "amd_applications": "{blog_amd_applications}"
        "amd_industries": "{blog_amd_industries}"
        "amd_blog_releasedate": {weekday} {month} {day}, 12:00:00 PST {year}
---
<!---
Copyright (c) {year} Advanced Micro Devices, Inc. (AMD)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
--->

# {blog_title}

ROCm Blogs follow a consistent magazine article approach where there is no explicit introduction per se,
but rather each blog starts with a brief, wide-scoped introductory text, without a section title,
before moving into the blog’s first section.
The introductory text should include a concise description of your blog: briefly describe for the
reader how they will benefit from the blog, detailing its main deliverables. Please use an active-voice,
call-to-action approach.

## Body

This is a table.
|      | SPX (MI300X) | CPX (MI300X) |
| ---- | :----------: | :----------: |
| NPS1 |      ✔       |      ✔       |
| NPS4 |              |      ✔       |

Below is a code snippet from the console. You can also use bash, C++, python and other languages.

```console
echo "c 226:128 rwm" > /sys/fs/cgroup/devices/devices.deny #Deny access to device 226:128 in docker (renderD128)

echo "c 226:128 rwm" > /sys/fs/cgroup/devices/devices.allow #Allow access to device 226:128 in docker (renderD128)
```

```{note}
This is how to add a note. See the [myst markdown admomition guide](https://mystmd.org/guide/admonitions) for more details.
```

## Summary

ROCm Blogs follow a consistent magazine-article approach where each blog ends with a “Summary” section.
Please provide a brief summary of your blog, reiterating the main takeaways and deliverables, as well
as what the reader learned from it.

## Disclaimers

Third-party content is licensed to you directly by the third party that owns the
content and is not licensed to you by AMD. ALL LINKED THIRD-PARTY CONTENT IS
PROVIDED “AS IS” WITHOUT A WARRANTY OF ANY KIND. USE OF SUCH THIRD-PARTY CONTENT
IS DONE AT YOUR SOLE DISCRETION AND UNDER NO CIRCUMSTANCES WILL AMD BE LIABLE TO
YOU FOR ANY THIRD-PARTY CONTENT. YOU ASSUME ALL RISK AND ARE SOLELY RESPONSIBLE
FOR ANY DAMAGES THAT MAY ARISE FROM YOUR USE OF THIRD-PARTY CONTENT.
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
        blog_amd_deployment=blog_amd_deployment,
        note="{note}",
    )

    directory_name = truncate_string(blog_title)

    os.makedirs(f"blogs/{directory_name}", exist_ok=True)

    # create README.md
    with open(f"blogs/{directory_name}/README.md", "w") as f:
        f.write(blog_template)

    return None

if __name__ == "__main__":
    create_blog_post_from_args()
