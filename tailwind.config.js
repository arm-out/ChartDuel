/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
      colors: {
        'spotify-gray': '#282828',
        'spotify-dark': '#121212',
        'spotify-green': '#1ED760',
        'spotify-light': '#777777',
      }
    }
	},
	plugins: []
};
