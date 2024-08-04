from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Generate static HTML files from Django templates with data'

    def handle(self, *args, **kwargs):
        # Define the data to be used in templates
        context_data = {
            'title': 'My Static Page',
            'content': 'This is some static content.',
        }

        # Define your pages and their corresponding templates
        pages = {
            'index.html': 'index.html',
            'home.html': 'home.html',
            'hello.html': 'hello.html',
        }

        # Directory to save static files
        output_dir = os.path.join(settings.BASE_DIR, 'docs')

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        for filename, template_name in pages.items():
            html_content = render_to_string(template_name, context_data)
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'w') as file:
                file.write(html_content)

        self.stdout.write(self.style.SUCCESS('Successfully generated static HTML files'))
