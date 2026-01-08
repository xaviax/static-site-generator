# Static Site Generator

A Python-based static site generator built as part of the [Boot.dev](https://boot.dev) guided project curriculum.

## Overview

This is a complete implementation of a static site generator that converts markdown files into a fully functional static website. The project demonstrates core programming concepts including file I/O, text parsing, HTML generation, and build automation.

## About This Project

This static site generator was built following the Boot.dev guided project curriculum, which teaches fundamental software engineering concepts through hands-on practice. The project covers:

- Working with markdown syntax and parsing
- HTML template rendering
- File system operations
- Build pipeline automation
- Static asset management

## Features

- **Markdown to HTML Conversion**: Automatically converts markdown files to styled HTML pages
- **Template System**: Uses HTML templates for consistent page layouts across the site
- **Static Asset Handling**: Manages CSS and other static resources
- **Automated Build Process**: Shell scripts automate the site generation workflow
- **Test Suite**: Includes testing scripts to verify functionality
- **GitHub Pages Compatible**: Generated output ready for immediate deployment

## Project Structure

```
static-site-generator/
├── content/          # Source markdown content files
├── docs/             # Generated static site output
├── src/              # Python source code for the generator
├── static/           # Static assets (CSS, images, etc.)
├── build.sh          # Build automation script
├── main.sh           # Main execution script
├── template.html     # HTML page template
├── test.sh           # Test runner script
└── README.md         # Project documentation
```

## Technologies Used

- **Python (93.0%)**: Core generator logic and markdown processing
- **CSS (5.8%)**: Styling for the generated site
- **Bash**: Build automation and scripting
- **HTML**: Page templates and output

## Getting Started

### Prerequisites

- Python 3.x
- Bash shell
- Git (for cloning the repository)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/xaviax/static-site-generator.git
cd static-site-generator
```

2. Verify Python installation:
```bash
python3 --version
```

### Building the Site

Generate your static site by running:

```bash
./build.sh
```

This will:
- Process all markdown files in the `content/` directory
- Apply the HTML template
- Copy static assets
- Output the complete site to the `docs/` directory

### Running Tests

Execute the test suite:

```bash
./test.sh
```

### Development Mode

Run the main script directly:

```bash
./main.sh
```

## How It Works

1. **Content Authoring**: Write your pages in Markdown format in the `content/` directory
2. **Template Processing**: The generator reads `template.html` and prepares it for content injection
3. **Markdown Parsing**: Python scripts parse markdown syntax and convert it to HTML
4. **HTML Generation**: Parsed content is inserted into the template to create complete HTML pages
5. **Asset Management**: Static files (CSS, images) are copied to the output directory
6. **Output**: The complete static site is generated in `docs/` ready for deployment

## Customization

### Adding Content

Create new markdown files in the `content/` directory:

```markdown
# My New Page

This is some content with **bold** and *italic* text.

- List item 1
- List item 2
```

### Modifying the Template

Edit `template.html` to change the site's structure and layout. The template uses placeholder syntax that gets replaced with your content during generation.

### Styling

Customize the appearance by editing CSS files in the `static/` directory.

## Deployment

### GitHub Pages

The generated site in `docs/` is ready for GitHub Pages:

1. Push your repository to GitHub
2. Navigate to Settings → Pages
3. Select your branch and `/docs` folder as the source
4. Your site will be published automatically

### Other Platforms

Upload the contents of the `docs/` directory to any static hosting service like Netlify, Vercel, or a traditional web server.

## Learning Outcomes

This project teaches:

- File system operations and directory traversal
- Text parsing and manipulation
- HTML/CSS basics
- Template rendering concepts
- Build automation with shell scripts
- Software testing fundamentals
- Version control with Git
- Static site deployment

## Boot.dev Curriculum

This project is part of the Boot.dev learning platform's guided project series. Boot.dev offers a hands-on, project-based approach to learning backend development and computer science fundamentals.

Learn more at [boot.dev](https://boot.dev)

## Author

**xaviax**

GitHub: [@xaviax](https://github.com/xaviax)

## Acknowledgments

- [Boot.dev](https://boot.dev) for the guided project curriculum and learning platform
- The Python community for excellent documentation and tools
- GitHub Pages for free static site hosting

## License

Check the repository for license information.

## Contributing

While this is a learning project, feedback and suggestions are welcome! Feel free to:

- Open issues for bugs or questions
- Suggest improvements
- Share your own implementation ideas

---

**Note**: This project represents a complete implementation of the Boot.dev Static Site Generator guided project. It's designed as an educational tool to learn static site generation concepts and Python programming fundamentals.
