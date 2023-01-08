 // Set the current theme
 function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// Switch between lite and dark themes
function switchTheme() {
    if (localStorage.getItem('theme') === 'dark') {
        setTheme('lite');
    } else {
        setTheme('dark');
    }
}

// Set theme on page load
function loadTheme() {
    if (localStorage.getItem('theme') === 'dark') {
        setTheme('dark');
    } else {
        setTheme('lite');
    }
}

loadTheme();