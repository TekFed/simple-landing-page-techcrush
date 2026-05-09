const fs = require('fs');
const path = require('path');

const files = ['dist/index.html', 'dist/styles.css', 'dist/bg_logo.jpg'];
const missing = files.filter((file) => !fs.existsSync(path.resolve(file)));

if (missing.length) {
  console.error('Build verification failed. Missing files:');
  missing.forEach((file) => console.error(`- ${file}`));
  process.exit(1);
}

console.log('✅ Build verification passed. All expected files exist in dist/');
