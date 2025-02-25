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
    blog_kvp = args[6]
    blog_keywords = args[7]
    blog_amd_technical_blog_type = args[8]
    blog_amd_product_type = args[9]
    blog_amd_developer_type = args[10]
    blog_amd_applications = args[11]
    blog_amd_industries = args[12]

    metadata = {
        "blogpost": False,
        "blog_title": blog_title,
        "date": blog_release_date,
        "author": blog_authors,
        "thumbnail": "",
        "tags": blog_tags,
        "category": blog_category,
        "target_audience": blog_audience,
        "key_value_propositions": blog_kvp,
        "language": "English",
        "myst": {
            "html_meta": {
                "author": blog_authors,
                "description lang=en": blog_title,
                "keywords": blog_keywords,
                "property=og:locale": "en_US",
                "amd_category": "",
                "amd_asset_type": "",
                "amd_blog_type": "",
                "amd_technical_blog_type": blog_amd_technical_blog_type,
                "amd_developer_type": blog_amd_developer_type,
                "amd_deployment": "",
                "amd_product_type": blog_amd_product_type,
                "amd_developer_tool": "",
                "amd_applications": blog_amd_applications,
                "amd_industries": blog_amd_industries,
                "amd_blog_releasedate": blog_release_date,
            }
        }
    }

    # Now proceed with creating the new blog post using metadata.
    print("Metadata received:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    # ... (rest of your blog post creation code) ...

if __name__ == "__main__":
    create_blog_post_from_args()
