# TechCrush Assignment Landing Page

A sleek, modern landing page designed for startups, SaaS products, and creative launches. Built with clean HTML and CSS, featuring smooth animations and a responsive design that works beautifully across all devices.

![TechCrush Landing Page](bg_logo.jpg)

## ✨ Features

- **Responsive Design**: Looks great on desktops, tablets, and mobile devices
- **Scroll Animations**: Content sections fade in smoothly as you scroll
- **Light/Dark Mode**: Toggle between themes with preference persistence
- **Fast Performance**: Lightweight, no dependencies or build tools required
- **Accessible**: Built with semantic HTML and proper contrast ratios

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TekFed/simple-landing-page-techcrush.git
   cd simple-landing-page-techcrush
   ```

2. Open `index.html` in your browser

That's it! No server or build process required.

## 📁 Project Structure

```
simple-landing-page-techcrush/
├── index.html          # Main page markup
├── styles.css          # Styles and theme variables
├── bg_logo.jpg         # Hero image asset
└── README.md           # This file
```

## 🛠 Technologies Used

- **HTML5**: Semantic markup and structure
- **CSS3**: Custom properties, flexbox, grid, and animations
- **JavaScript**: Theme switching and scroll animations (vanilla JS)

## 🚀 CI/CD Pipeline

This project includes a GitHub Actions workflow for automated deployment. The pipeline:

- Runs on every push to the `main` branch
- Validates HTML and CSS syntax
- Deploys the static site to GitHub Pages for live preview

Check the workflow file at `.github/workflows/deploy.yml` for details.

## 🎨 Customization

### Changing the Hero Image

Replace `bg_logo.jpg` with your own image. Recommended size: 1200x800px or similar aspect ratio.

### Modifying Colors

Edit the CSS custom properties in `:root` and `[data-theme="light"]` for theme colors.

### Adding Content

Update the HTML in `index.html` to change text, add sections, or modify the layout.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

For questions or suggestions, feel free to open an issue on GitHub.

## Notes

This is a self-contained static project and does not require a server or build tools.