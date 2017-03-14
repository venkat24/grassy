import markdown
import sys, os

class BlogProcessor:
    def __init__(self):
        self.blogList = []
        self.populateBlogs()

    def populateBlogs(self):
        root_dir = "blogs"
        blog_dir = os.path.abspath(root_dir)
        for root, dirs, files in os.walk(blog_dir):
            for file in files:
                with open(os.path.join(blog_dir,file),'r') as md_file:
                    markdown_text = md_file.read()
                    html_text = markdown.markdown(markdown_text)
                    print(html_text)

if __name__=="__main__":
    blog = BlogProcessor()
