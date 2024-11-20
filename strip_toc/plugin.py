from mkdocs.plugins import BasePlugin

class StripTocPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        # Replace the TOC markers in the markdown content
        return markdown.replace('[[_TOC_]]', '').replace('[[_TOSP_]]', '')