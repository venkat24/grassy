import markdown
import sys, os
import re
from jinja2 import Environment, PackageLoader, select_autoescape

class BlogProcessor:
    def __init__(self):
        self.blogList = []
        self.populateBlogs()
        self.renderTemplates()

    def populateBlogs(self):
        root_dir = "blogs"
        blog_dir = os.path.abspath(root_dir)
        for root, dirs, files in os.walk(blog_dir):
            for file in files:
                with open(os.path.join(blog_dir,file),'r') as md_file:
                    markdown_text = md_file.read()
                    html_text = markdown.markdown(markdown_text)
                    self.blogList.append({
                        "title"   : file,
                        "content" : html_text
                    })

    def renderTemplates(self):
        template_dir = "templates"
        template_full_dir = os.path.abspath(template_dir)
        env = Environment(
            loader=PackageLoader('grassy', os.path.join('..','templates'))
        )
        template = env.get_template('main.html')
        print(template.render(posts=self.blogList))

if __name__=="__main__":
    blog = BlogProcessor()
